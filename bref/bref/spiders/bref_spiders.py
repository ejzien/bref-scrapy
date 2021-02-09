# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from bref.items import BrefItem
import re


class BrefSpider(Spider):
    name = 'bref_spider'
    allowed_urls = ['https://www.baseball-reference.com/awards/awards_2019.shtml']
    start_urls = ['https://www.baseball-reference.com']
    def parse(self, response):
        base_url = '//*[@id="div_AL_MVP_voting"]/table/tbody/tr'
        end_url = '/td'

        #base_url = '//*[@id="default"]/div/div/div/aside/div/ul/li/ul/li/a'
        #end_url = './text()'

        rows = response.xpath('//*[@id="div_AL_MVP_voting"]/table/tbody/tr')
        print('--------------------------------this--------------------------------')
        print(len(rows))
        print(type(rows))
        print(rows)
        print('--------------------------------that--------------------------------')
        for row in rows:
            print('--------------------------------new row--------------------------------')
            #row.xpath(end_url)

            item = BrefItem()
            #print('-----------------------------------------------------------------')
            item['year'] = 2019
            item['name'] = 'Mike Trout'
            item['points'] = 355
            #print('-----------------------------------------------------------------')

            yield item

    #   # Find all the table rows
    #   rows = response.xpath('//*[@id="mw-content-text"]/div/table/tbody/tr')
        
    #   # The movie title could be of different styles so we need to provide all the possibilities.
    #   patterns = ['./td[1]/i/a/text()', './td[1]/i/b/a/text()', './td[1]/i/span[2]//text()', './td[1]/i/b/span/text()']
    #   for row in rows:
    #       # extract() will return a Python list, extract_first() will return the first element in the list
    #       # If you know the first element is what you want, you can use extract_first()
    #       for pattern in patterns:
    #           film = row.xpath(pattern).extract_first()
    #           if film:
    #               break
    #       # If the movie title is missing, then we just skip it.
    #       if not film:
    #           continue
    #       # Relative xpath for all the other columns
    #       year = row.xpath('./td[2]/a/text()').extract_first()
    #       awards = row.xpath('./td[3]/text()').extract_first()
    #       nominations = row.xpath('./td[4]/text()').extract_first().strip()

    #       is_best_picture = bool(row.xpath('./@style'))
    #       # Initialize a new WikiItem instance for each movie.
    #       item = WikiItem()
    #       item['film'] = film
    #       item['year'] = year
    #       item['awards'] = awards
    #       item['nominations'] = nominations
    #       item['is_best_picture'] = is_best_picture

    #       yield item
