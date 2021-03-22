import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem


class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = [
        'https://hh.ru/search/vacancy?area=&fromSearchLine=true&st=searchVacancy&text=python',
    ]

    def parse(self, response: HtmlResponse):
        vacancy_links = response.xpath(
            '//div[contains(@class, "vacancy-serp-item")]//a[contains(@class, "HH-LinkModifier")]/@href'
        ).extract()
        for link in vacancy_links:
            yield response.follow(link, callback=self.parse_vacancies)

        next_page = response.xpath('//a[contains(@class, "-Pager-Controls-Next")]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        pass

    def parse_vacancies(self, response: HtmlResponse):
        # Не стоит обрабатывать данные здесь
        title = response.xpath("//h1//text()").get()
        salary = response.xpath("//p[contains(@class, 'vacancy-salary')]//span/text()").getall()
        vacancy_link = response.url
        site = self.allowed_domains[0]
        yield JobparserItem(title=title, salary=salary, vacancy_link=vacancy_link, site=site)
