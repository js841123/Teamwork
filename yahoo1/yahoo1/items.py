# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Yahoo1Item(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    ID = scrapy.Field()
    price = scrapy.Field()
    rate = scrapy.Field()
    tag = scrapy.Field()
    # name = scrapy.Field()
    #pass
