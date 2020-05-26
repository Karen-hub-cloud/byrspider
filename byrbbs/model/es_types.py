# -*- coding: utf-8 -*-
# elasticsearch_dsl：https://elasticsearch-dsl.readthedocs.io/en/latest/

from elasticsearch_dsl import Document, Date, Completion, Keyword, Text, Integer

from elasticsearch_dsl.analysis import CustomAnalyzer
# 使用ik分词
ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])

from elasticsearch_dsl.connections import connections
# 本地服务器
es = connections.create_connection(host="127.0.0.1")


# 使用python创建索引
class bbsType(Document):
    # 设置index名称和document名称
    class Index:
        name = "byr"
        # type = "article"
        doc_type = "article"
        # settings = {
        #   "number_of_shards": 2,
        # }

    # TODO:fileds定义
    partion = Keyword()  # 板块名称？
    title = Text(analyzer="ik_smart")  # 标题
    url = Keyword()  # 链接
    send_time = Date()  # 日期
    sender = Keyword()  # 作者
    reply_count = Integer()  # 评论个数
    latest_reply_time = Date()
    content = Text(analyzer="ik_max_word")  # 内容
    comments = Text(analyzer="ik_smart")  # 评论

    suggest = Completion(analyzer=ik_analyzer)  # 搜索建议


    def __init__(self,item):
        super(bbsType, self).__init__()#调一下父类的init，避免init重写导致一些init操作没执行
        self.assignment(item)

# if __name__ == '__main__':
#     bbsType.init()

    # TODO:将item转换为es的数据
    def assignment(self, item):
        # TODO：给没爬到的字段赋默认值：空串
        keys = ['partion', 'title', 'url', 'send_time', 'sender', 'reply_count', 'content','latest_reply_time']
        for key in keys:
            try:
                item[key]
            except:
                item[key] = ''
        # TODO：将字段值转换为es的数据
        # 虽然只是将原来的item值赋给了成员变量，但这个过程中会执行数据格式转换操作，比如url本来在item是python的字符串类型，转换后变为es的keyword类型
        self.partion = item['partion']
        self.title = item['title']
        self.send_time = item['send_time']
        self.url = item['url']
        self.sender = item['sender']
        self.reply_count = item['reply_count']
        self.content = item['content']
        self.latest_reply_time = "2020-01-11"

        # # 或者简化代码为
        # for key in keys:
        #     vars(self)[key]=item[key]

        # TODO：生成搜索建议词
        # self.suggest = self.gen_suggests(((self.title, 10), (self.content, 7)))

    def gen_suggests(self, info_tuple):
        # 根据字符串生成搜索建议数组
        used_words = set()  # set为去重功能
        suggests = []
        for text, weight in info_tuple:
            if text:
                # 字符串不为空时，调用elasticsearch的analyze接口分析字符串（分词、大小写转换）
                words = es.indices.analyze(body={'text': text, 'analyzer': "ik_max_word"},params={'filter':["lowercase"]})
                print("words",words)
                # anylyzed_words = set([r["token"] for r in words["tokens"] if len(r["token"]) > 1])
                analyzed_words = []
                for r in words["tokens"]:
                    if len(r["token"]) > 1:
                        analyzed_words.append(r["token"])
                anylyzed_words = set(analyzed_words)

                new_words = anylyzed_words - used_words
            else:
                new_words = set()

            if new_words:
                suggests.append({'input': list(new_words), 'weight': weight})
                print("suggests",suggests)
        return suggests

