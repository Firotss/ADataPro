import scrapy
from project.items import ProjectItem

class TeamSpider(scrapy.Spider):
    name = "team"
    allowed_domains = ["dota2.fandom.com"]
    start_urls = ["https://dota2.fandom.com/wiki/Professional_teams"]

    def nextParse(self, response, url):
        start_urls = ["https://dota2.fandom.com"+url]
        return scrapy.Request("""//*[@id="mw-content-text"]/div/table[1]/tbody/tr[3]/td""",
                          callback=self.parse_page2)

    def parse(self, response):
        #item = ProjectItem()
        #for l in response.xpath("""//*[@class="product"]"""):
        #    item = {
        #        "title": l.xpath(""".//div[@class="title"]//span/text()""").get(),
        #        "rating": float(
        #            l.xpath(""".//div[@class="rating col-md-9"]//span/text()""")
        #            .get()
        #            .replace("(", "")
        #            .replace(")", "")
        #        ),
        #        "parameters": [i.get() for i in l.xpath(""".//ul/li/text()""")],
        #        "price": float(
        #            l.xpath(""".//span[@class="price-num"]/text()""").get()
        #            + "."
        #            + l.xpath(""".//span[@class="price-num"]//sup/text()""").get()
        #        ),
        #    }
        #    yield item
        item = ProjectItem()
        for l in response.xpath("""//*[@class="mw-parser-output"]/div"""):
            item = {
                    "title": l.xpath("""//*[@class="teambox"]/div/a/text()""").get(),
                    "logo": l.xpath("""//*[@class="teambox"]/div/a/img/@src""").get(),
                    "country": self.nextParse(response.xpath(response, """//*[@class="teambox"]/div/a/@href"""))
            }
        yield item
    
   