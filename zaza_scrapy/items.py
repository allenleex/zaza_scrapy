# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZazaScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    host = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    publish_date = scrapy.Field()
    used = scrapy.Field()
    pass
