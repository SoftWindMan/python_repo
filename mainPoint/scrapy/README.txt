- 创建项目：scrapy startproject tutorial
- 创建爬虫：scrapy genspider sina "sina.com.cn"
- 项目结构：
    tutorial/
        scrapy.cfg
        tutorial/
            __init__.py
            items.py
            pipelines.py
            settings.py
            spiders/
                __init__.py
                ...
    scrapy.cfg – 项目的配置文件
    tutorial/ – 该项目的python模块，之后您将在此加入代码
    tutorial/items.py – 项目中的item文件
    tutorial/pipelines.py – 项目中的pipelines文件
    tutorial/settings.py – 项目的设置文件
    tutorial/spiders/ – 放置spider代码的目录
- 了解Selector的使用方法（使用内置的Scrapy shell）：scrapy shell “http://www.imooc.com/course/list”
- 运行爬虫：scrapy crawl MySpider（进入项目目录下）
- 存储爬取内容：
    最简单存储爬取的数据的方式是使用Feed exports，主要可以导出四种格式：JSON，JSON lines，CSV和XML。
    常用的存储文件格式为json：scrapy crawl dmoz -o items.json -t json