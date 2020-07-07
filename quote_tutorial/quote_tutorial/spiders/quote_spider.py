
import scrapy

from .. items import QuoteTutorialItem

class quote_spider(scrapy.Spider):
    page_number=2
    name='quote_spider'
    start_urls=[
        'http://quotes.toscrape.com/'
    ]
    def parse(self,response):
        item=QuoteTutorialItem()
        # title=response.css('title::text').extract()
        all_quotes=response.css('.quote')
        for quote in all_quotes:
            quotes=quote.css('span.text::text').extract()
            author=quote.css('.author::text')[0].extract()
            tags=quote.css('.tags .tag::text').extract()
            item['quote']=quotes
            item['author']=author
            item['tags']=tags
            yield item
        print('*********************************')
        next_page='http://quotes.toscrape.com/page/'+str(quote_spider.page_number)+'/' 
        if quote_spider.page_number<11:
            yield response.follow(next_page,callback=self.parse)
