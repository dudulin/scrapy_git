import scrapy
from ..items import ComickItem  #

class ComicSpider(scrapy.Spider):
    name = 'comic'
    allowed_domains = ['www.1kkk.com']
    # 如果使用分页函数 start_requests 这个 url 会不生效
    start_urls = ['http://www.1kkk.com/']

    page_url = r'https://www.1kkk.com/manhua-list-area36-s2-p{}/'  # 用于分页函数

    def parse(self, response):
        lists = response.xpath('//div[@class="mh-item"]')
        for i in lists:
            items = ComickItem()
            items['title'] = i.xpath('.//h2/a/text()').get()

            items['image_urls'] = [i.xpath(
                './p/@style').get().replace('background-image: url(', '').replace(')', '')]
            yield items  # 发送给pipe 管道处理
