import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info/world-population']
    start_urls = ['http://www.worldometers.info/world-population/']

    def parse(self, response):
        pass
