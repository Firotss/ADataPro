# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import logging
import sqlite3

class CrawlerFilesPipeline:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS AllMatches(Team1 TEXT, Team2 TEXT, date TEXT)")

    def process_item(self, item, spider):
  
        self.cursor.execute(
            """INSERT INTO AllMatches (Team1, Team2, date) values (?, ?, ?)""",
            (item['Team1'], item['Team2'], item['Date']),
        )
        self.connection.commit()
        return item