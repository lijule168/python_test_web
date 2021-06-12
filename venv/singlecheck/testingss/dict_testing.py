import json

#
#
# aa= '{"aa":11,"bb":"22"}'
#
#
# # 将字符串转化为字典
# print(type(json.loads(aa)))
#
#
# bb= {"aa":11,"bb":"22"}
#
# # 将字典转化为字符串
# print(type(json.dumps(bb)))


#替换字典中的值

# bb= {"aa":11,"bb":"22"}
# cc=bb.items()
# dd= 3
#
# del dd

# dd= ' li ju le'
#
# gg=dd.split('j')
#
# aa=dd.strip(' ')
# print(len(aa),len(dd))


# def add(num1,num2):
#     return '{0}+{1}+{2}'.format(num1,num2,num1+num2)
#
#
#
# print(add(2,5))


#
# str = '1234567'
#
# # print (str)          # 输出字符串  Runoob
# # print (str[0:-1])    # 输出第一个到倒数第二个的所有字符  Runoo
# # print (str[0])       # 输出字符串第一个字符  R
# # print (str[2:5])     # 输出从下标第二个开始到小标第四个的字符，注意不是第二个到第五个。noo，所以如果要取后面的数据，建议使用以下[2:]
# # print (str[2:])      # 输出从第三个开始的后的所有字符 noob
# # print (str[:2])  # 输出第一个到第二个的字符 Ru
#
#
# print(str.find('7'))
#


# listss=[1,2,2,3,5,'6']
# listss2=[1,4,6,9,{"aa":99}]
# listss.append(9)
# listss.insert(2,'lijule')
# listss.extend(listss2)
#
# print(listss)
#

#
# a = [1, 2, 3, 5, 4, 6]
# # print (a[:])  #  取整个列表
# # print(a[2:-1]) # -1表述倒数第二个
#
# # print(a[2:0],'---') # 第二个取到全部
# #
# # print(a[2::2]) # 第隔一个数取值
# # [3, 5]
#
# a.reverse()
# print(a)
#
# a.sort()
# a.reverse()
# print(a)


# list1 = [1, 3, 5, 7, 100]
# # # 通过循环用下标遍历列表元素
# # for index in range(len(list1)):
# #     print(list1[index])
# # # 通过for循环遍历列表元素
# # for elem in list1:
# #     print(elem)
# # 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
# for index, elem in enumerate(list1):
#     print(index, elem)


#
# aa=(1,2,3,4,5,['ss','tt','gg'])
#
# aa[5].append('tt')
#
# print(aa)
#

# bb= {1,2,3,4,5,6,7}
#
# # bb.add('lijule')
#
# bb.update([11,22])
# bb.add('lijule')
#
#
# print('lijule' in  bb)
#
#
# a={1,2,'aa','bb'}


a_range = range(10)
# # 对a_range执行for表达式
# a_list = [x * x for x in a_range]
# # a_list集合包含10个元素
# print(a_list)


# b_list = [x + x for x in a_range if x % 2 == 0]
# # a_list集合包含5个元素
# print(b_list)
#
# d_list = [[x, y] for x in range(5) for y in range(4)]
# # d_list列表包含20个元素
# print(d_list)


import re
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配


import re

# line = "Cats are smarter than dogs"
#
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if matchObj:
#     print ("matchObj.group() : ", matchObj.group())
#
#     print ("matchObj.group(1) : ", matchObj.group(1))
#
#     print ("matchObj.group(2) : ", matchObj.group(2))
#
# else:
#     print ("No match!!")
#

import re
# #全文查号匹配
# print(re.search('www', 'wwsw.runoobwww.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoobcom.com').span())         # 不在起始位置匹配
#
# # 只匹配字符串的开始
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))


phone = "2004-959-559 # 这是一个国外电话号码"

# # 删除字符串中的 Python注释
# num = re.sub(r'#.*$', "", phone)
# print ("电话号码是: ", num)
#
#
# # 删除非数字(-)的字符串
# num = re.sub(r'\D', "", phone)
# print ("电话号码是 : ", num)


# # 将匹配的数字乘以 2
# def double(matched):
#     value = int(matched.group('value'))
#     print(value,'---')
#     return str(value * 2)
#
#
#
#
#
# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', '99', s,2))
#
# print(s)
# 第一个参数查找的字符串,第二个参数,被替换的字符串,第三个参数,被处理前的字符串

#?P<value>的意思就是命名一个名字为value的组，匹配规则符合后面的/d+



# s= 'this is a number 23564-235-22-423'
# r=re.match('.+?(\d+-\d+-\d+-\d+)',s)  #非贪婪模式匹配 + 匹配前面字符一次或多次 ?意思是匹配前面字符一次或 0 次
# a=r.group(1)   #提取
# print(a)
#
#
# s= 'this is a number 23564-235-22-423'
# r=re.match('.+(\d+-\d+-\d+-\d+)',s)  #匹配
# a=r.group(1)   #提取
# print(a)


#1234

# aa=[]
#
# for a in range(1,5):
#     for b in range(1, 5):
#         for c in range(1, 5):
#
#             if a !=b and a !=c and b != c :
#                 print(a,b,c)
#
#


#
# aa=[1,3,7,2]
#
# aa.sort()
# aa.reverse()
#
# print(aa)


# upper
# lower



import re
s= 'this is a number 23564-235-22-423'
r=re.match('.+(\d+-\d+-\d+-\d+)',s)  #匹配
a=r.group()   #提取