#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

from lib.util.log_util import l
from lib.entity.run_config import EmailConfig
from lib.util.time_util import TimeUtil

def send_email(content, receiver_emails=None, title=""):
    if receiver_emails is None:
        receiver_emails = ["qa@mobike.com", "dingbaixia@mobike.com"]
    my_sender = EmailConfig.sender# 'pengdingguo@mobike.com'
    mail_pass = EmailConfig.passwd
    my_user = receiver_emails#['dingbaixia@mobike.com']

    mail_host = EmailConfig.server# 'smtp.partner.outlook.cn'
    cur_time = TimeUtil.format_timer_to_str(format_date='%Y-%m-%d %H:%M:%S')# time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    sub = cur_time + "      " + title
    msg = MIMEText(content, _subtype="html", _charset="utf-8")
    try:
        attatch = MIMEMultipart()
        attatch['Subject'] = sub
        attatch['From'] = formataddr(["", my_sender])
        attatch['To'] = ','.join(my_user)
        attatch.attach(msg)
        log_name = "api_auto_test_debug.log"
        with open(log_name, 'rb') as attachment:
            attachment = MIMEText(attachment.read(), _subtype="octet-stream", _charset="gb2312")
            attachment.add_header('content-disposition', 'attachment', filename=log_name)
            attatch.attach(attachment)
        #attr = MIMEText()
        server = smtplib.SMTP(mail_host, EmailConfig.port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.set_debuglevel(0)
        server.login(my_sender, mail_pass)
        server.sendmail(my_sender, my_user, attatch.as_string())
        server.quit()
        l.info("send email successfully")
        return True
    except Exception as e:
        l.error("send email failed, exception: {0}".format(e))

