import zipfile
import os ,sys,shutil,time

def zip_ya(startdir,file_news):


    z = zipfile.ZipFile(file_news,'w',zipfile.ZIP_DEFLATED) #参数一：文件夹名
    for dirpath, dirnames, filenames in os.walk(startdir):

        fpath = dirpath.replace(startdir,'') #这一句很重要，不replace的话，就从根目录开始复制
        fpath = fpath and fpath + os.sep or ''#这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
        for filename in filenames:
            if filename.endswith('.had') or filename.endswith('.chk'):

                z.write(os.path.join(dirpath, filename),'20Q4SP1\\'+filename)


                # shutil.move('E:\\pycharm_work_space\\singlecheck\\20Q4SP1.zip', startdir )
    z.close()

    #移动 生产的zip 包地址
    # shutil.move('E:\\pycharm_work_space\\singlecheck\\20Q4SP1.zip', 'E:\\pycharm_work_space\\20Q4SP1')




def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')


if __name__== "__main__":
    zip_ya(startdir='E:\\pycharm_work_space\\20Q4SP1',file_news= 'E:\\pycharm_work_space\\20Q4SP1\\20Q4SP1.zip')

    # unzip_file('E:\\pycharm_work_space\\singlecheck\\2004.zip','E:\\pycharm_work_space\\19692629')

