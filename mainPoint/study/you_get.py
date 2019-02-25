#coding=utf-8
import os
import requests
from pyquery import PyQuery as pq


""" 解析网页数据，获得目标url """
def get_urls(url):
    response = requests.get(url)
    if response.status_code == 200:
        # print(response.text)
        html = response.text
        doc = pq(html)
        a_list = doc('li.video a.title')
        url_list = [a.attr('href').strip('//') for a in a_list.items()]
        return url_list
    return None

""" 逐条进行下载视频 """
def cmd_download(url):
    try:
        info = os.system('you-get --debug -o /Users/apple/Desktop/  {}'.format(url))
    except Exception as e:
        print(e)
        cmd_download(url)

""" 函数的主入口 """
def main():
    for i in range(1, 2):
        url = 'https://search.bilibili.com/video?keyword=%E8%90%A7%E4%BA%95%E9%99%8C&order=totalrank&page=' + str(i)
        url_list = get_urls(url)
        print(url_list)

        if url_list is not None:
            [cmd_download(url) for url in url_list]

if __name__ == '__main__':
    main()