# -*- coding: utf-8 -*-
import scrapy
import datetime
from bs4 import BeautifulSoup
from yshop.items import YshopItem

class Yahoo3shopSpider(scrapy.Spider):
    name = "yahoo3shop"
    #allowed_domains = ["yahoo3shop.com"]
    start_urls = ['https://tw.mall.yahoo.com/search?m=list&sid=s3&ccatid=242&s=-sc_salerank&view=image&path=197%2C242&b=0','https://tw.mall.yahoo.com/search?m=list&sid=s3&ccatid=242&s=-sc_salerank&view=image&path=197%2C242&b=48','https://tw.mall.yahoo.com/search?m=list&sid=s3&ccatid=242&s=-sc_salerank&view=image&path=197%2C242&b=96','https://tw.mall.yahoo.com/search?m=list&sid=s3&ccatid=242&s=-sc_salerank&view=image&path=197%2C242&b=144']
    def parse(self, response):
        res = BeautifulSoup(response.body, "lxml")
	#print res.text
	#print response.text
	for news in res.select('p[class="desc"]'):
	    #print news.select('a')[0]['title']
	    #print news.select('a')[0]['href']
	    yield scrapy.Request(news.select('a')[0]['href'],self.parse_detail)
    def parse_detail(self, response):
	res = BeautifulSoup(response.body)
	item = YshopItem()
	item['name'] = res.select('h1')[0].text
        item['ID'] = res.select('span[itemprop="productID"]')[0].text
	abc = res.select('[name=keywords],content')[0]['content']
	item['tag'] = abc
        item['price'] = res.select('.price')[0].text
        item['rate'] = res.select('.store-sup')[0].text
	item['date'] = datetime.datetime.now().strftime("%Y-%m-%d")
	urls = res.select('img[class="main-image current"]')[0]['src']
	item['image_urls'] = urls
        return item
	
	
