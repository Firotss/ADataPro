import scrapy

from items import MatchesInfo, RankingInfo
from datetime import datetime
from pipelines import CrawlerFilesPipeline
class MatchesInfoClass(scrapy.Spider):

    name = "MatchesInfo"
    allowed_domains = ["openligadb.de"]
    url = "https://api.openligadb.de/getmatchdata/bl1/2020" #Актуална година + str(datetime.now().year)
    start_urls = [url]

    def parse(self, response):
        item = MatchesInfo()
        jsonresponse = response.json()

        for allMatches in jsonresponse:
            item["team1"] = allMatches["team1"]["teamName"]
            item["team2"] = allMatches["team2"]["teamName"]
            item["date"] = allMatches["matchDateTime"]
            print("- - - - - - - - - - - - - - - - - - - -")
            print(item)
            print("- - - - - - - - - - - - - - - - - - - -")
            try:
                extended_item = RankingInfo()

                extended_item["matchID"] = allMatches["matchID"]
                extended_item["points"] = allMatches["matchResults"][0]['pointsTeam1']
                extended_item["team_name"] = allMatches["team1"]["teamName"]

                team2_result_wins = '0'
                team2_result_losses = '0'
                team2_result_draws = '0'

                extended_item["losses"] = "0"
                extended_item["draws"] = "0"
                extended_item["wins"] = "0"

                if extended_item["points"] > allMatches["matchResults"][0]['pointsTeam2']:
                    team2_result_losses = "1"
                    extended_item["wins"] = "1"

                elif extended_item["points"] < allMatches["matchResults"][0]['pointsTeam2']:
                    team2_result_wins = "1"
                    extended_item["losses"] = "1"

                else:
                    team2_result_draws = "1"
                    extended_item["draws"] = "1"

                yield CrawlerFilesPipeline.process_extended_item(self, extended_item, scrapy.Spider)

                extended_item["points"] = allMatches["matchResults"][0]['pointsTeam2']
                extended_item["team_name"] = allMatches["team2"]["teamName"]
                extended_item["wins"] = team2_result_wins
                extended_item["losses"] = team2_result_losses
                extended_item["draws"] = team2_result_draws

                yield CrawlerFilesPipeline.process_extended_item(self, extended_item, scrapy.Spider)

            except:
                print("no results",allMatches["matchID"])
            yield CrawlerFilesPipeline.process_item(self, item, scrapy.Spider)