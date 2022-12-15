import scrapy
from scrapy.loader import ItemLoader  # essa e as importações da linha de baixo foram feitas após concluir os dados do arquivos items.py
from varredor.items import CitacaoItem

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
        #with open('pagina.html', 'wb') as arquivo:  anulei essa e a linha abaixo para realizar o procedimento de varrer uma página
         #   arquivo.write(response.body) 
        for elemento in response.xpath("//div[@class='quote']"):
            yield{
                
                'frase': elemento.xpath(".//span[@class='text']/text()").get(),  # para pegar o primeiro elemento. Reparar no ponto antes de //.
                'autor': elemento.xpath(".//small[@class='author']/text()").get(),  # o ponto antes do // significa que queremos aquele conteúdo exato deste local do xptah
                'tags': elemento.xpath(".//a[@class='tag']/text()").getall()  # Quero que pegue todas as tags do site
            }