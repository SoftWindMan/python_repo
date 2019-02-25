#coding=utf-8
from parseHtml import *

# 模型类
class NovelModel:
    def __init__(self):
        self._baseUrl = 'https://www.x88dushu.com'
        self._parseHtml = ParseHtml()

    # 所有小说类型
    def all_novel_type_names(self):
        allNovelTypeNames = self._all_novel_types()
        newAllNovelTypeNames = []
        for i in range(len(allNovelTypeNames)):
            novelTypeName = allNovelTypeNames[i]['novelTypeName']
            novelTypePages = allNovelTypeNames[i]['novelTypePages']
            newAllNovelTypeNames.append('【{}】 {} - 共{}页'.format(i, novelTypeName, novelTypePages))
        return newAllNovelTypeNames

    # 某类某页
    def single_novels(self, novelTypeNameIndex, pageIndex):
        novelTypeName = self._all_novel_types()[novelTypeNameIndex]['novelTypeName']
        novelTypePages = self._all_novel_types()[novelTypeNameIndex]['novelTypePages']
        singleNovels = self._single_novels_under_novel_type_name(novelTypeName, pageIndex)
        newSingleNovels = []
        for singleNovel in singleNovels:
            newsingleNovelDict = {}
            newsingleNovelDict['novelName'] = singleNovel['novelName']
            newsingleNovelDict['novelAuthor'] = singleNovel['novelAuthor']
            newSingleNovels.append(newsingleNovelDict)
        newSingleNovels.append(novelTypeName)
        newSingleNovels.append(novelTypePages)
        newSingleNovels.append(pageIndex)
        return newSingleNovels

    # 某类某页某小说
    def one_novel(self, novelTypeNameIndex, pageIndex, novelIndex):
        novelTypeName = self._all_novel_types()[novelTypeNameIndex]['novelTypeName']
        singleNovels = self._single_novels_under_novel_type_name(novelTypeName, pageIndex)
        return singleNovels[novelIndex]['novelName'], singleNovels[novelIndex]['novelUrl']

    # 根据小说名查找小说
    def all_novels_by_find(self, novelNameStr):
        pass

    # 所有小说分类信息
    def _all_novel_types(self):
        response = self._parseHtml.parse_url(self._baseUrl)
        allNovelTypeName = self._parseHtml.tagtext_from_html(response, '.nav_l li')
        allNovelTypeUrl = self._parseHtml.attrtext_from_html(response, '.nav_l li a', 'href')

        allNovelTypeInfo = []
        for i in range(1, len(allNovelTypeName)):
            baseUrl = self._baseUrl + allNovelTypeUrl[i]
            baseResponse = self._parseHtml.parse_url(baseUrl)
            pages = self._parseHtml.attrtext_from_html(baseResponse, '.pagelink a', 'href')[-1].split('/')[-2]

            allNovelTypeDict = {}
            allNovelTypeDict['novelTypeUrl'] = self._baseUrl + '/' + allNovelTypeUrl[i].split('/')[1] + '/'
            allNovelTypeDict['novelTypeName'] = allNovelTypeName[i]
            allNovelTypeDict['novelTypePages'] = pages
            allNovelTypeInfo.append(allNovelTypeDict)
        return allNovelTypeInfo

    # 某类某页的所有小说信息
    def _single_novels_under_novel_type_name(self, novelTypeName, pageIndex):
        allNovelTypeInfo = self._all_novel_types()
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
    def all_novels_under_novel_type_name(self, novelTypeName):
        allNovelTypeInfo = self._all_novel_types()
        for novelTypeInfo in allNovelTypeInfo:
            if novelTypeInfo['novelTypeName'] == novelTypeName:
                novelTypePages = int(novelTypeInfo['novelTypePages'])
                novelTypeUrl = novelTypeInfo['novelTypeUrl']

                novelInfo = []
                for i in range(1, novelTypePages + 1):
                    pageUrl = novelTypeUrl + str(i)
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
    novelModel = NovelModel()
    a = novelModel.all_novel_type_names()
    # b = novelModel.all_novels_under_novel_type_name('玄幻魔法')

    for per in a:
        print(per)
