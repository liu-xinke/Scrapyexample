# -*- coding: utf-8 -*-
import scrapy


class Day2Spider(scrapy.Spider):
    name = 'day2'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
