#!/usr/bin/env python
# -*- coding:utf8 -*-

def dir_class(obj):
    """ dir_class(obj) -> list of string """
    names = dir(obj)
    names = [name for name in names if not name.startswith('_')]
    names = [name for name in names if not name.isupper()]
    request_class = [name for name in names if "Req" in name]
    response_class = [name for name in names if "Resp" in name]
    return request_class, response_class     #返回接收包和发送包的对应类名称列表

def dir_attr(obj):
    """ dir_attr(obj) -> list of string """
    names = dir(obj)
    names = [name for name in names if not name.startswith('_')]
    names = [name for name in names if name.islower()]
    return names                             #返回一个类的内部属性

def gen_req(obj, class_name):
    text = []
    attrs = dir_attr(obj)
    line = gen_func_def(camercase_to_underscore(class_name), attrs)
    text.append(line)
    cp_statement = gen_cp(class_name, attrs)
    text.extend(cp_statement)
    line = "\tsingle_request(req)"
    text.append(line)
    return text                              #生成请求类的函数体

def gen_func_def(func_name, arglist):
    line = "def " + func_name + "("
    if not arglist:
        line += "):"
        return line
    line += ", ".join(arglist) + "):"
    return line

def gen_cp(class_name, attrs):
    text = []
    text.append("\treq = " + class_name + "()")
    for attr in attrs:
        line = "\treq." + attr + " = " + attr
        text.append(line)
    return text

def camercase_to_underscore(var_name):
    result = []
    start = 0
    for i, char in enumerate(var_name):
        if char.isupper():
            result.append(var_name[start:i])
            start = i
    result.append(var_name[start:])
    underscore_name = "_".join([var.lower() for var in result])
    underscore_name = underscore_name[1:]
    return underscore_name                  #驼峰命名法到下划线分割的命名

def underscore_to_camercase(var_name):
    result = var_name.split("_")
    result = [word.capitalize() for word in result]
    return "".join(result)                  #下划线分割的命名到驼峰法命名

def main():
    with open("/Users/dbx/Documents/mobike/project/spider/mobike-api-test/lib/mbmanage/microservice_manage/grpc_py/ridingtrack/ridingtrack_pb2_grpc.py") as fh:
        lines = fh.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("ridingtrack"):
                #import package
                __import__(line, globals(), locals(), [], -1)
                #analysis class
                protobuf_package = eval(line)
                pb2_req, pb2_resp = dir_class(protobuf_package)
                #gen request function and resp printer
                req_funcs = []
                for req in pb2_req:
                    req_func = gen_req(eval(line + "." + req + "()"), req)
                    req_funcs.extend(req_func)
                    req_funcs.append("")
                #write file
                filename = line[len("protobuf") + 1:]
                filename = filename[:-4]
                import_statement = "from " + line + "" + "import *"
                body = "\n".join(req_funcs)
                with open(filename+".py", "w") as f:
                    print(filename)
                    f.write("\n".join([import_statement, body]))

if __name__ == '__main__':
    main()