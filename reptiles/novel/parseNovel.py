#coding=utf-8
import requests
import os
from requests import RequestException
from pyquery import PyQuery as pq
from concurrent.futures import ThreadPoolExecutor, wait

class ParseNovel:
    def __init__(self, novelName):
        self._saveDir = os.path.join(os.getcwd(), novelName)
        self._executor = ThreadPoolExecutor(max_workers=100)
        self.responseEncoding = 'gbk'

    """ 函数作用：解析url获取响应
        参数：urls - 请求地址(单个str或者多个str组成的list)
    """
    def parse_url(self, urls):
        if isinstance(urls, str):
            urls = [urls, ]
        if not isinstance(urls, list):
            print('url类型必须时str或者list。')

        futureArr = []
        for url in urls:
            try:
                future = self._executor.submit(requests.get, url)
                futureArr.append(future)
            except RequestException as e:
                print('Request error - {}'.format(e))
        wait(futureArr)

        responseArr = []
        for future in futureArr:
            res = future.result()
            res.encoding = self.responseEncoding
            response = res.text if res.status_code == requests.codes.ok else None
            responseArr.append(response)
        return responseArr

    """ 函数作用：获取响应中某标签的某属性的内容
        参数：response - 响应
             tagStr - 特定标签
             attrStr - 特定属性
    """
    def get_tagtext(self, response, tagStr):
        doc = pq(response)
        specialTag = doc(tagStr).items()
        return [(tag.text().encode('utf-8') if isinstance(tag.text(), unicode) else tag.text()) for tag in specialTag]

    """ 函数作用：获取响应中某标签的某属性的内容
        参数：response - 响应
             tagStr - 特定标签
             attrStr - 特定属性
    """
    def get_attrtext(self, response, tagStr, attrStr):
        doc = pq(response)
        specialTag = doc(tagStr).items()
        return [(tag.attr(attrStr).encode('utf-8') if isinstance(tag.attr(attrStr), unicode) else tag.attr(attrStr)) for tag in specialTag]

    """ 将小说写入文件 """
    def write_to_file(self, titles, contents, isCover=False):
        if not os.path.exists(self._saveDir):
            os.mkdir(self._saveDir)

        for i in range(len(titles)):
            filePath = os.path.join(self._saveDir, titles[i])
            isWrite = True if os.path.exists(filePath) else False
            if not isWrite:
                with open(filePath, 'w') as fp:
                    fp.write(titles[i] + '\n')
                    fp.write(contents[i])
                print('{} - 下载完成。'.format(titles[i]))



