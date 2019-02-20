#coding=utf-8
from prettytable import PrettyTable
from colored import *

# 视图类
class NovelView:
    def __init__(self):
        self._colored = Colored()

    # 显示消息
    def show_msg_page(self, msg):
        print(self._colored.red('Error - ' + msg))

    # 小说类型列表
    def show_novel_type_name_list_page(self, allNovelTypeNames):
        print('*************************************************')
        print('***                小说分类目录                 ***')
        print('*************************************************')
        for novelTypeName in allNovelTypeNames:
            print(novelTypeName)
        print('【q | Q】退出')

    # 选择操作
    def choice_operate_page(self):
        return raw_input(self._colored.red('请选择操作类型：'))

    # 显示某页小说
    def show_single_novels_page(self, singleNovels):
        novelTable = PrettyTable(['编号', '小说名', '作者'])
        for i in range(len(singleNovels) - 3):
            novelTable.add_row(['【' + str(i) + '】', singleNovels[i]['novelName'], singleNovels[i]['novelAuthor']])
        print('*************************************************')
        print('***             【{}】小说目录             ***'.format(singleNovels[-3]))
        print('*************************************************')
        print(novelTable)
        print('【b | B】返回上级目录')
        print('【n | N】下一页\t\t\t第{}/{}页'.format(singleNovels[-1], singleNovels[-2]))
        print('【s | S】跳转至某页')

    # 输入要跳转的页码
    def input_skip_page_index(self):
        return raw_input(self._colored.red('请输入要跳转的页码：'))

if __name__ == '__main__':
    pass




