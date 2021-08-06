# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from datetime import datetime
import sqlite3

class CrawlerFilesPipeline:
    def __init__(self):
        self.connection = sqlite3.connect('../../db.sqlite3')
        self.cursor = self.connection.cursor()
        

    def process_item(self, item, spider):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()

        match_db = self.cursor.execute("""SELECT * FROM matches_matches""")

        check = 0

        for i in match_db:
            if i[4] == item['matchID']:
                check = i[0]

        if(check == 0):
            self.cursor.execute(
                """INSERT INTO matches_matches (team1_name, team2_name, date_match, year, matchID) values (?, ?, ?, ?, ?)""",
                (item['team1'], item['team2'], item['date'], item['year_of_season'], item['matchID']),
            )
            
        else:
            self.cursor.execute(
                """UPDATE matches_matches SET team1_name = ?, team2_name = ?, date_match = ? WHERE id = ?""",
                (item['team1'], item['team2'], item['date'], check),
            )

        self.connection.commit()
        return item

    def process_extended_item(self, item, spider):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()

        teamsdb = self.cursor.execute("""SELECT * FROM matches_teamsinfo""")

        check = 0

        for i in teamsdb:
            if i[2] == item['team_name'] and i[1] == item['matchID']:
                check = i[0]

        if(check == 0):
            self.cursor.execute(
                """INSERT INTO matches_teamsinfo (matchID, team_name, wins, losses, draws, points, date) values (?, ?, ?, ?, ?, ?, ?)""",
                (item['matchID'], item['team_name'], item['wins'], item['losses'], item['draws'], item['points'], item['year_of_season']),
            )
            
        else:
            self.cursor.execute(
                """UPDATE matches_teamsinfo SET wins = ?, losses = ?, draws = ?, points = ? WHERE id = ?""",
                (item['wins'], item['losses'], item['draws'], item['points'], check),
            )
            
        self.connection.commit()
        return item

    