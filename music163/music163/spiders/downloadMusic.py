import scrapy
from ..items import Music163Item
# import json

class DownloadmusicSpider(scrapy.Spider):
    name = 'downloadMusic'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/']
    dowload_url = 'http://music.163.com/song/media/outer/url?id={}'

    def parse(self, response):
        lists = response.xpath('//div[@class="ttc"]')
        for i in lists:
            items = Music163Item()
            items['title'] = i.xpath(
                './/a/@href').get()
            items['id'] = self.dowload_url.format(i.xpath('.//b/@title').get())
            print(items, '1111')
            yield items


