#coding=utf-8
from parseNovel import *

novelName = 'novel_官神'
baseUrl = 'https://www.x88dushu.com/xiaoshuo/42/42267/'
parseNovel = ParseNovel(novelName)
response = parseNovel.parse_url(baseUrl)[0]

if response:
    """ 章节标题 """
    newChapterTitles = []
    chapterTitles = parseNovel.get_tagtext(response, '.mulu li')
    for i in range(len(chapterTitles)):
        if chapterTitles[i] == '': continue
        chapterTitle = chapterTitles[i] if '章' not in chapterTitles[i] else chapterTitles[i].split('章')[1].strip()
        chapterTitle = '第' + str(i) + '章 ' + chapterTitle + '.txt'
        newChapterTitles.append(chapterTitle)

    """ 章节地址 """
    chapterUrls = [(baseUrl + chapterUrl) for chapterUrl in parseNovel.get_attrtext(response, '.mulu li a', 'href')]

    """ 章节内容 """
    newChapterContents = []
    chapterContents = parseNovel.parse_url(chapterUrls)
    for chapterContent in chapterContents:
        chapterContent = parseNovel.get_tagtext(chapterContent, '.yd_text2')[0]
        newChapterContents.append(chapterContent)

    # print(len(newChapterTitles), len(chapterUrls), len(newChapterContents))
    # print(newChapterContents[0])

    """ 保存小说 """
    parseNovel.write_to_file(newChapterTitles, newChapterContents)





