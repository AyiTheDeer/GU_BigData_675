# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
# в вашем случае
# MONGO_URL = "localhost:27017"
# если нестандартный порт
MONGO_URL = "localhost:27017"


class JobparserPipeline:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client['geek_brains']

    def process_item(self, item, spider):
        if spider.name == 'hhru':
            item["site"] = 'hh.ru'
        if spider.name == 'sjru':
            item["site"] = 'superjob.ru'

        collection = self.db[spider.name]
        # collection.insert_one(item)
        # collection.update_one({'url': item['url']}, item, upsert=True)
        collection.update_one(item, {"$set": item}, upsert=True)
        # чтобы удалить поле нужно делать то же, что и в обычном словаре
        # del item['salary']
        # item.pop("title")
        return item
