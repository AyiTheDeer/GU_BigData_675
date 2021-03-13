import pymongo
from pymongo import MongoClient
import pandas as pd
import json


# 1. функция записи полученных парсером данных в базу
def insert_vacansies(f):
    client = MongoClient('localhost', 27017)
    db = client.geek_brains
    collection = 'vacancies'

    # уюираю весь строковый шит, из-за которого монго неправильно определяет тип данных
    data = pd.read_csv(f)
    data = data[(data['salary_min'] != 'По договоренности') | (data['salary_max'] != 'По договоренности')]
    data = data.fillna(0)
    data['salary_min'] = data['salary_min'].astype('int')
    data['salary_max'] = data['salary_max'].astype('int')

    data_json = json.loads(data.to_json(orient='records'))
    db[collection].insert_many(data_json)
    return (print('Ok'))


# 2. функция принта записей больше минимальной зарплаты
def print_salary_min(x):
    with MongoClient('localhost', 27017) as client:
        db = client.geek_brains
        collection = 'vacancies'

        a = db[collection].find(
            {'$and': [
                {'salary_min': {'$gt': x}},
                {'salary_max': {'$exists': True}}
            ]}
        )

        for i in a:
            print(a)

# 3. понимаю, что нужно использовать upsert но не могу написать код.
