# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    suoshu = scrapy.Field()
    name = scrapy.Field()
    date = scrapy.Field()
    price = scrapy.Field()
    pass
