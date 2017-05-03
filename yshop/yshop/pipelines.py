# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class YshopPipeline(object):
    def open_spider(self, spider):
	self.conn = sqlite3.connect('yahoo.sqlite')
	self.cur = self.conn.cursor()
	self.cur.execute('create table if not exists yshop_86(name varchar(1000), ID varchar(1000), price varchar(1000), rate varchar(1000), tag varchar(3000), date text,image_urls text,shop text)')
	#pass     
    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()
        #pass
    def process_item(self, item, spider):
	col = ','.join(item.keys())
        placeholders = ','.join(len(item) * '?')
        sql = 'insert into yshop_86({}) values({})'
	self.cur.execute(sql.format(col, placeholders), item.values())
        return item
