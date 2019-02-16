#coding=utf-8
import requests
import os
from requests import RequestException
from pyquery import PyQuery as pq

class NovelParse:
    """函数作用：获取响应内容
       参数：novelName - 小说名称，也是保存章节文件的文件夹名称
            responseEncoding - 响应编码格式
            isCover - 是否覆盖下载
    """
    def __init__(self, novelName, responseEncoding, isCover=False):
        self.novelName = novelName
        self.responseEncoding = responseEncoding
        self.isCover = isCover

    """ 函数作用：获取响应内容
        参数：url - 请求地址 
    """
    def parse_url(self, url):
        try:
            response = requests.get(url)
            response.encoding = self.responseEncoding
        except RequestException as e:
            print('Request error - {}'.format(e))
        else:
            return response.text if response.status_code == 200 else None

    """ 函数作用：获取响应中某标签的内容
        参数：response - 响应
             tagStr - 特定标签 
    """
    def get_tagtext(self, response, tagStr):
        specialTag = self.__get_specialtag(response, tagStr)
        return [(tag.text().encode('utf-8') if isinstance(tag.text(), unicode) else tag.text()) for tag in specialTag]

    """ 函数作用：获取响应中某标签的某属性的内容
        参数：response - 响应
             tagStr - 特定标签
             attrStr - 特定属性
    """
    def get_attrtext(self, response, tagStr, attrStr):
        specialTag = self.__get_specialtag(response, tagStr)
        return [(tag.attr(attrStr).encode('utf-8') if isinstance(tag.attr(attrStr), unicode) else tag.attr(attrStr)) for tag in specialTag]

    """ 函数作用：将小说章节内容写入文件
        参数：filePath - 保存章节文件的路径
             content - 章节内容
    """
    def write_to_file(self, chapterTitle, chapterContent):
        filePath = os.path.join(os.getcwd(), self.novelName, chapterTitle)
        with open(filePath, 'w') as fp:
            fp.write(chapterTitle.split('.')[0])
            fp.write('\n')
            fp.write(chapterContent)

    """ 创建小说文件夹 """
    def create_noveldir(self):
        novelPath = os.path.join(os.getcwd(), self.novelName)
        if not os.path.exists(novelPath):
            os.mkdir(novelPath)

    """ 判断本章节小说是否存在 """
    def is_exists_file(self, chapterTitle):
        if self.isCover: return False
        filePath = os.path.join(os.getcwd(), self.novelName, chapterTitle)
        return True if os.path.exists(filePath) else False

    """ 获取响应中某标签的结点 """
    def __get_specialtag(self, response, tagStr):
        doc = pq(response)
        specialTag = doc(tagStr).items()
        return specialTag


