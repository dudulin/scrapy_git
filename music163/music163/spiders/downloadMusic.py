import scrapy


class DownloadmusicSpider(scrapy.Spider):
    name = 'downloadMusic'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/']

    def parse(self, response):
        pass
