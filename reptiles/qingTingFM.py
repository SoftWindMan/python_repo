#coding=utf-8
import requests
import json
import os
from pyquery import PyQuery as pq

class QingTingFM:
    # 初始化
    def __init__(self, channelCount, bookName):
        self.channelCount = channelCount
        self.bookName = bookName

        self.listUrl = 'https://www.qingting.fm/channels/{}/'
        self.pageUrl = 'https://i.qingting.fm/wapi/channels/{}/programs/page/{}/pagesize/10'
        self.baseChapterUrl = 'https://www.qingting.fm/channels/{}/programs/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }

    # 创建保存目录
    def _create_dir(self):
        self.filePath = os.path.join(os.getcwd(), self.bookName)
        if not os.path.exists(self.filePath):
            os.mkdir(self.filePath)

    # 总页数
    def _page_count(self):
        baseRes = requests.get(self.listUrl.format(self.channelCount)).text
        doc = pq(baseRes)
        pageCount = int([page.text() for page in doc('.pagination li').items()][-2])
        return pageCount

    # 下载
    def download(self):
        self._create_dir()

        for i in range(self._page_count()):
            realPageUrl = self.pageUrl.format(self.channelCount, str(i + 1))
            res = requests.get(realPageUrl, headers=self.headers).text
            for chapterNumber in json.loads(res)['data']:
                # print(chapterNumber['name'])

                chapterUrl = self.baseChapterUrl.format(self.channelCount) + str(chapterNumber['id'])
                os.system('you-get -d -o {} {}'.format(self.filePath, chapterUrl))

    # 修改文件类型
    def modify_file_type(self, dirPath, rawType, targetType):
        # 列出当前目录下所有的文件
        files = os.listdir(dirPath)
        # print('files - ', files)

        for filename in files:
            portion = os.path.splitext(filename)
            if portion[1] == '.' + rawType:
                newname = portion[0] + '.' + targetType
                os.rename(filename, newname)
        print('文件类型修改成功！')

if __name__ == '__main__':
    ts = QingTingFM('78160', 'DaoMuBiJi')
    # ts.download()
    ts.modify_file_type('/Users/apple/')