# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CourseItem(scrapy.Item):
    #课程标题
    title = scrapy.Field()
    #课程url
    url = scrapy.Field()
    #课程标题图片
    image_url = scrapy.Field()
    #课程描述
    introduction = scrapy.Field()
    #学习人数
    student = scrapy.Field()
    image_path = scrapy.Field()

if __name__ == '__main__':
    # 定义一个item
    course = CourseItem()
    # 赋值
    course['title'] = "语文"
    # 取值
    print(course['title'])
    print(course.get('title'))
    # 获取全部键
    print(course.keys())
    # 获取全部值
    print(course.items())
