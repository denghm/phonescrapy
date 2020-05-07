from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from spider.items import CountryCodeItem
from scrapy import Selector


class CountrySpider(CrawlSpider):
    name = 'country'
    allowed_domains = ['www.countrycode.org']
    start_urls = ['https://www.countrycode.org/']
    rules = [
        Rule(LinkExtractor(allow=(r'org/$')), callback='parse_country_code_items', follow=False)
    ]

    def parse_country_code_items(self, response):
        url = response.url
        print(url)
        codes = []
        for item in response.xpath('//div[@class="visible-md visible-lg"]/table/tbody/tr').extract():
            d = {}
            link = Selector(text=item)
            d['country'] = link.xpath('//tr/td[1]/a/text()').extract_first()
            d['country_code'] = link.xpath('//tr/td[2]/text()').extract_first()
            d['iso_code'] = link.xpath('//tr/td[3]/text()').extract_first()
            value = link.xpath('//tr/td[4]/text()').extract_first()
            d['population'] = int(value.replace(',', ''))
            value = link.xpath('//tr/td[5]/text()').extract_first()
            d['area'] = int(value.replace(',', ''))
            d['gdp'] = link.xpath('//tr/td[6]/text()').extract_first()
            codes.append(d)
        country_codes = CountryCodeItem()
        country_codes['codes'] = codes
        return country_codes








