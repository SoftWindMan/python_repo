#!/usr/bin/python
#coding=utf-8

import os, sys, time

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

reload(sys)  
sys.setdefaultencoding('utf8') 

resultDir = os.path.join(os.getcwd(), 'report')
lists = os.listdir(resultDir)
lists.sort(key=lambda fn: os.path.getmtime(resultDir + '\\' + fn) if not os.path.isdir(resultDir + '\\' + fn) else 0)
fileName = os.path.join(resultDir, lists[-1])

f = open(fileName, 'rb')
mailBody = f.read()
f.close()

sender = '13240359614@163.com'
receiver = '184994562@qq.com'
smtpserver = 'smtp.163.com'

username = '13240359614@163.com'
password = 'fengyuleidian95'

# 和text方式发送的区别是在邮件列表中也能看到文件内容
msg = MIMEText(mailBody, _subtype='html', _charset='utf-8')
msg['Subject'] = Header('python测试报告', 'utf-8')
msg['date'] = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
msg['From'] = Header(sender)
msg['To'] = Header(receiver)

smtp = smtplib.SMTP(smtpserver, 25)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
