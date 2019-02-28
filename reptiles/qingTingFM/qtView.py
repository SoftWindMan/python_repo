#coding=utf-8
from prettytable import *

class QtView:
    # 消息
    def show_msg(self, msg):
        print('Error - ' + msg)

    # 小说分类列表
    def show_type_list(self, typeList):
        pt = PrettyTable(['编号', '类名', '页数'])
        pt.align['编号'] = 'l'
        pt.align['类名'] = 'l'
        pt.align['页数'] = 'l'
        print('************* 蜻蜓FM分类列表 *************')
        for i in range(len(typeList)):
            pt.add_row(['【' + str(i) + '】', typeList[i]['typeName'], typeList[i]['pageCount']])
        print(pt)
        print('【q | Q】退出')

    # 选择操作
    def choice_operate(self):
        return input('请选择相应操作的编号：')

    # 故事列表
    def show_story_list(self, storyList):
        pt = PrettyTable(['编号', '名称', '描述'])
        pt.align['编号'] = 'l'
        pt.align['名称'] = 'l'
        pt.align['描述'] = 'l'
        print('*************************************** 【{}】分类故事列表 ***************************************'.format(storyList[-1]))
        for i in range(len(storyList) - 1):
            pt.add_row(['【' + str(i) + '】', storyList[i]['storyTitle'], storyList[i]['storyDesc']])
        print(pt)
        print('【n | N】下一页')
        print('【b | B】上一页')
        print('【q | Q】返回上层目录')

    # 故事目录
    def show_story_catalog(self, storyCatalog):
        pt = PrettyTable(['章节'])
        pt.align['章节'] = 'l'
        print('*************************************** 【{}】故事目录 ***************************************'.format(storyCatalog[-1]))
        for i in range(len(storyCatalog) - 1):
            pt.add_row([storyCatalog[i]['chapterTitle']])
        print(pt)
        print('【y | Y】下载')
        print('【q | Q】返回上层目录')




