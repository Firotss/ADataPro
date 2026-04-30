import scrapy

try:
    from items import MatchesInfo, RankingInfo
except ImportError:
    from ..items import MatchesInfo, RankingInfo

class MatchesInfoClass(scrapy.Spider):
    name = "MatchesInfo"
    allowed_domains = ["openligadb.de"]
    start_urls = [] 

    def parse(self, response):
        year = response.url[-4:]
        jsonresponse = response.json()

        for allMatches in jsonresponse:
            item = MatchesInfo()
            item["matchID"] = allMatches["matchID"]
            item["year_of_season"] = year
            item["team1"] = allMatches["team1"]["teamName"]
            item["team2"] = allMatches["team2"]["teamName"]
            item["date"] = allMatches["matchDateTime"]
            item["img_team1"] = allMatches["team1"]["teamIconUrl"]
            item["img_team2"] = allMatches["team2"]["teamIconUrl"]
            
            yield item

            if allMatches.get('matchIsFinished') and allMatches.get("matchResults"):
                
                results = allMatches["matchResults"][0]
                points_team1 = results['pointsTeam1']
                points_team2 = results['pointsTeam2']

                extended_item_t1 = RankingInfo()
                extended_item_t2 = RankingInfo()

                extended_item_t1["matchID"] = extended_item_t2["matchID"] = allMatches["matchID"]
                extended_item_t1["year_of_season"] = extended_item_t2["year_of_season"] = year
                
                extended_item_t1["team_name"] = allMatches["team1"]["teamName"]
                extended_item_t1["img"] = allMatches["team1"]["teamIconUrl"]
                extended_item_t1["points"] = points_team1

                extended_item_t2["team_name"] = allMatches["team2"]["teamName"]
                extended_item_t2["img"] = allMatches["team2"]["teamIconUrl"]
                extended_item_t2["points"] = points_team2

                extended_item_t1["wins"] = extended_item_t1["losses"] = extended_item_t1["draws"] = "0"
                extended_item_t2["wins"] = extended_item_t2["losses"] = extended_item_t2["draws"] = "0"

                if points_team1 > points_team2:
                    extended_item_t1["wins"] = "1"
                    extended_item_t2["losses"] = "1"
                elif points_team1 < points_team2:
                    extended_item_t1["losses"] = "1"
                    extended_item_t2["wins"] = "1"
                else:
                    extended_item_t1["draws"] = "1"
                    extended_item_t2["draws"] = "1"

                yield extended_item_t1
                yield extended_item_t2