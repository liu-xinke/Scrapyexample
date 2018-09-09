# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem

class DgSpider(CrawlSpider):
    name = 'dg'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=0']

    rules = (
        Rule(LinkExtractor(allow=r'page=\d+')),
        Rule(LinkExtractor(allow=r'html/question/\d+/\d+.shtml'),callback="parse_item"))

    def parse_item(self, response):
        item=DongguanItem()
        item['title'] = response.xpath('/html/body/div[6]/div/div[1]/div[1]/strong/text()').extract()[0]
        item['num']=item['title'].split(" ")[-1].split(':')[-1]

        item['content']=response.xpath('/html/body/div[6]/div/div[2]/div[1]/text()').extract()[0]
        item['url'] = response.url
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        yield item
