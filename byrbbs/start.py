# -*- coding: utf-8 -*-
# command.py file
import os
#如果此文件就存于项目目录，可以注释掉下面这行更改工作目录的代码
# os.chdir(r'C:\Users\chen\PycharmProjects\byrbbs')
# os.system('scrapy crawl byr_section')   # 运行爬虫byr_section
# os.system('scrapy crawl byr_article')  # 运行爬虫byr_section，并将item存到xml文件中（在没写pipline前可以先在本地存储）
os.system('scrapy crawl byr_article')