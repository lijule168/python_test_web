import requests

#�������ݵ�׼��

url=www.baidu.com

data = {
    'username':'admin',
    'password':'123456'

}

#ģ��������·�
res=requests.post(url=url,json=data)
#������Ӧ����жϱ��ε������Ƿ�ɹ�

print(res.text)