
import singlecheck.computeMd5
import requests ,json ,time

import singlecheck.create_file
import singlecheck.create_message
from singlecheck import create_zipfile



class icheck:

    def __init__(self,filepath,filename,username,hadDataVersion,suitPackageIDs,new_file_path_and_name,mesh,check_url):

        # 编辑器中要参与检查的 所有图幅的总目录
        self.filepath = filepath
        #要压缩的zip 的文件夹路径和名称和执行检查结束后解压文件的地址
        self.filename= filename
        #单库执行用户名
        self.username= username
        #单库执行的版本
        self.hadDataVersion= hadDataVersion
        #单库执行的规则包suitID
        self.suitPackageIDs= suitPackageIDs
        #编辑器参与检查的两个图幅的地址
        self.new_file_path_and_name = new_file_path_and_name

        self.mesh= mesh


        #执行检查的ip+端口
        self.check_url= check_url

        # # 编辑器中要参与检查的 所有图幅的总目录
        # self.filepath = 'E:\\pycharm_work_space\\20Q4SP1\\'
        # # 要压缩的zip 的文件夹路径和名称和执行检查结束后解压文件的地址
        # self.filename = 'E:\\pycharm_work_space\\20Q4SP1\\20Q4SP1.zip'
        # # 单库执行用户名
        # self.username = 'lijule'
        # # 单库执行的版本
        # self.hadDataVersion = 'HAD_V7.0.0'
        # # 单库执行的规则包suitID
        # self.suitPackageIDs = 390
        # # 编辑器参与检查的两个图幅的地址
        # self.new_file_path_and_name = ['E:\\pycharm_work_space\\lijule\\19692628\\19692628.chk',
        #                                'E:\\pycharm_work_space\\lijule\\19692629\\19692629.chk']
        #
        # self.mesh = ['19692628', '19692629']
        #
        # # 执行检查的ip+端口
        # self.check_url = 'http://10.73.1.31:18898'




    def start_icheck(self):

        singlecheck.create_zipfile.zip_ya(startdir=self.filepath,file_news=self.filename) #压缩had,chk 文件

        zip_path =  self.filename #压缩文件的路径
        print('9999'+zip_path)
        zip_md5= str(singlecheck.computeMd5.get_file_md5(zip_path)) #获取压缩文件的 md5 码


        url=self.check_url+'/qavalidator/had/single/taskqueue/start?MD5='+zip_md5+'&hadDataVersion='+self.hadDataVersion+'&suitPackageIDs='+str(self.suitPackageIDs)+'&token=9999&username='+self.username

        filees={'file':open(zip_path,'rb')}
        print(filees)

        # 执行单库理论检查
        response_check=requests.post(url,  files=filees)



        print(response_check.json())

        return response_check


    def check_state(self):

        taskid = self.start_icheck() .json().get('data')



        resp= requests.get(self.check_url+'/qavalidator/had/querystate/'+taskid).json()

        # downloadURL = resp.get('downloadURL')

        status= resp.get('data').get('status')


        print(status+'9999999-9999999')
        while status!= '4':
            resp = requests.get(self.check_url + '/qavalidator/had/querystate/' + taskid).json()
            print(resp)
            status =  resp.get('data').get('status')

            time.sleep(10)
            print(status,'-999999999999999999--')
            continue
            if status == '4':
                return

        resp = requests.get(self.check_url + '/qavalidator/had/querystate/' + taskid).json()
        return resp.get('data').get('downloadURL')



    # def write_chk(self):
    #     wurl= self.check_state()
    #
    #     r=requests.get(wurl)
    #     with open('2003.zip','wb' ) as code:
    #         code.write(r.content)
    #
    #     #解压下载好的临时文件到新的临时目录
    #
    #     #解压前zip的文件目录
    #     zippaths = self.filename.split('\\')
    #     dstDir = ''
    #
    #     for a in range(0, len(zippaths) - 2):
    #         dstDir = dstDir + '\\' + zippaths[a]
    #         print(dstDir)
    #
    #     print(dstDir)
    #
    #
    #     create_zipfile.unzip_file(dst_dir=dstDir, zippath=self.filename)
    #
    #
    #     #解压后的文件夹下的所有文件的URL
    #
    #
    #     dstDirList = []
    #
    #     meshlist=self.mesh
    #
    #
    #
    #     for a in range (0,len(meshlist)-1):
    #
    #         dstDirList.append(dstDir+'\\'+meshlist[a])
    #
    #
    #
    #
    #     tt=singlecheck.create_message.createMessage().copy_file(old_file_path_and_name=dstDirList,new_file_path_and_name=self.new_file_path_and_name)
    #
    #
    #     print(tt)

    def write_chk(self):
        wurl = self.check_state()

        r = requests.get(wurl)
        with open(self.filename, 'wb') as code:
            code.write(r.content)

        # 解压下载好的临时文件到新的临时目录

        # 解压前zip的文件目录
        zippaths = self.filename.split('\\')
        dstDir = ''

        for a in range(0, len(zippaths) - 1):
            if dstDir == '':
                dstDir =  zippaths[a]
                print(dstDir)
            else:
                dstDir =dstDir+'\\'+ zippaths[a]

        print(dstDir,self.filename)

        create_zipfile.unzip_file(dst_dir=dstDir, zip_src=self.filename)

        # 解压后的文件夹下的所有文件的URL

        dstDirList = []

        meshlist = self.mesh

        for a in range(0, len(meshlist) ):
            dstDirList.append(dstDir + '\\' + meshlist[a]+'.chk')


        print('1111111111111',dstDirList)
        tt = singlecheck.create_message.createMessage().copy_file(old_file_path_and_name=dstDirList,
                                                                  new_file_path_and_name=self.new_file_path_and_name)

        print(tt)


    def testing_method(self):

            self.write_chk()





# aa=icheck()
#
# aa.testing_method()
# gg=icheck()
#
# gg.testing_method()



