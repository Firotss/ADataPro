from scrapy.crawler import CrawlerProcess
from spiders.matches import MatchesInfoClass
from scrapy.utils.project import get_project_settings

def start_crawling():
    process = CrawlerProcess(get_project_settings())
    process.crawl(MatchesInfoClass)
    process.start()