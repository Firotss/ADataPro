# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# # useful for handling different item types with a single interface
# from datetime import datetime
# import sqlite3

# class CrawlerFilesPipeline:
#     def __init__(self):
#         self.open_spider()
#         self.cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_match_team ON matches_teamsinfo(matchID, team_name)")
#         self.cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_matchID_matches ON matches_matches(matchID)")
#         self.connection.commit()
        
#     def open_spider(self):
#         self.connection = sqlite3.connect('db.sqlite3')
#         self.cursor = self.connection.cursor()
        
#         self.cursor.execute("PRAGMA journal_mode=WAL;")
#         self.cursor.execute("PRAGMA synchronous=NORMAL;")
#         self.connection.commit()

#     def close_spider(self):
#         self.connection.commit()
#         self.connection.close()

#     def process_item(self, item, spider):
#         self.cursor.execute("""
#             INSERT INTO matches_matches (team1_name, team2_name, date_match, year, matchID, img_link_team1, img_link_team2)
#             VALUES (?, ?, ?, ?, ?, ?, ?)
#             ON CONFLICT(matchID) DO UPDATE SET
#                 team1_name=excluded.team1_name,
#                 team2_name=excluded.team2_name,
#                 date_match=excluded.date_match
#         """, (item['team1'], item['team2'], item['date'], item['year_of_season'], item['matchID'], item['img_team1'], item['img_team2']))
#         self.connection.commit()

#     def process_extended_item(self, item, spider):
#         self.cursor.execute("""
#             INSERT INTO matches_teamsinfo (matchID, team_name, wins, losses, draws, points, date, img_link_team)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#             ON CONFLICT(matchID, team_name) DO UPDATE SET
#                 wins=excluded.wins,
#                 losses=excluded.losses,
#                 draws=excluded.draws,
#                 points=excluded.points,
#                 img_link_team=excluded.img_link_team
#         """, (item['matchID'], item['team_name'], item['wins'], item['losses'], item['draws'], item['points'], item['year_of_season'], item['img']))
#         self.connection.commit()