#!/usr/bin/python
#coding=utf-8

import unittest, sys, time, os
import HTMLTestRunner
import allCaseList
from testCase import baidu, youdao

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

reload(sys)  
sys.setdefaultencoding('utf8') 

sys.path.append('\testCase')

def sendReport():
	resultDir = os.path.join(os.getcwd(), 'report')
	lists = os.listdir(resultDir)
	lists.sort(key=lambda fn: os.path.getmtime(resultDir + '\\' + fn) if not os.path.isdir(resultDir + '\\' + fn) else 0)
	fileName = os.path.join(resultDir, lists[-2])
	sendMail(fileName)

def sendMail(fileName):
	f = open(fileName, 'rb')
	mailBody = f.read()
	f.close()
	
	sender = '13240359614@163.com'
	receiver = '184994562@qq.com'
	smtpserver = 'smtp.163.com'

	username = '13240359614@163.com'
	password = 'fengyuleidian95'

	# 和text方式发送的区别是在邮件列表中也能看到文件内容
	msg = MIMEText(mailBody, 'html', 'utf-8')
	msg['Subject'] = Header('python测试报告', 'utf-8')
	msg['date'] = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
	msg['From'] = Header(sender)
	msg['To'] = Header(receiver)

	smtp = smtplib.SMTP(smtpserver, 25)
	smtp.login(username, password)
	smtp.sendmail(sender, receiver, msg.as_string())
	smtp.quit()
	
if __name__ == '__main__':
	suite = unittest.TestSuite()

	for case in allCaseList.caseList():
		suite.addTest(unittest.makeSuite(case))

	nowTime = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
	filePath = os.path.join(os.getcwd(), 'report', nowTime + 'result.html')
	f = open(filePath, 'wb')
	runner = HTMLTestRunner.HTMLTestRunner(stream = f, title = '百度搜索测试报告', description = '用例执行情况：')
	runner.run(suite)
	sendReport()
	
	