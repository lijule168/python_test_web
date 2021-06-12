import configparser as cp

filepath = '.\config.ini'
inifile= cp.ConfigParser()

inifile.read(filepath,'UTF-8')

print(inifile.get('db','port'))

print(inifile['db']['port'])

print(inifile.items('web'))


#添加新的配置文件,或修改配置
inifile['web']['pwds']= '198.333.444'

with open(filepath,'w') as config:
    inifile.write(config)