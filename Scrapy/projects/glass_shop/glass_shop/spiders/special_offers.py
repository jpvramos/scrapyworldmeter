import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['http://www.glassesshop.com/bestsellers']

    def parse(self, response):
        
        for glass in response.xpath('//div[@id="product-lists"]/div[@class="col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item"]'):
            yield{
                'product_url':glass.xpath('.//div[@class="product-img-outer"]/a[1]/@href').get(),
                'product_image_link':glass.xpath('.//div[@class="product-img-outer"]/a[1]/img[1]/@data-src').get(),
                'product_name':glass.xpath('.//div[@class="p-title-block"]/div[2]/div/div[1]/div/a/@title').get(),
                'product_price':glass.xpath('.//div[@class="p-title-block"]/div[2]/div/div[2]/div/div/span/text()').get(),
            }