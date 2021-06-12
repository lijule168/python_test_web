#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'YinJia'

import os,sys
from email.header import Header

from email.mime.text import MIMEText


import smtplib

from email.mime.image import MIMEImage

# 创建邮件对象
from email.mime.multipart import MIMEMultipart


def send_mail():
    """
    定义发送邮件
    :param file_new:
    :return: 成功：打印发送邮箱成功；失败：返回失败信息
    """
    # 连接邮箱服务器 SMTP.163.COM
    #端口号 465/25
    #创建连接
    com=smtplib.SMTP_SSL('smtp.163.com',465)
    #登录连接
    com.login('lijule168@163.com','li16888')

    #准备数据
    msg= MIMEMultipart()

    # 设置邮件主题
    subject = Header('重要信息麻烦给予确认','utf-8').encode()
    msg['Subject']=subject

    #设置邮件发送人
    msg['From']='lijule168@163.com<lijule168@163.com>'

    # 设置邮件接收人 '收件人1;收件人2'
    msg['To'] = '1176923313@qq.com'

    # 构建文本内容 MIMEText(文字内容,文本类型,编码方式)
    #文本类型 -plain (普通文字) , html (超链接), base64(二进制文件)
    # text=MIMEText('smtplib 发送邮件','plain','utf-8')

    # --------------构建HTML 文本----------
    comtent='''
    <img src='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'>
    <h1>我是正文大标题 </h1>
    <h2>我是副标题</h2>
    <p> 我是邮件正文</p>
    <a href= 'https://www.baidu.com'>点击跳转</a>
    
    
    '''
    html=MIMEText(comtent,'html','utf-8')
    msg.attach(html)
    #获取图片对象,创建图片对象
    image1_datal=open('files/image.jpg','rb').read()
    image1=MIMEImage(image1_datal)
    #设置附件名
    image1['Content-Disposition']= 'attachment; filename="friend.jpg"'

    msg.attach(image1)

    #发送邮件
    #连接对象.sendmail(发件人,收件人,字符串类型的邮件对象)
    com.sendmail('lijule168@163.com','1176923313@qq.com',msg.as_string())
    #退出
    com.quit()




send_mail()

