# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewdongguanItem(scrapy.Item):
    title = scrapy.Field()
    num = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()

