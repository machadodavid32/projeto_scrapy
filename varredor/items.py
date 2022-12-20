# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join

def tirar_espaco_branco(valor):
    return valor.strip()

def processar_caracteres_especiais(valor):
    return valor.replace(u"\u201c", '').replace(u"\201d", '').replace(u"\u2014", '-').replace(u"\u2019", '')

def letras_maiusculas(valor):
    return valor.upper()

class CitacaoItem(scrapy.Item):
    frase = scrapy.Field(
        
        input_processor=MapCompose(tirar_espaco_branco, processar_caracteres_especiais),
        output_processor=TakeFirst() # TakeFirst retorna o primeiro item
    )
    
    autor = scrapy.Field(     
    input_processor=MapCompose(letras_maiusculas),
        output_processor=TakeFirst()   
    )
    
    tags = scrapy.Field(
        output_processor=Join(';'), # Aqui será usado para pegar as tags do site e separar somente via virgula
        
    )
    