# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from newdongguan.items import NewdongguanItem

class DongSpider(CrawlSpider):
    name = 'dong'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=']

    rules = (
        Rule(LinkExtractor(allow=r'page=\d')),
    )

    def parse_item(self, response):
        item=NewdongguanItem()

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return item
