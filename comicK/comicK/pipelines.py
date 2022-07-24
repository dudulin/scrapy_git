# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from itemadapter import ItemAdapter


from scrapy.pipelines.images import ImagesPipeline  # 图片下载工具 内置函数
from scrapy import Request  # 获取请求功能
from scrapy.exceptions import DropItem




class ComickPipeline(ImagesPipeline):  # ImagesPipeline 继承图片下载功能
    # def process_item(self, item, spider):
    #     return item

    def get_media_requests(self, item, info):

        # yield Request(url=item['image_urls'], meta={'item': item})  # 是列表 需要 变成字符串
        for image_urls in item['image_urls']:
            yield Request(image_urls)

    def file_path(self, request, response=None, info=None, *, item=None):
        return f'{item["title"]}.jpg'

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
