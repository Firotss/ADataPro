# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MatchesInfo(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    team1 = scrapy.Field()
    team2 = scrapy.Field()
    date = scrapy.Field()
    year_of_season = scrapy.Field()
    matchID = scrapy.Field()
    img_team1 = scrapy.Field()
    img_team2 = scrapy.Field()
    
class RankingInfo(scrapy.Item):
    matchID = scrapy.Field()
    team_name = scrapy.Field()
    wins = scrapy.Field()
    losses = scrapy.Field()
    draws = scrapy.Field()
    points = scrapy.Field()
    year_of_season = scrapy.Field()
    img = scrapy.Field()

