#coding=utf-8
from qtModel import *
from qtView import *

class QtController:
    # 初始化
    # downloadPath：下载路径
    def __init__(self, downloadPath):
        self.downloadPath = downloadPath

        self._qtView = QtView()
        self._qtModel = QtModel()

    # 输入校验
    def input_check(self, input):
        try:
            newNumber = int(input)
        except ValueError:
            self._qtView.show_msg("Incorrect index '{}'".format(input))
        else:
            return newNumber

    # 页码校验
    def page_index_check(self, typeIndex, pageIndex):
        if pageIndex > self._qtModel.type_list()[typeIndex]['pageCount'] or pageIndex <= 0:
            return False
        else:
            return True

    # 运行
    def run(self):
        while True:
            # 分类列表
            self._qtView.show_type_list(self._qtModel.type_list())

            # 分类列表 - 操作
            inputOne = self._qtView.choice_operate()
            if inputOne == 'q' or inputOne == 'Q': break

            # 分类下故事列表
            pageIndex = 1
            inputOneCheck = self.input_check(inputOne)

            while True:
                self._qtView.show_story_list(self._qtModel.story_list(inputOneCheck, pageIndex))

                # 故事列表 - 操作
                inputTwo = self._qtView.choice_operate()
                if inputTwo == 'q' or inputTwo == 'Q': break # 返回上层目录
                if inputTwo == 'n' or inputTwo == 'N': # 下一页
                    pageIndex += 1
                    if self.page_index_check(inputOneCheck, pageIndex): continue
                    self._qtView.show_msg('页码太大！！！')
                    pageIndex -= 1
                elif inputTwo == 'b' or inputTwo == 'B': # 上一页
                    pageIndex -= 1
                    if self.page_index_check(inputOneCheck, pageIndex): continue
                    pageIndex += 1
                else: # 显示目录
                    inputTwoCheck = self.input_check(inputTwo)

                    while True:
                        self._qtView.show_story_catalog(self._qtModel.story_catalog(inputTwoCheck))

                        # 目录列表 - 操作
                        inputThree = self._qtView.choice_operate()
                        if inputThree == 'q' or inputThree == 'Q': break # 返回上层目录

                        # 下载
                        self._qtModel.download_story(self._qtModel.story_catalog(inputTwoCheck), self.downloadPath)
                        break

if __name__ == '__main__':
    qtContorller = QtController('/Users/apple/Desktop/')
    qtContorller.run()

