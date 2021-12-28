import scrapy
import sqlite3
from zaza_scrapy.items import ZazaScrapyItem


class YitbSpider(scrapy.Spider):
    name = "yitb"

    def start_requests(self):
        urls = [
            'http://www.yitb.com/category-2',
        ]

        i = 2
        while i < 42:
            urls.append('http://www.yitb.com/category-2-page-' + str(i))
            i = i + 1

        print(urls)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        host = 'http://www.yitb.com/'
        for each in response.xpath("//div[@class='hot-jobs-content']"):
            item = ZazaScrapyItem()
            item['host'] = host
            item['title'] = each.xpath("h3/a/text()").extract_first()
            item['url'] = each.xpath("h3/a/@href").extract_first()
            item['author'] = each.xpath("ul/li/span[1]/text()").extract_first()
            item['publish_date'] = each.xpath("ul/li/span[2]/text()").extract_first()
            item['used'] = '0'

            # print(item)
            yield item
