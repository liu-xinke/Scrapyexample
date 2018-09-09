# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):

    # 电影名称
    title = scrapy.Field()
    # 导演+主演
    director_star = scrapy.Field()
    # 上映时间
    time = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 类别
    classify = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评分人数
    number = scrapy.Field()
    # 电影引述
    quote = scrapy.Field()

