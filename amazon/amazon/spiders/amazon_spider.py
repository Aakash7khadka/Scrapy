import scrapy
from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1594108864&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0']

    def parse(self, response):
        item=AmazonItem()
        name=response.css('.a-color-base.a-text-normal').css('::text').extract()
        price=response.css('.a-spacing-top-small .a-price-fraction , .a-spacing-top-small .a-price-whole , .sg-col-24-of-28:nth-child(1) .s-image').css('::text').extract()
        author=response.css('.sg-col-12-of-28 .a-size-base+ .a-size-base').css('::text').getall()
        picture=response.css('.s-image::attr(src)').extract()
        item['name']=name
        item['price']=price
        item['author']=author
        item['picture']=picture

        yield item
