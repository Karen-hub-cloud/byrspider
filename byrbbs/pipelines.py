# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyCodePipeline(object):
    def process_item(self, item, spider):
        # print('pipeline got item:',item)
        return item


from scrapy.exporters import JsonItemExporter


class JsonExporterPipleline(object):
    # 调用scrapy提供的json export导出json文件
    def __init__(self):
        self.file = open('export.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


# import MySQLdb
# import MySQLdb.cursors
# from twisted.enterprise import adbapi
#
#
# class MysqlTwistedPipline(object):
#     def __init__(self, dbpool):
#         self.dbpool = dbpool
#
#     @classmethod
#     def from_settings(cls, settings):#settings是包含在settings文件中的所有的变量，所以如果使用了该pipeline，记得修改
#         dbparms = dict(
#             host = settings["MYSQL_HOST"],
#             db = settings["MYSQL_DBNAME"],
#             user = settings["MYSQL_USER"],
#             passwd = settings["MYSQL_PASSWORD"],
#             charset='utf8',
#             cursorclass=MySQLdb.cursors.DictCursor,
#             use_unicode=True,
#         )
#         dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
#
#         return cls(dbpool)
#
#     def process_item(self, item, spider):
#         #使用twisted将mysql插入变成异步执行
#         query = self.dbpool.runInteraction(self.do_insert, item)
#         query.addErrback(self.handle_error, item, spider) #处理异常
#
#     def handle_error(self, failure, item, spider):
#         #处理异步插入的异常
#         print (failure)
#
#     def do_insert(self, cursor, item):
#         #执行具体的插入
#         #根据不同的item 构建不同的sql语句并插入到mysql中
#         insert_sql, params = item.get_insert_sql()
#         cursor.execute(insert_sql, params)
#

#为了代码的清晰度，将es数据类型定义、格式转换和es的连接放到models/es_types.py
from .model.es_types import bbsType

class ElasticsearchPipeline(object):

    def process_item(self, item, spider):
        # 生成bbs对象
        bbs_info = bbsType(item)# 将item转换为es所需格式
        # 将数据传入es
        # jobType继承自DocType，所以DocType有的函数，它都有。
        # save就是DocType定义的将类中的各成员变量打包成数据插入操作，进行数据插入的函数
        bbs_info.partion = item['partion']
        bbs_info.title = item['title']
        bbs_info.send_time = item['send_time']
        bbs_info.url = item['url']
        bbs_info.sender = item['sender']
        bbs_info.reply_count = item['reply_count']
        bbs_info.latest_reply_time = item['latest_reply_time']
        bbs_info.content = item['content']
        bbs_info.comments = item['comments']
        bbs_info.save()

        #仍返回item，使得运行窗口能看到爬到的数据
        return item
