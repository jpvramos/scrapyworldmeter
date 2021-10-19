import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['https://worldpopulationreview.com/countries/countries-by-national-debt']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        gdp_countries = response.xpath('//table[@class="jsx-2139574911 table table-striped tp-table-body"]/tbody/tr')
        
        for country in gdp_countries:
            name = country.xpath(".//td/a/text()").get()
            url = country.xpath(".//@href")
            gdp_debt = country.xpath(".//td[2]/text()").get()
            yield {
                "name":name,
                "coutry_url": url,
                "gdp_debt": gdp_debt
            }
