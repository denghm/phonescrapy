import unittest
from .phone import AreaCodeSpider
from spider.items import AreaCodeItem, ExchangeCodeItem

class TestPhone(unittest.TestCase):
    def test_parse_information(self):
        ec = ExchangeCodeItem()
        print(ec.__dict__.keys())
        spider = AreaCodeSpider()
        information = r'<div class="panel-body cmpanelbody">\r\n            <strong>Type: </strong>Landline\r\n            <strong>Carrier: </strong>Verizon Maryland, Inc.<br>\r\n            <strong>City: </strong>Chestertown <strong>State: </strong>Maryland, MD <strong>County: </strong>Kent <strong> Zip code: </strong>21620  <strong>Timezone: </strong>Eastern            </div>'
        spider.parse_information(information)


if __name__ == '__main__':
    unittest.main()
