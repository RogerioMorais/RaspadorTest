# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose, Join,Identity
from scrapy.loader import ItemLoader

class ProdutoItem(scrapy.Item):
    id = scrapy.Field()
    breadcrumb = scrapy.Field()
    name = scrapy.Field()
    img = scrapy.Field()
    seller = scrapy.Field()
    price = scrapy.Field()
    picture = scrapy.Field()
    
class ProdutoItemLoader(ItemLoader):
    def format_price(param):
        return param.replace('R$ ','').replace(',','.')

    def set_array_value(self,value):
      outcome=""
      for x in value:
          if outcome!="":
              outcome+=","
          outcome+=x
      return '['+outcome+']'


    default_input_processor = TakeFirst()
    default_output_processor = TakeFirst()
    price_in = MapCompose(format_price)
    breadcrumb_in = set_array_value