#coding=utf-8
from parseHtml import *
from concurrent.futures import ThreadPoolExecutor

""" 小说列表类 """
class NovelList:
    def __init__(self):
        self._baseUrl = 'https://www.x88dushu.com'
        self._parseHtml = ParseHtml()

        self._executor = ThreadPoolExecutor(max_workers=1000)

    # 所有小说分类信息
    def all_novel_type_info(self):
        response = self._parseHtml.parse_url(self._baseUrl)
        allNovelTypeName = self._parseHtml.tagtext_from_html(response, '.nav_l li')
        allNovelTypeUrl = self._parseHtml.attrtext_from_html(response, '.nav_l li a', 'href')

        allNovelTypeInfo = []
        for i in range(1, len(allNovelTypeName)):
            baseResponse = self._parseHtml.parse_url(self._baseUrl + allNovelTypeUrl[i])
            pages = self._parseHtml.attrtext_from_html(baseResponse, '.pagelink a', 'href')[-1].split('/')[-2]

            allNovelTypeDict = {}
            allNovelTypeDict['novelTypeUrl'] = self._baseUrl + '/' + allNovelTypeUrl[i].split('/')[1] + '/'
            allNovelTypeDict['novelTypeName'] = allNovelTypeName[i]
            allNovelTypeDict['pages'] = pages
            allNovelTypeInfo.append(allNovelTypeDict)
        return allNovelTypeInfo

    # 获取某类型小说某页的小说信息
    def one_page_all_novel_under_novel_type_name(self, novelTypeName, pageIndex):
        allNovelTypeInfo = self.all_novel_type_info()
        for novelTypeInfo in allNovelTypeInfo:
            if novelTypeInfo['novelTypeName'] == novelTypeName:
                pageUrl = novelTypeInfo['novelTypeUrl'] + str(pageIndex)
                response = self._parseHtml.parse_url(pageUrl)
                novelName = self._parseHtml.tagtext_from_html(response, '.booklist .sm')[1:]
                novelAuthor = self._parseHtml.tagtext_from_html(response, '.booklist .zz')[1:]
                novelUrl = self._parseHtml.attrtext_from_html(response, '.booklist .sm a', 'href')

                novelInfo = []
                for i in range(len(novelName)):
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
                    novelName = self._parseHtml.tagtext_from_html(response, '.booklist .sm')[1:]
                    novelAuthor = self._parseHtml.tagtext_from_html(response, '.booklist .zz')[1:]
                    novelUrl = self._parseHtml.attrtext_from_html(response, '.booklist .sm a', 'href')
                    for i in range(len(novelName)):
                        novelInfoDict = {}
                        novelInfoDict['novelName'] = novelName[i]
                        novelInfoDict['novelAuthor'] = novelAuthor[i]
                        novelInfoDict['novelUrl'] = self._baseUrl + novelUrl[i]
                        novelInfo.append(novelInfoDict)
                return novelInfo

if __name__ == '__main__':
    novelList = NovelList()
    a = novelList.one_page_all_novel_under_novel_type_name('玄幻魔法', 1)
    # a = novelList.all_novel_type_info()
    print(len(a))
    print(a)
