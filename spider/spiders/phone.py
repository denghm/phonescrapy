from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from spider.items import AreaCodeItem, ExchangeCodeItem
import re


class AreaCodeSpider(CrawlSpider):
    name = 'area'
    allowed_domains = ['www.phonenumberdata.net']
    start_urls = ['http://www.phonenumberdata.net/']
    rules = [
        Rule(LinkExtractor(allow=r'net/$'), callback='parse_area_code_items', follow=True),
        Rule(LinkExtractor(allow=r'net/\d{3}-.*'), follow=True),
        Rule(LinkExtractor(allow=r'[a-zA-Z_]+-\d{3}-\d{3}$', deny=r'result.*'), callback='parse_exchange_code_items', follow=True)
    ]

    def parse_area_code_items(self, response):
        url = response.url
        # text = response.xpath('//ul[@id="l"]//li/a/text()').extract()
        codes = []
        for link in response.xpath('//div[@id="ul1"]/a'):
            d = {}
            d['area_code'] = link.xpath('text()').extract_first()
            d['state'] = link.xpath('@title').extract_first()
            codes.append(d)
        area_codes = AreaCodeItem()
        area_codes['codes'] = codes
        return area_codes

    def parse_exchange_code_items(self, response):
        print(response.url)
        ec = ExchangeCodeItem()
        information = response.xpath('//div[@id="allcontent"]/div/div[@class="panel panel-default cmpanel"][1]/div[@class="panel-body cmpanelbody"]').extract_first()
        names = ['type', 'carrier', 'city', 'state', 'county', 'zip_code', 'timezone']

        url = response.url
        full_exchange_code = url[-7:]
        items = full_exchange_code.split('-')
        area_code = items[0]
        exchange_code = items[1]
        d = self.parse_information(information)
        for name in names:
            ec[name] = d.get(name, 'NA')
        ec['full_exchange_code'] = full_exchange_code
        ec['area_code'] = area_code
        ec['exchange_code'] = exchange_code
        return ec

    def normalize_value(self, value):
        return value.strip()

    def normalize_name(self, name):
        v = name.strip().lower()
        arr = re.split(r'[\s+]', v)
        if len(arr) > 1:
            return "_".join(arr)
        else:
            return v

    def parse_information(self, information):
        pattern = r'(strong>([\w\s]+):\s*</strong>([\d\w\s\,\.]+)(\\r\\n|<))'
        m = re.findall(pattern, information)
        d = {}
        for t in m:
            d[self.normalize_name(t[1])] = self.normalize_value(t[2])
        return d






