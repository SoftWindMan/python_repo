#coding = utf-8
import os
from concurrent.futures import ThreadPoolExecutor
from keepAccount.test.parseHtml import *

class DownloadNovel:
    def __init__(self, novelName, baseUrl):
        self.baseUrl = baseUrl
        self.novelName = novelName

        self._parseHtml = ParseHtml()

    # 保存小说章节内容
    def download_chapter(self, future):
        response = future.result()

        # 获取小说章节标题和章节内容
        chapterTitle = self._parseHtml.tagtext_from_html(response, '.novel h1')[0]
        chapterContent = self._parseHtml.tagtext_from_html(response, '.yd_text2')[0]

        # 创建文件夹
        novelDir = os.path.join(os.getcwd(), self.novelName)
        if not os.path.exists(novelDir):
            os.mkdir(novelDir)

        # 保存小说章节（不存在时才下载）
        filePath = os.path.join(novelDir, chapterTitle + '.txt')
        if not os.path.exists(filePath):
            with open(filePath, 'w') as fp:
                fp.write(chapterTitle + '\n')
                fp.write(chapterContent)
            print('{} - 已下载。'.format(chapterTitle))
        else:
            print('{} - 已存在。'.format(chapterTitle))

    # 下载小说
    def download_novel(self):
        listResponse = self._parseHtml.parse_url(self.baseUrl)
        # print(listResponse)

        doc = pq(listResponse)
        chapterUrls = [self.baseUrl + chapterUrl.attr('href') for chapterUrl in doc('.mulu li a').items()]

        executor = ThreadPoolExecutor(max_workers=1000)
        for chapterUrl in chapterUrls:
            executor.submit(self._parseHtml.parse_url, chapterUrl).add_done_callback(self.download_chapter)
        executor.shutdown()
        print('*** 小说【{}】下载完毕！***'.format(self.novelName))

if __name__ == '__main__':
    baseUrl = 'https://www.x88dushu.com/xiaoshuo/42/42267/'
    novelName = '官神'
    novel = DownloadNovel(novelName, baseUrl)
    novel.download_novel()





