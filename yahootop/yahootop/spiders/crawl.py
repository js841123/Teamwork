import scrapy
from bs4 import BeautifulSoup
from yahootop.items import YahootopItem

class TopCrawler(scrapy.Spider):
    name ='yahootop'
    start_urls = ['https://tw.promo.yahoo.com/2015store/topranking/#cat=category_4']
    def parse(self, response):
        res = BeautifulSoup(response.body)
	exp = res.select('.mall_list')[3]
	#print exp.select('.up')
        for news in exp.select('li'):
	    print news.select('.tit')[0].text
	    print news.select('.stor')[0].text
	    print news.select('.saleout')[0].text
	    print news.select('.price')[0].text
	    print news.select('i')[0]['class'][0]
