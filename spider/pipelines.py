# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from spider.items import AreaCodeItem, CountryCodeItem, ExchangeCodeItem
from spider.dao.model_dao import Dao
from spider.dao.model import AreaCode, CountryCode, ExchangeCode


class SpiderPipeline(object):
    def __init__(self):
        self.dao = Dao()

    def process_item(self, item, spider):
        if isinstance(item, AreaCodeItem):
            area_codes = item['codes']
            c = self.dao.get_country_by_code('1')
            for code in area_codes:
                a = self.dao.get_area_by_code(code['area_code'])
                if not a:
                    area_code = AreaCode(area_code=code['area_code'], state=code['state'])
                    area_code.country_code = c
                    self.dao.save(area_code)

        if isinstance(item, CountryCodeItem):
            countries = item['codes']
            for country in countries:
                c = self.dao.get_country_by_code(country['country_code'])
                if not c:
                    country_code = CountryCode(country_code=country['country_code'], country=country['country'],
                                               iso_code=country['iso_code'], population = country['population'],
                                               area=country['area'], gdp=country['area'])
                    self.dao.save(country_code)

        if isinstance(item, ExchangeCodeItem):
            e = self.dao.get_exchange_by_code(item['exchange_code'])
            if not e:
                exchange_code = ExchangeCode(exchange_code=item['exchange_code'],
                                             area_code_and_exchange_code=item['full_exchange_code'],
                                             type=item['type'],
                                             carrier=item['carrier'],
                                             city=item['city'],
                                             state=item['state'],
                                             county=item['county'],
                                             zip_code=item['zip_code'],
                                             timezone=item['timezone'])
                area_code = self.parse_area_code_from_full_exchange_code(item['full_exchange_code'])
                a = self.dao.get_area_by_code(area_code)
                exchange_code.area_code = a
                self.dao.save(exchange_code)
        return item

    def parse_area_code_from_full_exchange_code(self, full_exchange_code):
        return full_exchange_code[:3]
