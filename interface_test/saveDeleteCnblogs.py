#!/usr/bin/python
#coding:utf-8

''' ----- 绕过验证码通过cookie进行登录 ----- '''

import requests
import re
from bs4 import BeautifulSoup

# 禁止安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 登录博客
def loginCnblogs(s, loginUrl, headers, cnblogsCookie, cnblogsAspNetCoreCookies):
	
	# 先打开登录页面，获取部分cookie
	r = s.get(loginUrl, headers=headers, verify=False)

	# 添加登录需要的两个cookie
	c = requests.cookies.RequestsCookieJar()
	c.set('.CNBlogsCookie', cnblogsCookie)
	c.set('.Cnblogs.AspNetCore.Cookies', cnblogsAspNetCoreCookies)
	s.cookies.update(c)

# --------------- 登录全部走cookie登录 -------
# 保存随笔到草稿箱
def saveCnblogs(s, saveCnblogsUrl, headers, title, content):
	
	# 获取草稿箱所有随笔的title和postId
	allCnblogsArr = getAllCnblogsTitleAndPostId(s, boxCnblogsUrl, headers)
	
	# 判断需要保存随笔的title是否已经存在
	if title in allCnblogsArr:
		print '相同标题的内容已经存在。'
		return ''
	
	# 保存随笔
	body = {
		"__VIEWSTATE": "",
		"__VIEWSTATEGENERATOR":"FE27D343",
		"Editor$Edit$txbTitle":title,
		"Editor$Edit$EditorBody":"<p>"+content+"</p>",
		"Editor$Edit$Advanced$ckbPublished":"on",
		"Editor$Edit$Advanced$chkDisplayHomePage":"on",
		"Editor$Edit$Advanced$chkComments":"on",
		"Editor$Edit$Advanced$chkMainSyndication":"on",
		"Editor$Edit$Advanced$txbEntryName":"",
		"Editor$Edit$Advanced$txbExcerpt":"",
		"Editor$Edit$Advanced$tbEnryPassword":"",
		"Editor$Edit$lkbDraft":"存为草稿",
	}
	r2 = s.post(saveCnblogsUrl, data=body, verify=False)
	return r2.url
	
# 删除草稿箱中随笔
def deleteCnblogs(s, deleteCnblogsUrl, postId):	
	json3 = {'postId':postId}
	r = s.post(deleteCnblogsUrl, json=json3, verify=False)
	if r.json()['isSuccess']:
		print u'删除成功'
	else:
		print u'删除失败'
		
# 获取草稿箱中要删除随笔的postId
def getPostId(s, postIdUrl):
	
	# 正则提取需要的参数值
	postId = re.findall(r'postid=(.+?)&', postIdUrl)
	if len(postId)<1:
		return ''
	else:
		return postId[0]

# 打开草稿箱并获取所有随笔的title和postId
def getAllCnblogsTitleAndPostId(s, boxCnblogsUrl, headers):
	r = s.get(boxCnblogsUrl, headers=headers, verify=False)
	soup = BeautifulSoup(r.text, 'lxml')
	allA = soup.find_all(href=re.compile('^//www.cnblogs.com/SoftWindMan/p/'))
	allCnblogsArr = []
	for a in allA:
		allCnblogsArr.append(a.string)
		allCnblogsArr.append(a['id'].split('_')[3])
	return allCnblogsArr
	
	

if __name__ == '__main__':
	loginUrl = 'https://passport.cnblogs.com/user/signin'
	saveCnblogsUrl = 'https://i.cnblogs.com/EditPosts.aspx?opt=1'
	deleteCnblogsUrl = 'https://i.cnblogs.com/post/delete'
	boxCnblogsUrl = 'https://i.cnblogs.com/posts?postConfig=IsDraft'
	headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36'}

	cnblogsCookie = '3BB4E1DEEDC689191A51B440D54DA1C456CB3AA715D9034A344E032CC40E4C58C0424275D4D199B0185B6E465EE1C23962E48EFEEB9FF5D6818B672298A56FEB621E9FB4EA26EDA97062E6EA5A29F26C0AF9B85F0FA0DED65FD972BD376D52DB820215D8'
	cnblogsAspNetCoreCookies = 'CfDJ8FHXRRtkJWRFtU30nh_M9mA44AJTnrLbMFSlb0ZSMab2t_bDedF9ftIMZ-yj0c-oDvFk7lQPGZ95qeZgx2QTtW5pmL9EUYmuw7eAgjyjrrSHw7xl_P3qtBgI7unPLQBRXJQTye1gTmhDw0UhnzKDhKtk_Eh6qWo8ChtZJj2pk7SxDz0T_IvhHk6-rqTNHaIkxEbCC4J_XJMGRuBBGx50PcBWxFhylAr4CFknLb616CltI26X4oanydq0vd75eCCbMRPQcA1mkeXn-hCzBk9lBJdk2x7yKapCGQAnOoMnn9jH'

	title = 'title13'
	content = 'content10'

	s = requests.session()
	loginCnblogs(s, loginUrl, headers, cnblogsCookie, cnblogsAspNetCoreCookies)
	postIdUrl = saveCnblogs(s, saveCnblogsUrl, headers, title, content)
	if postIdUrl:
		postId = getPostId(s, postIdUrl)
		print u'获取postId成功：' + postId
	else:
		print '获取postId失败。'
#	deleteCnblogs(s, deleteCnblogsUrl, postId)






