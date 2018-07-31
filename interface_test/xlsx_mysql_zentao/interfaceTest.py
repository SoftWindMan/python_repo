#!/usr/bin/python
#coding=utf-8

import requests, xlrd, MySQLdb, time, sys
from xlutils import copy

# 读取用例excel中的case并存入数组，然后调用接口方法执行case
def readExcel(file_path):
	try:
		excelFile = xlrd.open_workbook(file_path)
	except Exception, e:
		print '路径不在或者excel不正确。', e
		return e
	else:
		sheet = excelFile.sheet_by_index(0)
		rows = sheet.nrows
		caseList = []
		for i in range(rows):
			if i!=0:
				caseList.append(sheet.row_values(i))
		return caseList

# 执行case并生成测试结果Excel（失败的case提bug）
def interfaceTest(caseList, file_path):
	resultFlags = []
	requestUrls = []
	responses = []
	for case in caseList:
		try:
			product = case[0]
			caseId = case[1]
			interfaceName = case[2]
			caseDetail = case[3]
			method = case[4]
			url = case[5]
			param = case[6]
			resultCheck = case[7]
			tester = case[10]
		except Exception, e:
			return '测试用例格式不正确！%s' %e
		
		if param == '':
			requestUrl = url
		else:
			requestUrl = url + '?' + urlParam(param)
		requestUrls.append(requestUrl)
		print requestUrl
		
		headers = {
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'zh-CN,zh;q=0.9',
			'Connection': 'close', 
			'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36'
		}			
		
		if method.upper() == 'GET':
			response = requests.get(requestUrl, headers=headers).text
		else:
			response = requests.post(requestUrl, headers=headers).text
		responses.append(response)
		res = readResult(response, resultCheck)
		print res
	
		if 'pass' in res:
			resultFlags.append('pass')
		else:
			resultFlags.append('fail')
			
			# 对失败的case提bug
			writeBug(caseId, interfaceName, requestUrl, response, resultCheck)
	
	# 生成测试结果Excel
	copyExcel(file_path, resultFlags, requestUrls, responses)

# 生成测试结果Excel
def copyExcel(file_path, resultFlags, requestUrls, responses):
	excelFile = xlrd.open_workbook(file_path)
	new_book = copy.copy(excelFile)
	sheet = new_book.get_sheet(0)
	i = 1
	for requestUrl, response, flag in zip(requestUrls, responses, resultFlags):
		sheet.write(i, 8, u'%s'%requestUrl)
		sheet.write(i, 9, u'%s'%response)
		sheet.write(i, 11, u'%s'%flag)
		i += 1
	new_book.save('%s_测试结果.xls'%time.strftime('%Y%m%d%H%M%S'))
	
# 将报错的case写入禅道bug
def writeBug(caseId, interfaceName, requestUrl, response, resultCheck):
	
	# 拼接sql。如果执行sql报错是可以sql看一下
	caseId = caseId.encode('utf-8')
	interfaceName = interfaceName.encode('utf-8')
	resultCheck = resultCheck.encode('utf-8')
	response = response.encode('utf-8')
	requestUrl = requestUrl.encode('utf-8')
	bugTitle = caseId + "_" + interfaceName + "_结果和预期不符"
	steps = "<p>[请求报文]</p>\n<p>" + requestUrl + "</p>\n<p>[响应报文]</p>\n<p>" + response + "</p>\n<p>[期望结果]</p>\n<p>" + resultCheck + "</p>"
	sql = "INSERT INTO `zt_bug` (`product`, `branch`, `module`, `project`, `plan`, `story`, `storyVersion`, `task`, `toTask`, `toStory`, `title`, `keywords`, `severity`, `pri`, `type`, `os`, `browser`, `hardware`, `found`, `steps`, `status`, `color`, `confirmed`, `activatedCount`, `activatedDate`, `mailto`, `openedBy`, `openedDate`, `openedBuild`, `assignedTo`, `assignedDate`, `deadline`, `resolvedBy`, `resolution`, `resolvedBuild`, `resolvedDate`, `closedBy`, `closedDate`, `duplicateBug`, `linkBug`, `case`, `caseVersion`, `result`, `testtask`, `lastEditedBy`, `lastEditedDate`, `deleted`) VALUES (1, 0, 4, 0, 0, 0, 1, 0, 0, 0, '%s', '', 3, 3, 'codeerror', '', '', '', '', '%s', 'active', '', 0, 0, NOW(), '', 'csz', NOW(), 'trunk', 'csz', NOW(), NOW(), '', '', '', NOW(), '', NOW(), 0, '', 0, 0, 0, 0, '', NOW(), '0')" % (bugTitle, steps)
	
	# 连接数据库并执行sql语句
	conn = MySQLdb.connect(user='root', passwd='123', db='zentao', port=3306, host='127.0.0.1', charset='utf8')
	cursor = conn.cursor()
	cursor.execute(sql)
	conn.commit()
	conn.close()
	
# 对response进行断言
def readResult(result, resultsCheck):
	result = result.replace('":"', "=").replace('":', "=")
	resultsCheck = resultsCheck.split(';')
	for s in resultsCheck:
		if s in result:
			pass
		else:
			return '错误，返回参数和预测结果不一样' + str(s)
	return 'pass'

# 拼接参数
def urlParam(param):
	return param.replace(';', '&')
	
if __name__ == '__main__':
	file_path = './interfaceTestExcel.xlsx'
	caseList = readExcel(file_path)
	interfaceTest(caseList, file_path)
