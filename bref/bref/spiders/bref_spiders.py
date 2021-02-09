# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from bref.items import BrefItem
import re


class BrefSpider(Spider):
    name = 'bref_spider'
    allowed_urls = ['https://www.baseball-reference.com']
    start_urls = ['https://www.baseball-reference.com/awards/awards_2019.shtml']
    # def parse(self, response):
    #     years = [2017,2018,2019]

    #     for year in years:
    #         base_url = '//*[@id="div_AL_MVP_voting"]/table/tbody/tr'
    #         end_url = '/td'

    #         rows = response.xpath('//*[@id="div_AL_MVP_voting"]/table/tbody/tr')
    #         for row in rows:
    #             #row.xpath(end_url)

    #             item = BrefItem()
    #             item['year'] = 2019
    #             item['name'] = row.xpath('./td[1]').extract_first().split('csk="')[-1].split('"')[0]
    #             item['team'] = row.xpath('./td[2]/text()').extract_first()
    #             item['points'] = row.xpath('./td[3]/text()').extract_first()

    #             yield item


    def parse(self, response):
        #years = [2017,2018,2019]
        years = list(range(1950,2020))
        years = [2017,2018,2019]

        for year in years:
            url = 'https://www.baseball-reference.com/awards/awards_%s.shtml' % year
            yield Request(url=url, callback=self.parse_result_page,meta={'year': year})


    def parse_result_page(self, response):
    
        for league in ['AL','NL']:

            base_url = '//*[@id="div_%s_MVP_voting"]/table/tbody/tr' % league
            end_url = '/td'

            rows = response.xpath(base_url)
            for row in rows:
                item = BrefItem()
                item['year'] = response.meta['year']
                item['league'] = league
                item['name'] = row.xpath('./td[1]').extract_first().split('csk="')[-1].split('"')[0]
                item['team'] = row.xpath('./td[2]/text()').extract_first()
                item['points'] = row.xpath('./td[3]/text()').extract_first()
                yield item







