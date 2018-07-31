#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

host = "http://127.0.0.1"

def login(s, username, psw):
	url = host + "/zentaopms/www/index.php?m=user&f=login"
	h = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
		"Accept-Encoding": "gzip, deflate, br",
		"Accept-Language": "zh-CN,zh;q=0.9",
		#Cookie: lang=zh-cn; device=desktop; theme=default; windowWidth=400; windowHeight=136; zentaosid=pd1jea89s9h7rso6pl9dtkgd1a
		"Proxy-Connection": "keep-alive",
		"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36",
		"Referer": host + "/zentaopms/www/index.php?m=my&f=index"
	}
	
	body1 = {
		"username":username,
		"password":psw,
		"keepLogin[]":"on",
		"referer":host + "/zentaopms/www/index.php?m=my&f=index"
	}
	
	r1 = requests.post(url, data=body1, headers=h)
	return r1.content.decode("utf-8")
	
def is_login_sucess(res):
	if u'登录失败，请检查您的用户名或密码是否填写正确' in res:
		return False
	elif "parent.location=" in res:
		return True
	else:
		return False
		
if __name__ == "__main__":
	s = requests.session()
	a = login(s, "csz", "abe092b5224533f0f6e3754689b05ac1")
	print a
	result = is_login_sucess(a)
	print("测试结果：%s" %result)