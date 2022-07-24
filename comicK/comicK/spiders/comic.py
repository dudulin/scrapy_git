import scrapy


class ComicSpider(scrapy.Spider):
    name = 'comic'
    allowed_domains = ['www.1kkk.com']
    start_urls = ['http://www.1kkk.com/']

    def parse(self, response):
        pass
