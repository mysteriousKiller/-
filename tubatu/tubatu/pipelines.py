# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import csv

class TubatuPipeline(object):
    def __init__(self):
        # self.f = open('yubayu.txt','ab')
        self.f = open('yubayu.csv','a',encoding='utf-8')
        self.mywrite = csv.writer(self.f,delimiter=' ')
        self.mywrite.writerow(['name', 'dianhua'])
    def process_item(self, item, spider):
        name = item['name']
        dianhua = item['dianhua']
        # json = {
        #     "name":name,
        #     "dianhua":dianhua
        # }
        # self.f.write(str(json).encode('utf-8'))
        # self.f.write("\n".encode('utf-8'))
        self.mywrite.writerow([name,dianhua])
        return item
    def cloxe_spider(self,spider):
        self.f.close()
