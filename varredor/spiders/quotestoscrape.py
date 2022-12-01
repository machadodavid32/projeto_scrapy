import scrapy

class QuotesToScrapeSpider(scrapy.Spider):  # scrapy.spider para aproveitar as funcionalidades
    # identidade (nome do bot)
    name = 'meubot'
    # request
    def start_requests(self):
        urls = ['https://quotes.toscrape.com']
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)  # yield serve para retornar diretamente para o site (se tivesse mais que um, sem o yield, ele sempre iria passar em todos os sites)
            # callback=self.parse vai referenciar a função self.parse que iremos criar abaixo e tem a função de extrair os dados dentro de uma pagina sempre que for solicitada
    
    # Response
    def parse(self, response):
        # Aqui é onde vc deve processar o que é retornada da response
        with open('pagina.html', 'wb') as arquivo:
            arquivo.write(response.body)