#coding=utf-8
from novelParse import *
import os

novelName = 'novel_官神'
listUrl = 'https://www.x88dushu.com/xiaoshuo/42/42267/'
responseEncoding = 'gbk'

novelParse = NovelParse(novelName, responseEncoding)

# 创建文件夹
novelParse.create_noveldir()

# 请求章节目录
listResponse = novelParse.parse_url(listUrl)
if listResponse:
    chapterTitles = novelParse.get_tagtext(listResponse, '.mulu li')
    chapterUrls = novelParse.get_attrtext(listResponse, '.mulu li a', 'href')
    # print(len(chapterTitles), len(chapterUrls))

    for i in range(len(chapterTitles)):
        if chapterTitles[i] == '': continue
        chapterTitle = chapterTitles[i] if '章' not in chapterTitles[i] else chapterTitles[i].split('章')[1].strip()
        chapterTitle = '第' + str(i) + '章 ' + chapterTitle + '.txt'

        # 本章未下载
        if not novelParse.is_exists_file(chapterTitle):
            # 请求章节内容
            chapterUrl = listUrl + chapterUrls[i]
            chapterResponse = novelParse.parse_url(chapterUrl)

            # 获取章节内容并保存
            if chapterResponse:
                chapterContent = novelParse.get_tagtext(chapterResponse, '.yd_text2')[0]
                novelParse.write_to_file(chapterTitle, chapterContent)
                print('{} - 下载完成。'.format(chapterTitle))
        else: # 本章已下载
            print('{} - 已经存在。'.format(chapterTitle))

