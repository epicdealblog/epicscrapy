import scrapy
from quotes_js_scraper.items import QuoteItem

from scrapy_splash import SplashRequest

# cd /Users/bryanlv/epic/epicdealblog/quotes-js-project/quotes_js_scraper

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    def start_requests(self):
        url = 'https://quotes.toscrape.com/js'
        yield SplashRequest(url, callback=self.parse)
        
    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.css('div.quote'):
            quote_item['text'] = quote.css('span.text::text').get()
            
            yield quote_item
