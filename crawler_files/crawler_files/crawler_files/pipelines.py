# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import sqlite3

class CrawlerFilesPipeline:
    def __init__(self):
        self.connection = sqlite3.connect('../../db.sqlite3')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
  
        self.cursor.execute(
            """INSERT INTO matches_matches (team1_name, team2_name, date_match) values (?, ?, ?)""",
            (item['Team1'], item['Team2'], item['Date']),
        )
        self.connection.commit()
        return item