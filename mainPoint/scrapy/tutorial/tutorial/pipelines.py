# -*- coding: utf-8 -*-
import pymysql
from tutorial.settings import *

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

class MyPipeline(object):
    def __init__(self):
        pass
    def open_spider(self, spider):
        pass
    def close_spider(self, spider):
        pass

    #该方法用于处理数据
    def process_item(self, item, spider):
        conn = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PWD, db=MYSQL_DB, charset=MYSQL_CHARSET)
        cur = conn.cursor()
        sql = """insert into tutorial(url, title, image_url, student, introduction) values('%s', '%s', '%s', '%s', '%s')""" %(item['url'], item['title'], item['image_url'], item['student'], item['introduction'])
        try:
            cur.execute(sql)
            conn.commit()
        except Exception:
            conn.rollback()
        conn.close()
        return item


