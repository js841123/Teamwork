# -*- coding: utf-8 -*-粉底
import scrapy
import datetime
from bs4 import BeautifulSoup
from yahmp.items import YahmpItem

class YahoospiSpider(scrapy.Spider):
    name = "yahoospi"
    #allowed_domains = ["yahoospi.com"]
    start_urls = ['https://tw.mall.yahoo.com/%E8%85%AE%E7%B4%85-%E4%BF%AE%E5%AE%B9%E9%A4%85-%E8%87%89%E9%83%A8%E5%BD%A9%E5%A6%9D-152984790-category.html?.r=1194045916']

    def parse(self, response):
        res = BeautifulSoup(response.body, "lxml")
	for goods in res.select('.Grid-U.Mb-20.Mx-18.Pb-10.Pos-r'):
            #print goods.select('.D-b.EC-C-gray.Mt-10.Mx-12.Fw-b.Lh-16.Ov-h')[0]['href']
            yield scrapy.Request(goods.select('.D-b.EC-C-gray.Mt-10.Mx-12.Fw-b.Lh-16.Ov-h')[0]['href'],callback=self.parse_detail1)
    def parse_detail1(self, response):
        res = BeautifulSoup(response.body, "lxml")
	item = YahmpItem()
	item['name'] = res.select('h1')[0].text
        item['ID'] = res.select('span[itemprop="productID"]')[0].text
	abc = res.select('[name=keywords],content')[0]['content']
	item['tag'] = abc
        item['price'] = res.select('.price')[0].text
        #item['rate'] = res.select('.store')[0].text
	item['date'] = datetime.datetime.now().strftime("%Y-%m-%d")
	urls = res.select('img[class="main-image current"]')[0]['src']
	item['image_urls'] = urls
	item['shop'] = res.select('.tit-word h2')[0].text
        return item
