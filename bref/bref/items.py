# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BrefItem(scrapy.Item):
    year = scrapy.Field()
    name = scrapy.Field()
    points = scrapy.Field()
