# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentposSpider(scrapy.Spider):

    name = 'tencentpos'
    allowed_domains = ['tencent.com']
    url = "https://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [url+str(offset)]


    def parse(self, response):
        if __name__ == '__main__':
            for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
                item = TencentItem()
                position_name = each.xpath("./td[1]/a/text()").extract()
                position_link = each.xpath("./td[1]/a/@href").extract()
                position_type = each.xpath("./td[2]/text()").extract()
                position_number = each.xpath("./td[3]/text()").extract()
                position_address = each.xpath("./td[4]/text()").extract()
                position_time = each.xpath("./td[5]/text()").extract()
                item['position_name'] = position_name[0]
                item['position_link'] = position_link[0]
                item['position_type'] = position_type[0]
                item['position_number'] = position_number[0]
                item['position_address'] = position_address[0]
                item['position_time'] = position_time[0]
                yield item
            if self.offset < 1680:
                self.offset += 10
            yield scrapy.Request(self.url + str(self.offset),callback=self.parse)
