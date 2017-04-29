import scrapy
#import datetime
from bs4 import BeautifulSoup
from yahoo1.items import Yahoo1Item

class AppleCrawler(scrapy.Spider):
    name ='Yahoo1'
    start_urls = ['https://tw.mall.yahoo.com/2144872329-category.html','https://tw.mall.yahoo.com/2144420544-category.html','https://tw.mall.yahoo.com/152982145-category.html','https://tw.mall.yahoo.com/2144420546-category.html','https://tw.mall.yahoo.com/152982310-category.html']
    def parse(self, response):
        res = BeautifulSoup(response.body, "lxml")
        for news in res.select('.Fz-s'):
	    #print news.select('a')[0].text
	    #print news.select('a')[0]['href']
            yield scrapy.Request(news.select('a')[0]['href'],self.parse_detail1)

    def parse_detail1(self, response):
        res = BeautifulSoup(response.body, "lxml")
	for goods in res.select('.Grid-U.Mb-20.Mx-18.Pb-10.Pos-r'):
            #print goods.select('.D-b.EC-C-gray.Mt-10.Mx-12.Fw-b.Lh-16.Ov-h')[0]['href']
            yield scrapy.Request(goods.select('.D-b.EC-C-gray.Mt-10.Mx-12.Fw-b.Lh-16.Ov-h')[0]['href'],self.parse_detail2)

    def parse_detail2(self, response):
        res = BeautifulSoup(response.body, "lxml")
        #print res.select('h1')[0].text
	ex1item = Yahoo1Item()
	ex1item['name'] = res.select('h1')[0].text
        ex1item['ID'] = res.select('span[itemprop="productID"]')[0].text
	abc = res.select('[name=keywords],content')[0]['content']
	#abclist = abc.split(',')
	#ex1item['tag'] = abclist
	ex1item['tag'] = abc
        ex1item['price'] = res.select('.price')[0].text
        ex1item['rate'] = res.select('.store')[0].text
	ex1item['date'] = '2017-04-27'
	urls = res.select('img[class="main-image current"]')[0]['src']
	ex1item['image_urls'] = urls
        return ex1item

