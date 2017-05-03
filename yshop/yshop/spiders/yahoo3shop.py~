# -*- coding: utf-8 -*-#小三，86
import scrapy
import datetime
from bs4 import BeautifulSoup
from yshop.items import YshopItem

class Yahoo3shopSpider(scrapy.Spider):
    name = "yahoo3shop"
    #allowed_domains = ["yahoo3shop.com"]
    start_urls = ['https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=0','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=48','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=96','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=144','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=192','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=240','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=288','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=336','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=384','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=432','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=480','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=528','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=576','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=624','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=672','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=720','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=768','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=816','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=864','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=912','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=960','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=1008','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=1056','https://tw.mall.yahoo.com/search?m=list&sid=86shops&ccatid=9&s=-sc_salerank&view=image&path=9&b=1104']
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
	item['shop'] = res.select('.tit-word h2')[0].text
        return item
	
	
