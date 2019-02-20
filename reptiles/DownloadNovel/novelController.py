#coding=utf-8
from novelView import *
from novelModel import *
from downloadNovel import *

# 控制类
class NovelController:
    # 初始化模型类和视图类
    def __init__(self):
        self._novelView = NovelView()
        self._novelModel = NovelModel()

    # 初始化页面
    def init_page(self):
        self._novelView.show_novel_type_name_list_page(self._novelModel.all_novel_type_names())

    # 数字校验
    def number_check(self, number):
        try:
            newNumber = int(number)
        except ValueError:
            self._novelView.show_msg_page("Incorrect index '{}'".format(number))
            return False
        else:
            return newNumber

    # 运行
    def run(self):
        while True:
            # 初始化小说类型列表
            self.init_page()

            # 小说类型列表操作
            novelTypeNameIndex = self._novelView.choice_operate_page()
            if novelTypeNameIndex == 'q' or novelTypeNameIndex == 'Q':  # 退出
                break
            else:  # 选择小说类型
                pageIndex = 1
                newNovelTypeNameIndex = self.number_check(novelTypeNameIndex)
                singleNovels = self._novelModel.single_novels(newNovelTypeNameIndex, pageIndex)
                while True:
                    self._novelView.show_single_novels_page(singleNovels)

                    # 小说列表操作
                    novelIndex = self._novelView.choice_operate_page()
                    if novelIndex == 'n' or novelIndex == 'N':  # 下一页
                        pageIndex += 1
                        singleNovels = self._novelModel.single_novels(newNovelTypeNameIndex, pageIndex)
                    elif novelIndex == 'b' or novelIndex == 'B':  # 退回上层列表
                        break
                    elif novelIndex == 's' or novelIndex == 'S':  # 跳转
                        skipPageIndex = self._novelView.input_skip_page_index()
                        newSkipPageIndex = self.number_check(skipPageIndex)
                        pageIndex = newSkipPageIndex
                        singleNovels = self._novelModel.single_novels(newNovelTypeNameIndex, newSkipPageIndex)
                    else:  # 下载小说
                        newNovelIndex = self.number_check(novelIndex)
                        novelName, novelUrl = self._novelModel.one_novel(newNovelTypeNameIndex, pageIndex, newNovelIndex)
                        downloadNovel = DownloadNovel(novelName, novelUrl)
                        downloadNovel.download_novel()

if __name__ == '__main__':
    novelController = NovelController()
    novelController.run()


