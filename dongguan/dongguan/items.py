# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanItem(scrapy.Item):
    title = scrapy.Field()
    num = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()


title =response.xpath(//div[@class='info']//a/span[1])
star=//div[@class='info']//p.text()
score=//div[@class='info']//div[@class='star']/span[@class='rating_num']/text()
number=//div[@class='info']//div[@class='star']/span[4]/text()
desc=//div[@class='info']//div[@class='bd']/p[@class='quote']/span/text()
https://movie.douban.com/top250?start=0