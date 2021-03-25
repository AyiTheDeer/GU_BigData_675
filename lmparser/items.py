# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class LmparserItem(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    photos = scrapy.Field()
    params = scrapy.Field()
    link = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst())
    _id = scrapy.Field()
    pass
