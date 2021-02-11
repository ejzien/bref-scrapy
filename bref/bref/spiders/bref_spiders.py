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
        years = list(range(1950,2020))
        #years = [2017,2018,2019]

        for year in years:
            url = 'https://www.baseball-reference.com/awards/awards_%s.shtml' % year
            yield Request(url=url, callback=self.parse_result_page,meta={'year': year})


    def parse_result_page(self, response):
    
        for league in ['AL','NL']:

            base_url = '//*[@id="div_%s_MVP_voting"]/table/tbody/tr' % league
            end_url = '/td'

            rows = response.xpath(base_url)
            count = 1
            for row in rows:
                item = BrefItem()
                item['year'] = response.meta['year']
                item['league'] = league
                item['voting_place'] = int(row.xpath('./th/text()').get())
                item['team'] = row.xpath('./th[0]/text()').extract_first()
                item['name'] = row.xpath('./td[1]').extract_first().split('csk="')[-1].split('"')[0]
                item['team'] = row.xpath('./td[2]/text()').extract_first()
                item['points'] = row.xpath('./td[3]/text()').extract_first()
                item['first_place_votes'] = row.xpath('./td[4]/text()').extract_first()
                item['vote_share'] = row.xpath('./td[5]/text()').extract_first()
                item['war'] = row.xpath('./td[6]/text()').extract_first()
                item['at_bats'] = row.xpath('./td[8]/text()').extract_first()
                item['runs'] = row.xpath('./td[9]/text()').extract_first()
                item['home_runs'] = row.xpath('./td[11]/text()').extract_first()
                item['rbi'] = row.xpath('./td[12]/text()').extract_first()
                item['sb'] = row.xpath('./td[13]/text()').extract_first()
                item['walks'] = row.xpath('./td[14]/text()').extract_first()
                item['average'] = row.xpath('./td[15]/text()').extract_first()
                item['obp'] = row.xpath('./td[16]/text()').extract_first()
                item['slg'] = row.xpath('./td[17]/text()').extract_first()
                item['ops'] = row.xpath('./td[18]/text()').extract_first()
                item['wins'] = row.xpath('./td[19]/text()').extract_first()
                item['era'] = row.xpath('./td[21]/text()').extract_first()
                item['saves'] = row.xpath('./td[25]/text()').extract_first()
                item['innings'] = row.xpath('./td[26]/text()').extract_first()
                item['strike_outs'] = row.xpath('./td[30]/text()').extract_first()
                yield item







