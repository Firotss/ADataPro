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
        matchdb = self.cursor.execute("""SELECT * FROM matches_matches""")
        check = 0
        for i in matchdb:
            if i[3] == item['Date'] and i[2] == item['Team2'] and i[1] == item['Team1']:
                print("-------------------------")
                print(i[1], item['Team1'])
                print(i[2], item['Team2'])
                print(i[3], item['Date'])
                print("-------------------------")
                check = i[0]
        if(check == 0):
            self.cursor.execute(
                """INSERT INTO matches_matches (team1_name, team2_name, date_match) values (?, ?, ?)""",
                (item['Team1'], item['Team2'], item['Date']),
            )
            
        else:
            self.cursor.execute(
                """UPDATE matches_matches SET team1_name = ?, team2_name = ?, date_match = ? WHERE id = ?""",
                (item['Team1'], item['Team2'], item['Date'], check),
            )
        self.connection.commit()
        return item