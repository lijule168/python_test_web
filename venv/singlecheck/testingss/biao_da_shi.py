# def memo(func):
#     cache={}
#     def wrap(*args):
#         if args not in cache:
#             cache[args]=func(*args)
#
#         return cache[args]
#
#     return wrap
#
#
#
#
# @memo
# def fibonaccl(n,cache=None):
#
#     if n<= 1:
#         return 1
#     return fibonaccl(n-1) +fibonaccl(n-2)




# print(fibonaccl(50))




# print(fibonaccl(50))

# @memo
# def climb(n,steps):
#     count = 0
#     if n==0:
#         count=1
#     elif n>0:
#         for step in steps:
#             count += climb(n-step,steps)
#
#     return count
#
#
# print( climb(10,(1,2,3)))


#
# def f(a,b=1,c=[]):
#     '''f function'''
#     #ljdskagsdkjgas
#     print(a,b,c)
#
#     return a*2

#
# def f():
#     a=2
#     return lambda k:a **k
#
#
# g=f()
#
# print(g.__closure__)
#
# c=g.__closure__[0]
#
#
# print(c.cell_contents)

# from functools import update_wrapper,wraps,WRAPPER_ASSIGNMENTS,WRAPPER_UPDATES
#
#
# def mydecorator(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         '''wrapper function'''
#         print('in wapper')
#         func(*args,**args)
#
#     return wrapper
#
# @mydecorator
# def example():
#     '''example function'''
#     print('in function')
#
#
# print(example.__name__)
# print(example.__doc__)




#
# import psycopg2
# # 数据库连接参数
# conn = psycopg2.connect(database="test1", user="jm", password="123", host="127.0.0.1", port="5432")
# cur = conn.cursor()
# cur.execute("SELECT * FROM a1;")
# rows = cur.fetchall()    # all rows in table
# print(rows)
#  conn.commit()
#  cur.close()
#  conn.close()




