# -*- coding: utf-8 -*-
import scrapy
from raspador.items import ProdutoItem,ProdutoItemLoader


class ProdutoSpider(scrapy.Spider):
    name="produtospider"
    allowed_domains = ['www.americanas.com.br']
    start_urls=["https://www.americanas.com.br/produto/134186808"]

    def parse(self,response):
        a=ProdutoItemLoader(item=ProdutoItem(),response=response)
        a.add_value('id',response.xpath('//span[contains(text(),"Cód")]/text()')[1].get())
        a.add_css('breadcrumb','div[class^="BreadcrumbContainer"] a span::text')
       # a.add_value('breadcrumb',response.css('div[class^="BreadcrumbContainer"] a span::text').getall())
        a.add_xpath('name',"//*[@id='product-name-default']/text()")
        a.add_value('img',response.css('.gallery-product-video-container img::attr(src)').get())
        a.add_value('seller','americanas.com')
        a.add_value('price',response.css('p[class^="main-offer"] span::text').get())
        return a.load_item()