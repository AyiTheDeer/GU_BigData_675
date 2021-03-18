import requests
from lxml import html
from pymongo import MongoClient
import pandas as pd
import json
from fake_useragent import UserAgent
from datetime import datetime
u = UserAgent()


# функция распарсивания
def get_xpath_content(link, xpath):
    headers = {'User-Agent': u.random}
    r = requests.get(link, headers)
    s = r.text
    doc = html.fromstring(s)
    return doc.xpath(xpath)


# новости из мейлру
def mailru():
    MAILRU = 'https://news.mail.ru/'
    top_5_news = "//div[contains(@class,'topnews')]//a[contains(@href,'news.mail.ru')]/@href"
    other_news = '//ul/li/a/@href'
    publication_time = "//meta[@property='article:published_time']/@content"
    source = "//a[contains(@class,'breadcrumbs__link')]/@href"
    title = '//title/text()'

    x = get_xpath_content(MAILRU, top_5_news)
    y = get_xpath_content(MAILRU, other_news)
    links = list(set(x + y))  # делаю, т.к в листах дубликаты ссылок

    result = []
    for link in links:
        pt = get_xpath_content(link, publication_time)[0]
        src = get_xpath_content(link, source)[0]
        ttl = get_xpath_content(link, title)[0]

        result.append({
            'link': link,
            'publication_time': pt,
            'source': src,
            'title': ttl
        })
    result = pd.DataFrame(result)
    return result


# новости ленты
def lentaru():
    LENTA = 'https://lenta.ru/'
    link = "///section[contains(@class,'top7-for-main')]//div[contains(@class,'item')]/a[not(@target)]/@href"
    title = "//title/text()"
    publication_time = "//meta[@itemprop='datePublished']/@content"

    links = get_xpath_content(LENTA, link)

    result = []
    for link in links:
        link = f'https://lenta.ru{link}'
        pt = get_xpath_content(link, publication_time)[0]
        src = LENTA
        ttl = get_xpath_content(link, title)[0]

        result.append({
            'link': link,
            'publication_time': pt,
            'source': src,
            'title': ttl
        })
    result = pd.DataFrame(result)
    return result


# новости яндекса
def yandexru():
    YANDEX = 'https://yandex.ru/news'
    container = "//div[contains(@class,'news-top-flexible-stories')]"
    link = "//span[contains(@class,'mg-card-source__source')]/a/@href "
    title = "//h2/text()"
    source = "//span[contains(@class,'mg-card-source__source')]/a/text()"
    publication_time = "//span[contains(@class,'mg-card-source__time')]/text()"

    pt = get_xpath_content(YANDEX, f'{container}{publication_time}')
    link = get_xpath_content(YANDEX, f'{container}{link}')
    src = get_xpath_content(YANDEX, f'{container}{source}')
    ttl = get_xpath_content(YANDEX, f'{container}{title}')

    yandex_news = pd.DataFrame()
    yandex_news['link'] = link
    yandex_news['publication_time'] = pt
    yandex_news['source'] = src
    yandex_news['title'] = ttl
    yandex_news['publication_date'] = datetime.now().date()

    return yandex_news


# отправка в монго
def insert_vacansies(df):
    client = MongoClient('localhost', 27017)
    db = client.geek_brains
    collection = 'news'

    data_json = json.loads(df.to_json(orient='records'))
    db[collection].insert_many(data_json)
    print('Ok')

# паехали
mailru_news = mailru()
lentaru_news = lentaru()
yandex_news = yandexru()

frames = [mailru_news, lentaru_news, yandex_news]
result = pd.concat(frames)

insert_vacansies(result)
