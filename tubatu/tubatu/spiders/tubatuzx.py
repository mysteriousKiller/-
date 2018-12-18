# -*- coding: utf-8 -*-
import scrapy
from tubatu.items import TubatuItem

class TubatuzxSpider(scrapy.Spider):
    name = 'tubatuzx'
    url = 'http://fs.to8to.com/company/list_'
    yeshu = 1
    start_urls = [url + str(yeshu) + '.html']
    # -- http://fs.to8to.com/company/list_4.html --

    def parse(self, response):
        ss = TubatuItem()
        quan = response.xpath('//ul[@class="company-data-list"]/li')
        # print(quan[1])
        # print('-------------------------------------')
        # items = []
        for sj in quan:
            ss = TubatuItem()
            name = sj.xpath('./a/div[2]/p[1]/span/text()').extract()[0]
            ss['name'] = name.strip()
        #     # name = sj.xpath('./li/a/div[2]/p[1]/span/text()').extract()
            if len(sj.xpath('./a/div[2]/p[2]/text()').extract()):
                # dianhua = sj.xpath('./li/a/div[2]/p[2]/text()').extract()
                ss['dianhua'] = sj.xpath('./a/div[2]/p[2]/text()').extract()[0]
            else:
                dianhua = ''
                ss['dianhua'] =' '

            # ss['name'] = name[0]
            # ss['dianhua'] = dianhua[0]
            # items.append(ss)

            # print(name,dianhua)
            # print(ss)
            yield ss

        if self.yeshu < 4:
            self.yeshu += 1
            url = self.url+str(self.yeshu)+'.html'
            print('>>>>>>>>>>>>>>>'+ url + '<<<<<<<<<<')
            yield scrapy.Request(url,callback=self.parse)




