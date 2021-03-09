import time
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import pandas as pd
import unicodedata
import re
import random

u = UserAgent()


def get(url, headers, params):
    r = requests.get(url, headers=headers, params=params)
    return r


def get_superjob(keyword):
    url = 'https://www.superjob.ru/vacancy/search/'
    params = {
        'keywords': keyword,
        'noGeo': '1',
        'page': ''
    }
    headers = {'User-Agent': u.random}

    r = get(url, headers, params)

    # поиск последней страницы
    if r.ok:
        soup = bs(r.text)
        pages = soup.find(class_='f-test-button-1')
    if not pages:
        last_page = 1
    else:
        last_page = int(pages.findParent().find_all('a')[-2].getText())

    superjob = []

    # обработка каждой найденной страницы
    for page in range(0, last_page + 1):
        params['page'] = str(page)
        r = get(url, headers, params)

        if r.ok:
            soup = bs(r.text, 'html.parser')
            result = soup.find_all(class_='f-test-vacancy-item')

            # парсинг информации
            for item in result:
                # получение названия вакансии
                name = item.find('a').getText()

                # cссылка на вакансию
                link = f'https://www.superjob.ru{item.find("a").get("href")}'

                # зарплата
                salary = item.find(class_='f-test-text-company-item-salary').getText()
                salary_min = salary_max = None

                if salary.split()[0] == 'По':
                    salary_min = salary_max = 'По договоренности'

                elif unicodedata.normalize("NFKD", salary).split()[0] == 'от':
                    salary_min = int(re.sub('[^\d]', '', salary))

                elif unicodedata.normalize("NFKD", salary).split()[0] == 'до':
                    salary_max = int(re.sub('[^\d]', '', salary))

                elif unicodedata.normalize("NFKD", salary).split()[2] == '—':
                    salary_min = re.sub('[^\d—]', '', salary).split('—')[0]
                    salary_max = re.sub('[^\d—]', '', salary).split('—')[1]

                else:
                    salary_max = re.sub('[^\d—]', '', salary).split('—')[0]

                # сайт
                website = 'superjob.ru'

                superjob.append({
                    'name': name,
                    'link': link,
                    'salary_min': salary_min,
                    'salary_max': salary_max,
                    'currency': 'rub',
                    'website': website
                })

                time.sleep(random.randint(1, 2))
    superjob = pd.DataFrame(superjob)
    return superjob


def get_hh(keyword):
    params = {
        'text': keyword,
        'area': '',
        'search_field': 'name',
        'items_on_page': '100',
        'page': ''
    }
    headers = {'User-Agent': u.random}
    link = 'https://hh.ru/search/vacancy'

    r = get(link, headers, params)

    # поиск последней страницы
    if r.ok:
        soup = bs(r.text, 'html.parser')
        pages = soup.find('div', {'data-qa': 'pager-block'})
    if not pages:
        last_page = 1
    else:
        last_page = int(pages.find_all('a', {'class': 'HH-Pager-Control'})[-2].getText())

    headhunter = []

    # обработка каждой найденной страницы
    for page in range(0, last_page + 1):
        params['page'] = str(page)
        r = get(link, headers, params)

        if r.ok:
            soup = bs(r.text, 'html.parser')
            result = soup.find_all(class_='vacancy-serp-item')

            # парсинг информации
            for item in result:
                # получение названия вакансии
                name = item.find(class_='resume-search-item__name').getText()

                # cссылка на вакансию
                link = item.find(class_='bloko-link').get("href").split('?')[0]

                # зарплата
                salary = result[2].find(class_='vacancy-serp-item__compensation')

                if not salary:
                    salary_min = salary_max = currency = None
                else:
                    salary = salary.getText().replace(u'\xa0', u'')

                    salary = re.split(r'\s|-', salary)

                    if salary[0] == 'до':
                        salary_min = None
                        salary_max = int(salary[1])
                    elif salary[0] == 'от':
                        salary_min = int(salary[1])
                        salary_max = None
                    else:
                        salary_min = int(salary[0])
                        salary_max = int(salary[1])

                    currency = salary[2]

                # сайт
                website = 'hh.ru'

                headhunter.append({
                    'name': name,
                    'link': link,
                    'salary_min': salary_min,
                    'salary_max': salary_max,
                    'currency': currency,
                    'website': website
                })

                time.sleep(random.randint(1, 2))
    headhunter = pd.DataFrame(headhunter)
    return headhunter


def get_vacancy(keyword):
    sj = get_superjob(keyword)
    hh = get_hh(keyword)
    frames = [sj, hh]
    df = pd.concat(frames)
    return df


keyword = input('Введите ключевое слово вакансии: ')
df = get_vacancy(keyword)
print(df)