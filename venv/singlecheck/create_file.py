import os
def mkdir(path):

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print
        path + ' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print
        path + ' 目录已存在'
        return False






#复制文件加改名到某一文件夹

def copy_file(old_path_name,new_path_name):
    import shutil


    shutil.copyfile(old_path_name,new_path_name)


def get_old_file_name(old_path):
    import shutil
    alllist = os.listdir( old_path)


    return alllist







