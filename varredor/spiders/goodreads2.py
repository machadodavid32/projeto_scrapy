import scrapy
from scrapy.loader import ItemLoader
from varredor.items import CitacaoItem



class GoodReadsSpider(scrapy.Spider):  # scrapy.spider para aproveitar as funcionalidades
    # identidade (nome do bot)
    name = 'botteste'
    # request
    def start_requests(self):
        urls = ['https://www.goodreads.com/quotes?page=1']  # reparar que eu peguei o primeiro link, da primeira pagina
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) 
    
    # Response
    def parse(self, response):
        for elemento in response.xpath("//div[@class='quote']"):
            loader = ItemLoader(item=CitacaoItem(),
                                selector=elemento, response=response)
            loader.add_xpath('frase', ".//div[@class='quoteText']/text()")
            loader.add_xpath('autor', ".//span[@class='authorOrTitle']/text()")
            loader.add_xpath('tags', "//div[@class='greyText smallText left']/text()")
            yield loader.load_item()
            
            
        prox_pag = response.xpath("//a[@class='next_page']/@href").get().split('=')[1]
        print('#'*10) # Isso é para mostrar no terminal, de forma clara, se as paginas estão realmente sendo acessadas.
        print(prox_pag)
        print('#'*20)
        if prox_pag is not None:
            full_next_page = f'https://www.goodreads.com/quotes?page={prox_pag}'
            print('#'*20)
            print(full_next_page)
            print("#"*20)
            yield scrapy.Request(url=full_next_page, callback=self.parse)
        
                
                
                