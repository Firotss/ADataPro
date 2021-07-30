# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MatchesInfo(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Team1 = scrapy.Field()
    Team2 = scrapy.Field()
    #Result = scrapy.Field()
    #Date = scrapy.Field()
    
    pass
