import scrapy
from urllib3.connectionpool import xrange

from byrbbs.spiders.byr_config import URL_HEAD,HEADERS,LOGIN_FORMDATA
from byrbbs.items import ByrArticleItem
import re
import os

class ByrArticleSpider(scrapy.Spider):
    name = "byr_article"
    allowed_domains = ["bbs.byr.cn"]
    start_urls = ["https://bbs.byr.cn"]
    article_per_list = 30

    def start_requests(self):
        return [scrapy.FormRequest("https://bbs.byr.cn/user/ajax_login.json",
                                   formdata=LOGIN_FORMDATA,
                                   meta={'cookiejar': 1},
                                   headers=HEADERS,
                                   callback=self.logged_in)]

    def logged_in(self, response):
        f = open("学术科技讨论区所有板块.txt")
        line = f.readline()
        while line:
            line = f.readline()
            line.replace('/', '&').replace('\\', '&&')
            item = ByrArticleItem()
            item['section_name'] = line.split(' ')[1].split('：')[1]
            print(item['section_name'],line.split(' ')[0].split('：')[1])
            yield scrapy.Request(response.urljoin(line.split(' ')[0].split('：')[1]),
                                 meta={'cookiejar':response.meta['cookiejar'],'item':item},
                                 headers=HEADERS, callback=self.parse_article_list_pre)
        f.close()


    # 处理列表，翻页问题
    def parse_article_list_pre(self, response):
        page_list_num = response.xpath('//*[@class="t-pre-bottom"]/div[1]/ul/li[1]/i/text()').extract()[0]
        total_num = int(page_list_num)//self.article_per_list+1  #页数从1到total_num
        first_list = response._get_url()
        for i in range(1,total_num+1):
            crawl_list_url = first_list+'?p='+str(i)
            print(crawl_list_url)
            yield scrapy.Request(crawl_list_url, meta={'cookiejar': response.meta['cookiejar'],'item':response.meta['item']}, headers=HEADERS,callback=self.parse_article_list)



    # 处理列表，获取列表上的每条文章信息与文章链接
    def parse_article_list(self, response):
        section_name = response.meta['item']['section_name']
        sel_article = response.xpath('//*[@class="b-content"]/table/tbody/tr')
        article_url = sel_article.xpath('td[2]/a/@href').extract()
        article_title = sel_article.xpath('td[2]/a/text()').extract()
        article_createtime = sel_article.xpath('td[3]/text()').extract()
        article_author = sel_article.xpath('td[4]/a/text()').extract()
        article_comment = sel_article.xpath('td[5]/text()').extract()

        # 处理列表的每一行，即每一篇文章的信息，存入item
        for index, url in enumerate(article_url):
            item = ByrArticleItem()
            item['section_name'] = section_name
            item['article_title'] = article_title[index]
            item['article_url'] = response.urljoin(article_url[index])
            item['article_createtime'] = article_createtime[index]
            item['article_author'] = article_author[index]
            item['article_comment'] = article_comment[index]
            yield scrapy.Request(item['article_url'], meta={'cookiejar': response.meta['cookiejar'],'item': item}, headers=HEADERS,callback=self.parse_article_content)

    # 处理文章主体内容
    def parse_article_content(self, response):
        article = response.xpath('//div[3]/div[1]/table/tr[2]/td[2]/div[1]').extract()[0]
        article = re.sub('</?(font|div).*?>', '', article)
        article = re.sub('<br>', '\n', article)
        item = response.meta['item']
        item['article_content'] = article
        fileName = item['section_name']+'.txt'  # 爬取的内容存入文件，文件名为：作者-语录.txt
        path = r'F:\Users\Karen\byrbbs-py2-master\byrbbs\board'  # 定义一个变量储存要指定的文件夹目录

        if not os.path.exists(path):  # 没有这个文件目录则新建一个
            os.mkdir(path)  #
        os.chdir(path)
        f = open(fileName, "a+", encoding='utf-8')  # 追加写入文件
        f.write('【文章标题】：' + item['article_title'] + ' ')
        f.write('【文章地址】：' + item['article_url'] + ' ')
        f.write('【创建时间】：' + item['article_createtime'] + ' ')
        f.write('【作者】：' + item['article_author'] + ' ')
        f.write('【评论】：' + item['article_comment'] + ' ')
        f.write('【内容】：' + item['article_content'] + ' ')
        f.write('\n')
        yield item


