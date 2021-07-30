import scrapy
from scrapy.exceptions import CloseSpider
from crawler_files.items import MatchesInfo
from datetime import datetime

class MatchesInfoClass(scrapy.Spider):

    name = "MatchesInfo"
    allowed_domains = ["openligadb.de"]
    url = "https://api.openligadb.de/getmatchdata/bl1/" + str(datetime.now().year) #Актуална година
    start_urls = [url]

    def parse(self, response):
        item = MatchesInfo()
        jsonresponse = response.json()

        for allMatches in jsonresponse:
            item["Team1"] = allMatches["team1"]["teamName"]
            item["Team2"] = allMatches["team2"]["teamName"]
            #item["Result"] = 
            print("- - - - - - - - - - - - - - - - - - - -")
            print(item)
            print("- - - - - - - - - - - - - - - - - - - -")
            yield item