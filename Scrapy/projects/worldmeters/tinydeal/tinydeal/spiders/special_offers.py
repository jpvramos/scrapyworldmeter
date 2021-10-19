import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html']
    start_urls = ['http://https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html/']

    def parse(self, response):
        pass
