#coding=utf-8
from pyquery import PyQuery as pq
import requests
import json
import math
import os

class QtModel:
    # 初始化
    def __init__(self):
        self._listUrl = 'https://www.qingting.fm/categories/'
        self._baseListSubUrl = 'https://i.qingting.fm/capi/neo-channel-filter?category={}&attrs=0&curpage={}'
        self._baseStoryPageUrl = 'https://i.qingting.fm/wapi/channels/{}/programs/page/{}/pagesize/10'
        self._baseChapterUrl = 'https://www.qingting.fm/channels/{}/programs/{}/'

        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }

    # 类型列表
    def type_list(self):
        listRes = requests.get(self._listUrl, headers=self._headers).text
        listDoc = pq(listRes)
        typeList = []
        for item in listDoc('._22K0 ._3fnw').items():
            itemDict = {}
            typeName = item.text()
            categoryId = item.attr('href').split('/')[2]

            # 获取总页数
            listSubUrl = 'https://i.qingting.fm/capi/neo-channel-filter?category={}&attrs=0&curpage=1'.format(categoryId)
            listSubPageRes = json.loads(requests.get(listSubUrl, headers=self._headers).text)
            listSubPageInfo = listSubPageRes['data']['channels']
            pageCount = int(math.ceil(int(listSubPageRes['total']) / len(listSubPageInfo)))

            itemDict['typeName'] = typeName
            itemDict['categoryId'] = categoryId
            itemDict['pageCount'] = pageCount
            typeList.append(itemDict)
        return typeList

    # 获取某类页面信息
    def story_list(self, typeIndex, pageIndex):
        self.typeIndex = typeIndex

        # 类型
        typeList = self.type_list()
        categoryId = typeList[int(typeIndex)]['categoryId']

        # 获取页面信息
        storyList = []
        listSubUrl = self._baseListSubUrl.format(categoryId, str(int(pageIndex)))
        listSubPageRes = json.loads(requests.get(listSubUrl, headers=self._headers).text)
        listSubPageInfo = listSubPageRes['data']['channels']
        for item in listSubPageInfo:
            itemDict = {}
            itemDict['storyId'] = item['id']
            itemDict['storyTitle'] = item['title']
            itemDict['storyDesc'] = item['description']
            storyList.append(itemDict)
        storyList.append(typeList[int(typeIndex)]['typeName'])
        return storyList

    # 获取故事目录
    def story_catalog(self, storyIndex):
        # 故事id和标题
        storyList = self.story_list(self.typeIndex, 1)
        storyId = storyList[int(storyIndex)]['storyId']

        # 故事目录页数
        storyUrl = 'https://i.qingting.fm/wapi/channels/{}/programs/page/1/pagesize/10'.format(storyId)
        storyRes = json.loads(requests.get(storyUrl).text)
        storyCatalogData = storyRes['data']
        storyPageCount = int(math.ceil(int(storyRes['total']) / len(storyCatalogData)))

        # 故事目录标题和url
        storyCatalog = []
        for i in range(storyPageCount):
            storyPageUrl = self._baseStoryPageUrl.format(storyId, str(i + 1))
            storyPageRes = json.loads(requests.get(storyPageUrl, headers=self._headers).text)['data']
            for item in storyPageRes:
                itemDict = {}
                itemDict['chapterTitle'] = item['name']
                itemDict['chapterUrl'] = self._baseChapterUrl.format(item['channel_id'], item['id'])
                storyCatalog.append(itemDict)
        storyCatalog.append(storyList[int(storyIndex)]['storyTitle'])
        return storyCatalog

    def download_story(self, storyCatalog, downloadPath):
        # 创建保存目录
        storyName = storyCatalog[-1]
        filePath = os.path.join(downloadPath, storyName)
        if not os.path.exists(filePath):
            os.mkdir(filePath)

        for i in range(len(storyCatalog) - 1):
            if not os.path.exists(os.path.join(filePath, storyCatalog[i]['chapterTitle'])): continue
            os.system('you-get -d -o {} {}'.format(filePath, storyCatalog[i]['chapterUrl']))
        print('【{}】下载完成。'.format(storyName))

if __name__ == '__main__':
    qt = QtModel()
    typeList = qt.type_list()
    # storyList = qt.story_list(35)
    # storyCatalog = qt.story_catalog(1)
    print(typeList)


