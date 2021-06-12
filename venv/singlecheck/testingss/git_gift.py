# import random
#
# def distribute_gift(data):
#     result = {}
#     list1 = list(data.values())
#     for user in data:
#         list2 = list(result.values())
#         new_list = [i for i in list1 if i not in list2]
#
#
#         while not result.get(user): # 如果result中没有这个人员，则可分配礼物
#             random_gift = random.choice(new_list)
#             if data[user] != random_gift:
#                 result[user] = random_gift
#     return result
#
# data = {"A": "礼物A", "B": "礼物B", "C": "礼物C", "D": "礼物D", "E": "礼物E", "F": "礼物F", "G": "礼物G", "H": "礼物H"}
# print("随机分配后：{}".format(distribute_gift(data)))

import random

data = {"A": "礼物A", "B": "礼物B", "C": "礼物C", "D": "礼物D", "E": "礼物E", "F": "礼物F", "G": "礼物G", "H": "礼物H"}


list1= [a  for  a in  data.values()]
# print(random.choice(list1))

data2={}

for  user in  data.keys():
    while not data2.get(user):
        random_gift= random.choice(list1)
        data[user] !=  random_gift
        data2[user] = random_gift




print(data2)


