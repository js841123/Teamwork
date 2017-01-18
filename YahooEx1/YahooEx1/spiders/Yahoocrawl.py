import scrapy
from bs4 import BeautifulSoup
from YahooEx1.items import Yahooex1Item

class AppleCrawler(scrapy.Spider):
    name ='YahooEx1'
    start_urls = ['https://tw.mall.yahoo.com/2144872365-category.html?img_only=0&sort_by=%5Brank%5D&order_by=0','https://tw.mall.yahoo.com/2144872356-category.html?img_only=0&sort_by=%5Brank%5D&order_by=0','https://tw.mall.yahoo.com/2144872335-category.html?img_only=0&sort_by=%5Brank%5D&order_by=0','https://tw.mall.yahoo.com/979412458-category.html?img_only=0&sort_by=%5Brank%5D&order_by=0','https://tw.mall.yahoo.com/2144872545-category.html?img_only=0&sort_by=%5Brank%5D&order_by=0']
    def parse(self, response):
        res = BeautifulSoup(response.body)
        for news in res.select('.P-18'):
            yield scrapy.Request(news.select('a')[0]['href'],self.parse_detail)            

    def parse_detail(self, response):
        res = BeautifulSoup(response.body)
        ex1item = Yahooex1Item()
        ex1item['product'] = res.select('h1')[0].text
        ex1item['ID'] = res.select('span[itemprop="productID"]')[0].text
        ex1item['span'] = res.select('.price')[0].text
        ex1item['point'] = res.select('.store')[0].text
        return ex1item
        #print res.select('h1')[0].text
        #print res.select('.price')[0].text,res.select('.store')[0].text
