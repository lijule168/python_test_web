from singlecheck import  create_file

import re

##内网分析，自动将文件放入指定文件夹



class createMessage:
    def __init__(self):
        self.old_file_path = "E:\\pycharm_work_space\\19692629"
        pass


    def create_dir(self,dir_list_path):
        for a in dir_list_path:
         create_file.mkdir(a)



#获取旧的文件,拼接新的文件夹名称
    def get_file_path_name(self):



        old_file_name = create_file.get_old_file_name(self.old_file_path)


        #数据去重
        new_dir_name_set = set()
        # 拼接要创建的文件夹路径名称
        new_dir_name_list = []
        for a in old_file_name:
            new_dir_name_set.add(int(a.split('.') [0]))

        had_chk=['.chk']
        new_dir_list=[]

        for a in new_dir_name_set:
            for c in had_chk:
                new_dir_name_list.append(self.old_file_path + "2\\" +str(a)+"\\"+ str(a)+c)

            new_dir_list.append(self.old_file_path +"2\\"+ str(a))



        return new_dir_name_list,new_dir_name_set,new_dir_list



#将指定的文件复制到指定的文件夹
    def copy_file(self,new_file_path_and_name,old_file_path_and_name):
        #获取旧的文件加路径




        # new_file_path_and_name = ['E:\\pycharm_work_space\\lijule\\19692628\\19692628.chk','E:\\pycharm_work_space\\lijule\\19692629\\19692629.chk']
        # old_file_path_and_name=['E:\\pycharm_work_space\\singlecheck\\2004\\19692628.chk','E:\\pycharm_work_space\\singlecheck\\2004\\19692629.chk']





        #复制文件
        for a in  range(0,len(old_file_path_and_name)):
            print(a)
            print(old_file_path_and_name[a], new_file_path_and_name[a])
            create_file.copy_file(old_file_path_and_name[a], new_file_path_and_name[a])








        return "复制成功",old_file_path_and_name,new_file_path_and_name







    def testing_method(self):

            aa=self.copy_file()
            print(aa)






# aa=create_message()

# aa.testing_method()



