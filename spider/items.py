# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CountryCodeItem(scrapy.Item):
    codes = scrapy.Field()


class AreaCodeItem(scrapy.Item):
    codes = scrapy.Field()


class ExchangeCodeItem(scrapy.Item):
    exchange_code = scrapy.Field()
    area_code = scrapy.Field()
    full_exchange_code = scrapy.Field()
    type = scrapy.Field()
    carrier = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    county = scrapy.Field()
    zip_code = scrapy.Field()
    timezone = scrapy.Field()






