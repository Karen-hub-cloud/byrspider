# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ByrArticleItem(scrapy.Item):
    # define the fields for your item here like:
    partion = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    send_time = scrapy.Field()
    sender = scrapy.Field()
    reply_count = scrapy.Field()
    latest_reply_time = scrapy.Field()
    content = scrapy.Field()
    comments = scrapy.Field()
    suggest = scrapy.Field()

class ByrSectionItem(scrapy.Item):
    section_url = scrapy.Field()
    partion = scrapy.Field()
    section_article_total = scrapy.Field()
    top_section_num = scrapy.Field()
    top_section_name = scrapy.Field()