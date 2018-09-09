# -*- coding: utf-8 -*-
import scrapy
from test1.items import Test1Item

class Myspider2Spider(scrapy.Spider):
    name = 'myspider2'
    allowed_domains = ['http://itcast.cn/']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#apython']

    def parse(self, response):
        # with open("teach.html",'wb') as f:
        #     print(type(response.body))
        #     f.write(response.body)

        for each in response.xpath("//div[@class='li_txt']"):
            name = each.xpath("./h3/text()").extract()
            pos = each.xpath("./h4/text()").extract()
            desc = each.xpath("./p/text()").extract()
            item = Test1Item()
            item['name']=name[0]
            item['title']=pos[0]
            item['desc']=desc[0]
            yield item
