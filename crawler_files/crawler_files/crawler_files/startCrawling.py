from datetime import datetime
from scrapy.crawler import CrawlerProcess
from spiders.matches import MatchesInfoClass
from scrapy.utils.project import get_project_settings

def start_crawling():
    process = CrawlerProcess(get_project_settings())

    date_now = int(datetime.now().year)

    while (date_now >= 2002):
        MatchesInfoClass.start_urls.append("https://api.openligadb.de/getmatchdata/bl1/" + str(date_now))
        date_now = date_now - 1 #update на всичко

    #MatchesInfoClass.start_urls.append("https://api.openligadb.de/getmatchdata/bl1/" + str(date_now))
    process.crawl(MatchesInfoClass)
    process.start()
        
    