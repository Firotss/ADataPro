from scrapy.crawler import CrawlerProcess
from spiders.matches import MatchesInfoClass
from scrapy.utils.project import get_project_settings
def startCrawling():

    process = CrawlerProcess(get_project_settings())
    process.crawl(MatchesInfoClass)
    process.start()