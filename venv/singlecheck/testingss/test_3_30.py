
#
# 1级
# 问题:编写一个程序，它将找到所有这些数字，可被7整除，但不是5的倍数，2000年至3200年(包括在内)。得到的数字应按逗号分隔的顺序打印在一行上。


# for  a in  range(2000,3201):
#     if a%7 ==0 and a%5 != 0 :
#         print(a ,end= ',')


# 1级
# 问题:编写一个可以计算给定数的阶乘的程序。结果应该以逗号分隔的顺序打印在一行上。假设向程序提供以下输入:8
# 则输出为:40320
# 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。


#
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
# print('请输入一个数字：')
# x=int(input())
# print (fact(x))


# 1级
# 问题:使用给定的整数n，编写一个程序生成一个包含(i, i*i)的字典，该字典包含1到n之间的整数(两者都包含)。然后程序应该打印字典。
# 假设向程序提供以下输入:8
# 则输出为:
# {1:1，2:4，3:9，4:16，5:25，6:36，,7:49，8:64}
# 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。考虑使用dict类型()

# mydict={}
#
# def dicts(i):
#
#    for a  in range(1,i+1):
#        print(a,a*a)
#        mydict[str(a)]= a*a
#
#
#    return mydict
#
#
#
# print('请输入一个数字：')
# x=int(input())
#
# tt=dicts(x)
# print(tt)
#


# print('请输入一个数字：')
# n = int(input())
# d = dict()
# for i in range(1, n + 1):
#     d[i] = i * i
#
# print(d)


# 字符串
# strs= 'sss'
#
# 元祖
# aaa= (1,2,'s')
#
# 列表
# listss= [1,2,3,'5']
#
# 集合
# dicts={1:3,2:6}
#
# 数字
# cc=9.001
#
# print(cc)

# 1级
# 问题:编写一个程序，该程序接受控制台以逗号分隔的数字序列，并生成包含每个数字的列表和元组。假设向程序提供以下输入:
# 34岁,67年,55岁,33岁,12日,98年
# 则输出为:['34'， '67'， '55'， '33'， '12'， '98']
#                ('34'， '67'， '55'， '33'， '12'， '98')
# 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。方法可以将列表转换为元组


# import re
# print('请输入一组数字：')
# values=input()
# k=re.findall(r'[0-9]+',values)
# t=tuple(k)
# print (k)
# print (t)

# 1级
# 问题:定义一个至少有两个方法的类:        getString:从控制台输入获取字符串        printString::打印大写母的字符串。
# 还请包含简单的测试函数来测试类方法。
# 提示:使用_init__方法构造一些参数

# class  getstr:
#
#     def __init__(self):
#         self.string= ''
#
#
#     def getString(self):
#         self.inputString()
#         print('你好',self.string.upper())
#
#     def inputString(self):
#         print('请输入字符串')
#         self.string=input()
#
#
# aa=getstr()
#
# aa.getString()


# 2级
# 问题:
# 编写一个程序，根据给定的公式计算并打印值:。以下是C和H的固定值:C是50。H是30。D是一个变量，
# 它的值应该以逗号分隔的序列输入到程序中。
# 例子假设程序的输入序列是逗号分隔的:100，150，180，
# 程序输出为:18，22，24
# 提示:如果接收到的输出是小数，则应四舍五入到其最近的值(例如，如果接收到的输出是26.0，则应打印为26)。
# 在为问题提供输入数据的情况下，应该假设它是控制台输入。
# import re,math
#
# def myFormat():
#     print('请输入数字')
#     mystr=input()
#     tt=[]
#     dd= re.findall(r'\d+',mystr)
#     print(dd)
#
#     for  a in dd:
#         bb=int(a)
#         qq = math.sqrt((2 * 50 * bb) / 30)
#         qq= int(qq)
#         tt.append(qq)
#
#
#     print(tt)
#
#
# myFormat()


# 2级
# 问题:编写一个程序，以2位数字，X,Y作为输入，生成一个二维数组。数组的第i行和第j列中的元素值应该是i*j。
# 注意:i= 0,1 . .,X - 1;    j = 0, 1,­Y-1。
# 例子假设程序有以下输入:3、5
# 则程序输出为:[[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8]]
# 提示:注意:如果要为问题提供输入数据，应该假设它是一个控制台输入，以逗号分隔。


# print('请输入两个数字：')
# input_str = input()
# dimensions = [int(x) for x in input_str.split(',')]
# rowNum = dimensions[0]
# colNum = dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
#
# print(multilist)
#
# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col] = row * col

# print(multilist)

# 2级
# 问题:编写一个程序，接受逗号分隔的单词序列作为输入，按字母顺序排序后按逗号分隔的序列打印单词。假设向程序提供以下输入:
# without,hello,bag,world
# 则输出为:
# bag,hello,without,world
# 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。

# import re
# mystr= input()
#
# aa= re.findall('[a-z]+',mystr)
#
# aa.sort()
#
# print(' '.join(aa))


# items=[x for x in input().split(',')]
#
# print(items)
# items.sort()
# print (','.join(items))

# 2级
# 问题:编写一个程序，接受一行序列作为输入，并在将句子中的所有字符大写后打印行。
# 假设向程序提供以下输入:
# Hello world
# Practice makes perfect
# 则输出为:
# HELLO WORLD
# PRACTICE MAKES PERFECT
# 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。


# lines = []
# while True:
#     s = input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break;
#
# for sentence in lines:
#     print(sentence)


# 2级
# 问题:编写一个程序，接受一系列空格分隔的单词作为输入，并在删除所有重复的单词并按字母数字排序后打印这些单词。
# 假设向程序提供以下输入:
# hello world and practice makes perfect and hello world again
# 则输出为:
# again and hello makes perfect practice world
# 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。
# 我们使用set容器自动删除重复的数据，然后使用sort()对数据进行排序。

# print('请输入一组字符串：')
# s = input()
# words = [word for word in s.split(" ")]
# print (" ".join(sorted(list(set(words)))))
#


# 问题：编写一个程序，接受一系列逗号分隔的4位二进制数作为输入，然后检查它们是否可被5整除。 可被5整除的数字将以逗号分隔的顺序打印。
# 例：
# 0100,0011,1010,1001
# 那么输出应该是：
# 1010
# 注意：假设数据由控制台输入。
#
# 提示：如果输入数据被提供给问题，则应该假定它是控制台输入。

# myinput=input()
#
# mylist=[ a for a in myinput.split(',') if int(a) % 5 == 0]
#
# mystr= ','.join(mylist)
#
# print(mystr)

# 2级
#
# 题：编写一个程序，它将找到1000到3000之间的所有这些数字（均包括在内），这样数字的每个数字都是偶数。
# 获得的数字应以逗号分隔的顺序打印在一行上。
#
# 提示：如果输入数据被提供给问题，则应该假定它是控制台输入。

# ABd1234@1,a F1#,2w3E*,2We3345
# import re
# value = []
# print("请输入：")
# items=[x for x in input().split(',')]
# for p in items:
#     if len(p)<6 or len(p)>12:
#         continue
#     else:
#         pass
#
#     if not re.search("[a-z]",p):
#         print(re.search("[a-z]",p))
#         continue
#     elif not re.search("[0-9]",p):
#         continue
#     elif not re.search("[A-Z]",p):
#         continue
#     elif not re.search("[$#@]",p):
#         continue
#     elif re.search("\s",p):
#         continue
#     else:
#         pass
#     print(p)
#     value.append(p)
# print (",".join(value))



# for letter in 'Python':  # 第一个实例
#     if letter == 'h':
#         continue
#     elif letter == 'o':
#          # print('小字母 :', letter)
#          continue
#
#     print('当前字母 :', letter)


# var = 10  # 第二个实例
# while var > 0:
#     var = var - 1
#     if var == 5:
#         continue
#     print ('当前变量值 :', var)
#
# print ("Good bye!")

#
# 题：您需要编写一个程序，按升序对（名称，年龄，高度）元组进行排序，其中name是字符串，age和height是数字。 元组由控制台输入。 排序标准是：
# 1：根据名称排序;
# 2：然后根据年龄排序;
# 3：然后按分数排序。
# 优先级是name> age>得分。
# 如果给出以下元组作为程序的输入：
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# 然后，程序的输出应该是：
# [（'John'，'20'，'90'），（'Jony'，'17'，'91'），（'Jony'，'17'，'93'），（'Json'，'21 '，'85'），（'Tom'，'19'，'80'）]
#
# 提示：如果输入数据被提供给问题，则应该假定它是控制台输入。我们使用itemgetter来启用多个排序键。
# import re
# mystr=input()
#
# print(mystr)
# aa= re.split(r'[,\r,\n]',mystr)
#
# # print(aa)

# from operator import itemgetter, attrgetter
#
# l = []
# print("请输入：")
# while True:
#
#     s = input()
#     if not s:
#         break
#     l.append(tuple(s.split(",")))
#
#
# print(l)
# print(sorted(l, key=itemgetter(0, 1, 2)))



# 题：使用生成器定义一个类，该生成器可以在给定范围0和n之间迭代可被7整除的数字。

# def  test(n):
#
#     lists=[]
#     while n >-1:
#         if n%7==0:
#             lists.append(n)
#
#         n -=1
#     yield lists
#
#
# mystr= int(input())
#
# for a in test(mystr): print(a)



#
# def putNumbers(n):
#     i = 0
#     while i < n:
#         j = i
#         i = i + 1
#         if j % 7 == 0:
#             yield j
#
#
# for i in putNumbers(100):
#     print(i)




# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3
# freq = {}  # frequency of words in text
# print("请输入：")
# line = input()
# for word in line.split():
#     print(freq.get(word, 0) + 1)
#     freq[word] = freq.get(word, 0) + 1
# words = sorted(freq.keys())  # 按key值对字典排序
#
# for w in words:
#     print("%s:%d" % (w, freq[w]))


# import re
#
# words = ['fafafasd', 'faFa1asd', 'fafEf21sdfaf', '1afafasdfa', 'faFafas3', '123123123123', 'fFfa13', 'ADFAFADFff',
#          'ADFAFADFF', '12ADFAFADFF']
# all_r_re = re.compile(r'[a-zA-Z0-9]{8,}')  # 包含任意三种字符的组合，包括其中一种或两种
# aA_re = re.compile(r'[a-zA-Z]{8,}')  # 包含任意两种字符的组合，包括其中一种
# ad_re = re.compile(r'[a-z0-9]{8,}')  # 包含任意两种字符的组合，包括其中一种
# Ad_re = re.compile(r'[A-Z0-9]{8,}')  # 包含任意两种字符的组合，包括其中一种
# result = set()  # 利用集合存放不重复的字符
# for w in words:
#     m = all_r_re.search(w)
#     if not m is None:
#         result.add(m.group())
# print (result)
#
#
#
# def remove_w(result, w, *re_s):
#     for r in re_s:
#         m = r.search(w)
#         if (not m is None) and m.group() in result:
#             result.remove(m.group())
#
#
# for w in words:
#     remove_w(result, w, aA_re, ad_re, Ad_re)
#
# print (result)




# 1、匹配一行文字中的所有开头的字母内容



import re
#
# s="i love you not because of who you are,but because of who i am when i am with you"
#
# content=re.findall(r"\b\w",s)      # \b 匹配每个单词开始的字母
#
# print (content)


# 2、匹配一行文字中的所有开头的数字内容

# s="i love you not because 12sd 34er 56df e4 54434"
#
# content=re.findall(r"\b\d",s);
#
# print(content)
# background-color: #faf7ef;">c:\Python27\Scripts>python task_test.py
#
# [‘1‘,‘3‘,‘5‘,‘5‘]


# print (re.match(r"\w+","a123sdf").group())


# 4、 只匹配包含字母和数字的行

# s="i love you not bec_ause\n12sd 34er 56\ndf e4 54434"
#
# content=re.findall(r"\w+",s,re.M)
#
# print(content)

# 5、写一个正则表达式，使其能同时识别下面所有的字符串：

# s="‘bat‘,‘hut,‘bat‘,‘bit‘,‘but‘,‘hat‘,‘hit‘,‘hut‘"
#
# content=re.findall(r"..t",s)
#
# print(content)

# 7、提取每行中完整的年月日和时间字段

# s="""se234 1987-02-09 07:30:00
#
# 1987-02-10 07:25:00"""
#
# content=re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",s)
#
# print(content)

# 8、将每行中的电子邮件地址替换为你自己的电子邮件地址

# s= 'my emall is  www.lijule@mobike.com zhe shi wo shang yi jia gong si de'
#
# content=re.sub(r"[\S]{4,20}.com",r"www.lijule168@163.com",s)
#
# dd=re.findall(r"[\S]{4,20}.com",s)



    # ret = re.match(r"[\w]{4,20}@163.com", email)

# a = re.sub(r'hello', 'i love the', 'hello world')
# print(content,dd)

# 1、使用正则提取出字符串中的单词

# s="""i love you not because of who 234 you are,234 but 3234ser because of who i am when i am with you"""
#
# content=re.findall(r"\b[a-zA-Z]+\b" ,s)
#
#
# print(content)


# s = "yu, Guan bei, Liu fei, Zhang"
#
# m = re.findall(r'([A-Za-z]+),\s([A-Za-z])', s)
#
# print(m)

#
# s = "__hello, python_1, 2world, pra_ni, @dfa_,ewq* "
#
# print(re.findall(r"\b[a-zA-Z_][\w]*", s))


# s = "1180 Bordeaux Drive"
#
# m = re.search(r'\d+( [0-9a-zA-Z]+)+', s)
#
# print(m.group())

# 6. 匹配以“www”起始且以“.com”结尾的简单Web域名:例如,http://www.yahoo.com ，也支持其他域名，如.edu .net等

# s= 'http://www.yahoo.com slkasdgsd salgdjsa g d'
# m = re.search(r'w{3}\.[a-zA-Z]+\.(com|edu|net)',s).group()
# print(m)