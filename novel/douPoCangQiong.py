#!/usr/bin/python
#coding=utf-8

# 斗破苍穹

import requests, sys, os
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

pageNumRequestUrl = 'https://m.doupocangqiong1.com/1/list/'
chapterListRequestUrl = 'https://m.doupocangqiong1.com/1/list/?sort=asc&page='
chapterInfoRequestUrl = 'https://m.doupocangqiong1.com'

# 获取分页数
def getPages(pageNumRequestUrl):
	html_res = requests.get(pageNumRequestUrl).text
	soup = BeautifulSoup(html_res, 'lxml')

	#print soup.prettify()
	
	pageNumArr = []
	for k in soup.find_all('a'):		
		if k.has_attr('href'):
			if '/1/list/' in k['href']:
				if '-' in k.text:
#					print k.text
					pageNumArr.append(k.text)
	
	pageNumArrLen = len(pageNumArr)
	pageNumArrLast = pageNumArr[pageNumArrLen - 1]
	lastChatpterNum = int(pageNumArrLast.split('-')[1].replace(u'章', ''))
	
	pageNum = lastChatpterNum / 50
	if lastChatpterNum % 50 != 0:
		pageNum +=1
	
	return pageNum
	
# 获取章节列表信息
def getChapterList(chapterListRequestUrl, pageNum):
	chapterListArr = []
	for i in range(1, pageNum + 1):
		chapterListUrl = chapterListRequestUrl + str(i)
#		print chapterListUrl
		
		html_res = requests.get(chapterListUrl).text
		soup = BeautifulSoup(html_res, 'lxml')
		
		for k in soup.find_all('a'):
			if k.has_attr('title'):
				if u'第' in k['title']:
#					print k['title']
					chapterListArr.append(chapterInfoRequestUrl + k['href'])
	return chapterListArr
	
# 获取每章节内容
def getChapterContent(chapterListArr):
	count = 1
	
	for chapterUrl in chapterListArr:
		html_res = requests.get(chapterUrl).text
		soup = BeautifulSoup(html_res, 'lxml')
		
		chapterTitle = soup.find_all('h1')[0].text
		chapterTitleSplitArr = chapterTitle.split(' ')
		if len(chapterTitleSplitArr) > 1:
			chapterTitle = '第' + str(count) + '章 ' + chapterTitle.split(' ')[1]
			
			chapterContentArr = []
			for content in soup.find_all('p'):
				chapterContentArr.append(content.text)
				
			if os.path.exists(chapterTitle):
				print chapterTitle + ' Downloading...'
				saveChapterContentToLocal(chapterTitle, chapterContentArr)
			else:
				print chapterTitle + ' exists'
			
		count += 1

	print 'Done!!!'
			
# 将章节内容写入文件保存到本地
def saveChapterContentToLocal(title, contentArr):
#	print title
#	print contentArr

	filename = title + '.txt'
	filehandle = open(filename, 'w')
	filehandle.write(title)
	filehandle.write('\n')
	
	for line in contentArr:
		filehandle.write(line)
		filehandle.write('\n')

	filehandle.close()
		
pageNum = getPages(pageNumRequestUrl)	
#print pageNum

chapterListArr = getChapterList(chapterListRequestUrl, pageNum)
#print chapterListArr

chapterContentDict = getChapterContent(chapterListArr)
#print chapterContentDict