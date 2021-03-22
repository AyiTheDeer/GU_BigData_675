import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem

class SjruSpider(scrapy.Spider):
    name = 'sjru'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://www.superjob.ru/vacancy/search/?keywords=python']

    def parse(self, response: HtmlResponse):
        vacancy_links = response.xpath(
            '//div[contains(@class, "search-result-item")]//a[contains(@href, "vakansii")]/@href'
        ).extract()
        for link in vacancy_links:
            yield response.follow(link, callback=self.parse_vacancies)

        next_page = response.xpath('//a[contains(@class, "button-dalshe")]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        pass

    def parse_vacancies(self, response: HtmlResponse):
        title = response.xpath("//h1//text()").get()
        salary = response.xpath("//span[contains(@class, '_1OuF_ ZON4b')]//span//text()").getall()
        vacancy_link = response.url
        site = self.allowed_domains[0]
        yield JobparserItem(title=title, salary=salary, vacancy_link=vacancy_link, site=site)
