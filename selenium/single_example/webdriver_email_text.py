#!/usr/bin/python
#coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '13240359614@163.com'
receiver = '184994562@qq.com'
smtpserver = 'smtp.163.com'

username = '13240359614@163.com'
password = 'fengyuleidian95'

subject = 'python email test.'

msg = MIMEText('你好！', 'text', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = Header(sender)
msg['To'] = Header(receiver)

smtp = smtplib.SMTP(smtpserver, 25)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
