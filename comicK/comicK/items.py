# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ComickItem(scrapy.Item):
    title = scrapy.Field()
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()
    images = scrapy.Field()
