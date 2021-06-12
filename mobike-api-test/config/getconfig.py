import configparser

config = configparser.ConfigParser()

#---------------------------查找文件内容,基于字典的形式



config.read('example.ini')

print(config.sections())        #   ['bitbucket.org', 'topsecret.server.com']

print('bytebong.com' in config) # False
print('bitbucket.org' in config) # True
#
#

tt= config['bitbucket.org']["nihao"]


gg=  eval(tt)
print( eval(tt))


print(config['bitbucket.org']["nihao"])  # Atlan



#
# print(config['DEFAULT']['Compression']) #yes
#
# print(config['topsecret.server.com']['ForwardX11'])  #no
#
#
# print(config['bitbucket.org'])          #<Section: bitbucket.org>
#
# for key in config['bitbucket.org']:     # 注意,有default会默认default的键
#     print(key)

# print(config.options('bitbucket.org'))  # 同for循环,找到'bitbucket.org'下所有键
#
# print(config.items('bitbucket.org'))    #找到'bitbucket.org'下所有键值对
#
# print(config.get('bitbucket.org','compression')) # yes       get方法Section下的key对应的value