#coding=utf-8
import requests
from requests import RequestException
from pyquery import PyQuery as pq

class ParseHtml:
    # 解析url
    def parse_url(self, url):
        try:
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'Connection': 'keep-alive',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
            }
            response = requests.get(url, headers=headers)
            response.encoding = 'gbk'
        except RequestException as e:
            print('Request error - {}'.format(e))
        else:
            return response.text if response.status_code == requests.codes.ok else None

    # 获取网页中标签内容
    def tagtext_from_html(self, response, tagName):
        doc = pq(response)
        return [tag.text() for tag in doc(tagName).items()]

    # 获取网页中某标签的属性内容
    def attrtext_from_html(self, response, tagName, attrName):
        doc = pq(response)
        return [tag.attr(attrName) for tag in doc(tagName).items()]





