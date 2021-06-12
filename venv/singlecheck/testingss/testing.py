# from random import randint
# data = [randint(-10,10) for _  in range(10)]
#
# s=set(data)
#
# print(s)
#
#
# hh={x for x in s if x %3==0}
#
# print(hh)
#




# print(data)
#
# ttt=filter(lambda x: x>=0,data)
# print(list(ttt))
#
#
# print(data)





# d={x:randint(60,100) for x in range(1,20)}
#
# # print(d.items())
#
# gg={k:v for k,v in d.items()  if v > 90 }
#
#
# print(gg)



from collections import Counter

# student = namedtuple('Student',['name','age','emall'])
#
#
#
# s=student(name='jim',age= 16,emall= 'liue@mobill.com')
#
#
#
# print(isinstance(s,tuple))

#
# from random import randint
#
# tt=[randint(0,20) for a in range(20)]
#
#
# c2=Counter(tt)
#
# print(c2.most_common(3))

# import re
#
#
#
#
#
# tt=open('aa.txt',encoding='utf-8').read()
#
# # print(re.split('\W+',tt))
#
#
# gg=Counter(re.split('\W+',tt))
#
#
# print(gg.most_common(10))




# c=dict.fromkeys(tt,0)
#
#
#
#
# for x  in tt:
#
#     c[x] +=1
#
#
# # d_order=sorted(d.items(),key=lambda x:x[1],reverse=False)
#
# gg=sorted(c.items(),key=lambda x:x[1] ,reverse= True)
#
# # print(c)
# # print(gg)

# from random import randint
# data = [randint(-10,10)  for a  in range(10)]
#
#
#
# if 0 in data:
#     print('nishgsd')



# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b  # 使用 yield
#         print (b,'----')
#         a, b = b, a + b
#         n = n + 1
#
#
# for n in fab(5):
#     print (n)


s = 'sa;sdg;/\sss,f;dsfd,sasd|sdf'

#
# import re
#
# tt=re.split(r'[,/\\;|]+',s)
#
# print(tt)


# slist= [s,'']
# print([x for x in slist if x ])
#
#
#
# slist0=[]
# slist=s.split(';')
#
# slist0.extend(slist)
#
#
#
#
#
#
# maplist= map(lambda x:x.split(';'),slist)
#
#
#
# maplist2 = map(lambda x :slist0.extend(x.split(';')),slist)
# for a in slist0 : print(a)



# class A:
#     def a(self):
#         pass
#
#     def b(self):
#         pass
#
#
# class B(A):
#     def c(self):
#         pass
#
#     def d(self):
#         pass
#
#
# def getmembers(klass, members=None):
#     # get a list of all class members, ordered by class
#     if members is None:
#         members = []
#     for k in klass.__bases__:
#         getmembers(k, members)
#     for m in dir(klass):
#         if m not in members:
#             members.append(m)
#     return members
#
#
# print('A=> :', getmembers(A))
# print()
# print('B=> :', getmembers(B))
# print()
# print('IOError=> :', getmembers(IOError))


for a in dir(dict) : print(a)


