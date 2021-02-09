# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BrefItem(scrapy.Item):
    year = scrapy.Field()
    name = scrapy.Field()
    team = scrapy.Field()
    points = scrapy.Field()
    first_place_votes = scrapy.Field()
    vote_share = scrapy.Field()
    league = scrapy.Field()
    at_bats = scrapy.Field()
    home_runs = scrapy.Field()
    sb = scrapy.Field()
    obp = scrapy.Field()
    slg = scrapy.Field()
    ops = scrapy.Field()
    walks = scrapy.Field()
    rbi = scrapy.Field()
    runs = scrapy.Field()
    average = scrapy.Field()
    wins = scrapy.Field()
    era = scrapy.Field()
    war = scrapy.Field()
    saves = scrapy.Field()
    innings = scrapy.Field()
    strike_outs = scrapy.Field()
