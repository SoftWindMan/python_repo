#coding=utf-8
from keepAccount.test.userOperate import *
from keepAccount.test.novelIndex import *
from keepAccount.test.downloadNovel import *

class ShowNovel:
    def __init__(self):
        self._novelIndex = NovelIndex()

    def show_novel_type(self):
        allNovelTypeName = self._novelIndex.all_novel_type_info()
        print('****** 所有小说分类 ******')
        count = len(allNovelTypeName)
        for i in range(len(allNovelTypeName)):
            print('【{}】 {} - 共{}页'.format(i, allNovelTypeName[i]['novelTypeName'], allNovelTypeName[i]['pages']))
        print('【q | Q】 退出')

    def show_all_novel_under_novel_type_name(self, novelTypeName, index):
        allNovelInfo = self._novelIndex.one_page_all_novel_under_novel_type_name(novelTypeName, index)
        print('****** 【{}】小说列表 ******'.format(novelTypeName))
        count = len(allNovelInfo)
        print('编号\t\t小说名')
        for i in range(count):
            print('【{}】\t{}'.format(i, allNovelInfo[i]['novelName']))
        print('*** 【back】返回小说类型列表\t【next】下一页 ***')


if __name__ == '__main__':
    showNovel = ShowNovel()
    userOperate = UserOperate()

    novelTypeName = None
    while True:
        showNovel.show_novel_type()
        novelTypeIndex = input('请选择小说类型编号：')
        if novelTypeIndex == 'q' or novelTypeIndex == 'Q':
            break
        else:
            novelTypeName, pages = userOperate.choice_novel_type(novelTypeIndex)
            index = 1
            showNovel.show_all_novel_under_novel_type_name(novelTypeName, index)
            while True:
                action = input('请选择相应的小说编号或动作：')
                if action == 'back':
                    break
                elif action == 'next':
                    index += 1
                    if index <= pages:
                        showNovel.show_all_novel_under_novel_type_name(novelTypeName, index)
                else:
                    novelName, novelUrl = userOperate.choice_novel(novelTypeName, index, action)

                    print(novelName, novelUrl)
                    downloadNovel = DownloadNovel(novelName, novelUrl)
                    downloadNovel.download_novel()




