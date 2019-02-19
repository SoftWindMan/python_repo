#coding=utf-8
from novelList import *

class UserOperate:
    def __init__(self):
        self._novelIndex = NovelList()

    # 选择小说分类
    def choice_novel_type(self, novelTypeIndex):
        novelTypeIndex = int(novelTypeIndex)
        allNovelTypeName = self._novelIndex.all_novel_type_info()
        return allNovelTypeName[novelTypeIndex]['novelTypeName'], int(allNovelTypeName[novelTypeIndex]['pages'])

    # 选择某分类某小说
    def choice_novel(self, novelTypeName, pageIndex, novelIndex):
        novelIndex = int(novelIndex)
        pageNovelInfo = self._novelIndex.one_page_all_novel_under_novel_type_name(novelTypeName, pageIndex)
        return pageNovelInfo[novelIndex]['novelName'], pageNovelInfo[novelIndex]['novelUrl']




