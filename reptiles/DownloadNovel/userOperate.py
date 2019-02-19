#coding=utf-8
from keepAccount.test.novelIndex import *
import sys

class UserOperate:
    def __init__(self):
        self._novelIndex = NovelIndex()

    def choice_novel_type(self, novelTypeIndex):
        novelTypeIndex = int(novelTypeIndex)
        allNovelTypeName = self._novelIndex.all_novel_type_info()
        return allNovelTypeName[novelTypeIndex]['novelTypeName'], int(allNovelTypeName[novelTypeIndex]['pages'])

    def choice_novel(self, novelTypeName, pageIndex, novelIndex):
        novelIndex = int(novelIndex)
        pageNovelInfo = self._novelIndex.one_page_all_novel_under_novel_type_name(novelTypeName, pageIndex)
        return pageNovelInfo[novelIndex]['novelName'], pageNovelInfo[novelIndex]['novelUrl']




