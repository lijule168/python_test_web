import requests

#请求数据的准备

url=www.baidu.com

data = {
    'username':'admin',
    'password':'123456'

}

#模拟请求的下发
res=requests.post(url=url,json=data)
#解析响应结果判断本次的请求是否成功

print(res.text)