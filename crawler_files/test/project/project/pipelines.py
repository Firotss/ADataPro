# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class ProjectPipeline:
    def __init__(self):
        self.connection = sqlite3.connect("./teams.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS TeamsTable(
                id INTEGER PRIMARY KEY,
                title VARCHAR(255),
                logo VARCHAR(255),
                country VARCHAR(255)
            )
            """)
        

    def process_item(self, item, spider):
  
        self.cursor.execute(
            """INSERT INTO TeamsTable (title, logo, country) values (?, ?, ?)""",
            (item['title'], item['logo'], item['country']),
        )
        self.connection.commit()
        return item
