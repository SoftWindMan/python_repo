#coding=utf-8
from keepAccount.test.parseHtml import *
from concurrent.futures import ThreadPoolExecutor
import os

class NovelIndex:
    def __init__(self):
        self._baseUrl = 'https://www.x88dushu.com'
        self._parseHtml = ParseHtml()

        self._executor = ThreadPoolExecutor(max_workers=100)

    # 所有小说分类信息
    def all_novel_type_info(self):
        response = self._parseHtml.parse_url(self._baseUrl)
        allNovelTypeName = self._parseHtml.tagtext_from_html(response, '.nav_l li')
        allNovelTypeUrl = self._parseHtml.attrtext_from_html(response, '.nav_l li a', 'href')

        allNovelTypeInfo = []
        for i in range(1, len(allNovelTypeName)):
            allNovelTypeDict = {}
            allNovelTypeDict['novelTypeUrl'] = self._baseUrl + allNovelTypeUrl[i]
            allNovelTypeDict['novelTypeName'] = allNovelTypeName[i]

            baseResponse = self._parseHtml.parse_url(self._baseUrl + allNovelTypeUrl[i])
            pages = self._parseHtml.attrtext_from_html(baseResponse, '.pagelink a', 'href')[-1].split('/')[-2]
            allNovelTypeDict['pages'] = pages
            allNovelTypeInfo.append(allNovelTypeDict)
        return allNovelTypeInfo

    # 获取某类型小说某页的小说信息
    def one_page_all_novel_under_novel_type_name(self, novelTypeName, pageIndex):
        allNovelTypeInfo = self.all_novel_type_info()
        for novelTypeInfo in allNovelTypeInfo:
            if novelTypeInfo['novelTypeName'] == novelTypeName:
                novelTypeUrl = novelTypeInfo['novelTypeUrl']
                pageUrl = self._baseUrl + '/' + novelTypeUrl.split('/')[-3] + '/' + str(pageIndex)
                response = self._parseHtml.parse_url(pageUrl)
                novelName = self._parseHtml.tagtext_from_html(response, '.booklist .sm')
                novelAuthor = self._parseHtml.tagtext_from_html(response, '.booklist .zz')
                novelUrl = self._parseHtml.attrtext_from_html(response, '.booklist a', 'href')
                novelInfo = []
                for i in range(1, len(novelName)):
                    novelInfoDict = {}
                    novelInfoDict['novelName'] = novelName[i]
                    novelInfoDict['novelAuthor'] = novelAuthor[i]
                    novelInfoDict['novelUrl'] = self._baseUrl + novelUrl[i]
                    novelInfo.append(novelInfoDict)
                return novelInfo

    # 获取某小说分类下所有小说信息
    def all_novel_under_novel_type_name(self, novelTypeName):
        allNovelTypeInfo = self.all_novel_type_info()
        for novelTypeInfo in allNovelTypeInfo:
            if novelTypeInfo['novelTypeName'] == novelTypeName:
                pages = int(novelTypeInfo['pages'])
                novelTypeUrl = novelTypeInfo['novelTypeUrl']

                novelInfo = []
                for i in range(1, pages + 1):
                    pageUrl = self._baseUrl + novelTypeUrl.split('/')[-3] + '/' + str(i)
                    response = self._parseHtml.parse_url(pageUrl)
                    novelName = self._parseHtml.tagtext_from_html(response, '.booklist .sm')
                    novelAuthor = self._parseHtml.tagtext_from_html(response, '.booklist .zz')
                    novelUrl = self._parseHtml.attrtext_from_html(response, '.booklist a', 'href')
                    for i in range(1, len(novelName)):
                        novelInfoDict = {}
                        novelInfoDict['novelName'] = novelName[i]
                        novelInfoDict['novelAuthor'] = novelAuthor[i]
                        novelInfoDict['novelUrl'] = self._baseUrl + novelUrl[i]
                        novelInfo.append(novelInfoDict)
                return novelInfo

if __name__ == '__main__':
    novelIndex = NovelIndex()
    a = novelIndex.one_page_all_novel_under_novel_type_name('恐怖悬疑', 1)
    print(a)