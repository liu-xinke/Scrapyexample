# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com']
    url = r"https://movie.douban.com/top250?start="
    offset = 0
    start_urls = [url+str(offset)]

    def parse(self, response):
        item = DoubanItem()
        movies = response.xpath("//div[@class='info']")
        for each in movies:
            item = DoubanItem()

            # 电影名称
            item["title"] = each.xpath(".//a/span[1]/text()").extract()[0].strip()

            # 导演+主演
            item["director_star"] = each.xpath(".//p/text()[1]").extract()[0].strip()

            # 上映时间+国家+分类
            time_country_classify = each.xpath(".//p/text()[2]").extract()[0].strip()
            # 上映时间
            item["time"]= time_country_classify.split("/")[0]
            # 国家
            item["country"] = time_country_classify.split("/")[1]
            # 类别
            item["classify"] = time_country_classify.split("/")[2]

            # 评分
            item["score"] = each.xpath(".//div[@ class ='star']/span[@ class ='rating_num']/text()").extract()[0]
            # 评分人数
            item["number"] = each.xpath(".// div[@ class ='star'] / span[4] / text()").extract()[0]
            # 电影引述
            item["quote"]= each.xpath(".// div[@ class ='bd'] / p[@ class ='quote'] / span / text()").extract()[0]

            yield item

        if self.offset < 225:
            self.offset += 25
            url = self.url + str(self.offset)
            yield scrapy.Request(url, callback=self.parse)



