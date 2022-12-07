import scrapy

# Extrair dados de varias páginas do doogreads.com
# Para isso, utilize no terminal o scrapy shell, exemplo: scrapy shell 'https://www.goodreads.com/quotes?page=1'
# Depois, digite: response.xpath("//a[@class='next_page']/@href").get()
# Este é  resultado: '/quotes?page=2'  Nesta pagina, a unica diferença no link é o número da pagina. Portanto, precisamos apenas do numero da pagina para ir para a proxima pagina
# response.xpath("//a[@class='next_page']/@href").get().split('=')
# ['/quotes?page', '2']
# response.xpath("//a[@class='next_page']/@href").get().split('=')[1]  # o primeiro indice é para a proxima pagina, que no caso é dois. Copie essa linha de comando e cole no codigo do programa
#'2'
#


class GoodReadsSpider(scrapy.Spider):  # scrapy.spider para aproveitar as funcionalidades
    # identidade (nome do bot)
    name = 'meubot3'
    # request
    def start_requests(self):
        urls = ['https://www.goodreads.com/quotes?page=1']  # reparar que eu peguei o primeiro link, da primeira pagina
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)  # yield serve para retornar diretamente para o site (se tivesse mais que um, sem o yield,...
            #...ele sempre iria passar em todos os sites)
            # callback=self.parse vai referenciar a função self.parse que iremos criar abaixo e tem a função de extrair os dados dentro de uma pagina sempre que for solicitada
    
    # Response
    def parse(self, response):
        # Aqui é onde vc deve processar o que é retornada da response
        #with open('pagina.html', 'wb') as arquivo:  anulei essa e a linha abaixo para realizar o procedimento de varrer uma página
         #   arquivo.write(response.body) 
        for elemento in response.xpath("//div[@class='quote']"):
            yield{
                
                'frase': elemento.xpath(".//div[@class='quoteText']/text()").get(),  # para pegar o primeiro elemento. Reparar no ponto antes de //.
                'autor': elemento.xpath(".//span[@class='authorOrTitle']/text()").get(),  # o ponto antes do // significa que queremos aquele conteúdo exato deste local do xptah
                'tags': elemento.xpath(".//div[@class='greyText smallText left']/text()").getall()  # Quero que pegue todas as tags do site
            }
            
            
            
            # Tentar encontrar o botão próximo, se encontrar, vou varrer essas páginas.
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
        
                
                
                