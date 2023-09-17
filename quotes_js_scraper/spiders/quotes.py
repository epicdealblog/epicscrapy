import scrapy
from quotes_js_scraper.items import QuoteItem

from scrapy_splash import SplashRequest

# cd /Users/bryanlv/epic/epicdealblog/quotes-js-project/quotes_js_scraper

class QuotesSpider(scrapy.Spider):
    name = 'nordstrom'
    allowed_domains = ['www.nordstrom.com']
    start_urls = ["https://www.nordstrom.com/s/vitamin-enriched-face-base-priming-moisturizer-duo-132-value/7396982?origin=category-personalizedsort&breadcrumb=Home%2FAnniversary%20Sale%2FAll%20Anniversary&color=000"]
    
    def start_requests(self):
        url = 'https://www.nordstrom.com/s/vitamin-enriched-face-base-priming-moisturizer-duo-132-value/7396982?origin=category-personalizedsort&breadcrumb=Home%2FAnniversary%20Sale%2FAll%20Anniversary&color=000'
        yield SplashRequest(url, callback=self.parse)
        
    def parse(self, response):
        print(response.text)
