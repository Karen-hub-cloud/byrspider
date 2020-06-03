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
            item['partion'] = line.split(' ')[1].split('：')[1]
            print(item['partion'],line.split(' ')[0].split('：')[1])
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
            # print(crawl_list_url)
            yield scrapy.Request(crawl_list_url, meta={'cookiejar': response.meta['cookiejar'],'item':response.meta['item']}, headers=HEADERS,callback=self.parse_article_list)



    # 处理列表，获取列表上的每条文章信息与文章链接
    def parse_article_list(self, response):
        partion = response.meta['item']['partion']
        sel_article = response.xpath('//*[@class="b-content"]/table/tbody/tr')
        url = sel_article.xpath('td[2]/a/@href').extract()
        title = sel_article.xpath('td[2]/a/text()').extract()
        send_time = sel_article.xpath('td[3]/text()').extract()
        sender = sel_article.xpath('td[4]/a/text()').extract()
        reply_count = sel_article.xpath('td[5]/text()').extract()
        latest_reply_time = sel_article.xpath('td[6]/a/text()').extract()

        # 处理列表的每一行，即每一篇文章的信息，存入item
        for index, url1 in enumerate(url):
            item = ByrArticleItem()
            item['partion'] = partion
            item['title'] = title[index]
            item['url'] = response.urljoin(url[index])
            item['send_time'] = send_time[index]
            item['sender'] = sender[index]
            item['reply_count'] = reply_count[index]
            item['latest_reply_time'] = latest_reply_time[index]
            yield scrapy.Request(item['url'], meta={'cookiejar': response.meta['cookiejar'],'item': item}, headers=HEADERS,callback=self.parse_article_content)

    # 处理文章主体内容
    def parse_article_content(self, response):
        item = response.meta['item']

        # 楼主发帖
        article = response.xpath('//div[3]/div[1]/table/tr[2]/td[2]/div[1]').extract()[0]
        article = re.sub('</?(font|div).*?>', '', article)
        article = re.sub('<br>', '\n', article)
        # 截取帖子中的内容
        # content = re.findall(r"\),(.+?)※",article.split("发信站")[1])[0]
        # print("!!!!!!!!!",content)
        item['content'] = article
        # 追贴
        lists = response.css('div.b-content')
        list_content = lists[0].css('div[class*=a-content-wrap] ::text').extract()
        result = "".join(list_content)
        result = re.sub('</?(font|div).*?>', '', result)
        result = re.sub('<br>', '\n', result)
        comment = ByrArticleSpider.getComments(self,result)
        item['comments'] = comment
        content = re.findall(r"\),(.+?)※",article.split("发信站")[1])
        item['content'] = article

        item['comments'] = ""

        # 获取评论页数
        num = response.xpath('/html/body/section/section/div[4]/div[1]/ul/li[2]/ol/li[10]/a/text()').extract()[0]
        total_page = int(num)
        for i in range(1,total_page+1):
            crawl_list_url = item['url']+'?p='+str(i)
            yield scrapy.Request(crawl_list_url, meta={'cookiejar': response.meta['cookiejar'],'item':response.meta['item']}, headers=HEADERS,callback=self.parse_article_comment)

        fileName = item['partion']+'.txt'  # 爬取的内容存入文件，文件名为：作者-语录.txt
        path = r'F:\Users\Karen\byrbbs-py2-master\byrbbs\board'  # 定义一个变量储存要指定的文件夹目录

        if not os.path.exists(path):  # 没有这个文件目录则新建一个
            os.mkdir(path)  #
        os.chdir(path)
        f = open(fileName, "a+", encoding='utf-8')  # 追加写入文件
        f.write('【文章标题】：' + item['title'] + ' ')
        f.write('【文章地址】：' + item['url'] + ' ')
        f.write('【创建时间】：' + item['send_time'] + ' ')
        f.write('【作者】：' + item['sender'] + ' ')
        f.write('【评论】：' + item['reply_count'] + ' ')
        f.write('【内容】：' + item['content'] + ' ')
        f.write('\n')
        yield item

    def getComments(self, comments):
        result = ""
        lists = comments.split('发信人')
        lists.remove(lists[0])
        lists.remove(lists[0])
        if len(lists) > 0:
            for _list in lists:
                name = re.findall(r":(.+?), 信区", _list)
                text = _list.split("发信站")[1]
                comment = re.findall(r"\),(.+?)※", text)
                result += name[0]
                result += "||"
                result += comment[0]
                result += "|||"
        return result


