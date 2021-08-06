import scrapy
try:
    from items import MatchesInfo, RankingInfo
    from pipelines import CrawlerFilesPipeline
except:
    from ..items import MatchesInfo, RankingInfo
    from ..pipelines import CrawlerFilesPipeline

class MatchesInfoClass(scrapy.Spider):

    name = "MatchesInfo"
    allowed_domains = ["openligadb.de"]
    start_urls = []                                     

    def parse(self, response):
        year = response.url[-4:]
        item = MatchesInfo()
        jsonresponse = response.json()

        for allMatches in jsonresponse:
            item["matchID"] = allMatches["matchID"]
            item["year_of_season"] = year
            item["team1"] = allMatches["team1"]["teamName"]
            item["team2"] = allMatches["team2"]["teamName"]
            item["date"] = allMatches["matchDateTime"]
            item["img_team1"] = allMatches["team1"]["teamIconUrl"]
            item["img_team2"] = allMatches["team2"]["teamIconUrl"]
            print("- - - - - - - - - - - - - - - - - - - -")
            print(item)
            print("- - - - - - - - - - - - - - - - - - - -")
            
            if allMatches['matchIsFinished'] == True:
                extended_item = RankingInfo()

                extended_item["matchID"] = allMatches["matchID"]
                extended_item["points"] = allMatches["matchResults"][0]['pointsTeam1']
                extended_item["team_name"] = allMatches["team1"]["teamName"]
                extended_item["img"] = allMatches["team1"]["teamIconUrl"]
                extended_item["year_of_season"] = year
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
                extended_item["img"] = allMatches["team2"]["teamIconUrl"]
                yield CrawlerFilesPipeline.process_extended_item(self, extended_item, scrapy.Spider)

            yield CrawlerFilesPipeline.process_item(self, item, scrapy.Spider)