# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
import os, os.path
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline

MONGO_URL = "localhost:27017"


class LmparserImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item["photos"]:
            for photo_url in item['photos']:
                try:
                    yield scrapy.Request(photo_url)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            item["photos"] = [itm[1] for itm in results]
        return item


class LmparserPipeline:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client['geek_brains']

    def process_item(self, item, spider):
        item["price"] = int(item["price"].replace(' ', ''))
        item["params"] = dict(zip(item["params"][::2], item["params"][1::2]))

        collection = self.db[spider.name]
        collection.update_one(item, {"$set": item}, upsert=True)

        return item
