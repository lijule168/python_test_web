import configparser


from singlecheck import start_icheck_and_dowload


config = configparser.ConfigParser()


config.read('C:\\singleCheckConfig\\singlecheck.ini')

filepath = config['singlecheck']["filepath"]
# 要压缩的zip 的文件夹路径和名称和执行检查结束后解压文件的地址
filename = config['singlecheck']["filename"]
# 单库执行用户名
username = config['singlecheck']["username"]
# 单库执行的版本
hadDataVersion = config['singlecheck']["hadDataVersion"]
# 单库执行的规则包suitID
suitPackageIDs = config['singlecheck']["suitPackageIDs"]
# 编辑器参与检查的两个图幅的地址
new_file_path_and_name = eval(config['singlecheck']["new_file_path_and_name"])
mesh = eval(config['singlecheck']["mesh"])

# 执行检查的ip+端口
check_url = config['singlecheck']["check_url"]


print(filepath,filename,username,hadDataVersion,suitPackageIDs,new_file_path_and_name,mesh,check_url)




aa= start_icheck_and_dowload.icheck(filepath,filename,username,hadDataVersion,suitPackageIDs,new_file_path_and_name,mesh,check_url)

print(filepath,filename,username,hadDataVersion,suitPackageIDs,new_file_path_and_name,mesh,check_url)
aa.write_chk()


print(username)
print(len(username))






