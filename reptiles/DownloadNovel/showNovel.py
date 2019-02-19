#coding=utf-8
from novelList import *
from prettytable import PrettyTable

class ShowNovel:
    def __init__(self):
        self._novelIndex = NovelList()

    # 显示小说类型列表
    def show_novel_type(self):
        allNovelTypeName = self._novelIndex.all_novel_type_info()
        print('*************************')
        print('***     所有小说分类    ***')
        print('*************************')
        count = len(allNovelTypeName)
        for i in range(count):
            print('【{}】 {} - 共{}页'.format(i, allNovelTypeName[i]['novelTypeName'], allNovelTypeName[i]['pages']))
        print('【q | Q】 退出')

    # 显示某类型小说下某页的小说
    def show_all_novel_under_novel_type_name(self, novelTypeName, index, pages):
        allNovelInfo = self._novelIndex.one_page_all_novel_under_novel_type_name(novelTypeName, index)
        novelTable = PrettyTable(['编号', '小说名', '作者'])
        # novelTable.align['id'] = 'l'
        # novelTable.padding_width = 1
        count = len(allNovelInfo)
        for i in range(count):
            novelTable.add_row(['【' + str(i) + '】', allNovelInfo[i]['novelName'], allNovelInfo[i]['novelAuthor']])

        print('*************************************************')
        print('***             【{}】小说列表             ***'.format(novelTypeName))
        print('*************************************************')
        print(novelTable)
        print('【q | Q】返回小说类型列表')
        print('【n | N】下一页\t\t\t第{}/{}页'.format(index, pages))
        print('【s | S】跳转至某页')

if __name__ == '__main__':
    pass




