import scrapy

class ProxyScraperSpider(scrapy.Spider):
    # Identidade
    name = 'proxyscraper'
    # Request
    def start_requests(self):
        urls = ['https://www.us-proxy.org/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    # Response
            