from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess

from lmparser import settings
from lmparser.spiders.merlin import MerlinSpider

if __name__ == "__main__":
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(MerlinSpider)

    process.start()