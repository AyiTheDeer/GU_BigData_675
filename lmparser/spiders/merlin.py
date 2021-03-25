import scrapy
from scrapy.http import HtmlResponse
from lmparser.items import LmparserItem
from scrapy.loader import ItemLoader


class MerlinSpider(scrapy.Spider):
    name = 'merlin'
    allowed_domains = ['leroymerlin.ru']
    start_urls = [
        'https://leroymerlin.ru/catalogue/vhodnye-dveri/'
    ]

    def parse(self, response: HtmlResponse):
        links = response.xpath("//a[contains(@class, 'item__info')]/@href").extract()
        print()
        for link in links:
            print()
            yield response.follow(link, callback=self.parse_item)

        # next_page = response.xpath('//a[contains(@class, "next-paginator-button")]/@href').get()
        # if next_page:
        #     yield response.follow(next_page, callback=self.parse)

        pass

    def parse_item(self, response: HtmlResponse):
        loader = ItemLoader(item=LmparserItem(), response=response)
        link = response.url
        loader.add_xpath('name', '//h1/text()')
        loader.add_xpath('price', '//span[@slot="price"]/text()')
        loader.add_xpath('params',
                         '//dt[contains(@class, "term")]/text() | //dd[contains(@class, "definition")]/text()')
        loader.add_xpath('photos',
                         '//img[contains(@alt, "product image")]//@src')
        print()
        yield LmparserItem(loader.load_item(), link=link)