# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import os
from itemadapter import ItemAdapter

from scrapy.pipelines.images import ImagesPipeline  # 图片下载工具 内置函数
from scrapy import Request  # 获取请求功能
from scrapy.exceptions import DropItem


class ComickPipeline(ImagesPipeline):  # ImagesPipeline 继承图片下载功能
    # def process_item(self, item, spider):
    #     return item

    # 请求图片的连接
    def get_media_requests(self, item, info):
        yield Request(item['image_urls'])  # 下载的路径  接收字符串

    # 返回保存路径和图片名称 函数
    def file_path(self, request, response=None, info=None, *, item=None):
        return f'{item["title"]}/{item["title"]}.jpg'

    # 结束函数
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths[0]
        return item


class JsonPipeline(object):
    # 构造方法（初始化对象时执行的方法）
    def __init__(self):
        # 必须使用 w+ 模式打开文件，以便后续进行 读写操作（w+模式，意味既可读，亦可写）
        # 注意：此处打开文件使用的不是 python 的 open 方法，而是 codecs 中的 open 方法
        self.json_file = codecs.open('message.json', 'w+', encoding='UTF-8')

    # 爬虫开始时执行的方法
    def open_spider(self, spider):
        # 在爬虫开始时，首先写入一个 '[' 符号，构造一个 json 数组
        # 为使得 Json 文件具有更高的易读性，我们辅助输出了 '\n'（换行符）
        self.json_file.write('[\n')

    # 爬虫 pipeline 接收到 Scrapy 引擎发来的 item 数据时，执行的方法
    def process_item(self, item, spider):
        # 将 item 转换为 字典类型，并编码为 json 字符串，写入文件
        # 为使得 Json 文件具有更高的易读性，我们辅助输出了 '\t'（制表符） 与 '\n'（换行符）
        item_json = json.dumps(dict(item), ensure_ascii=False)
        self.json_file.write('\t' + item_json + ',\n')
        return item

    # 爬虫结束时执行的方法
    def close_spider(self, spider):
        # 在结束后，需要对 process_item 最后一次执行输出的 “逗号” 去除
        # 当前文件指针处于文件尾，我们需要首先使用 SEEK 方法，定位文件尾前的两个字符（一个','(逗号), 一个'\n'(换行符)）的位置
        self.json_file.seek(-2, os.SEEK_END)
        # 使用 truncate() 方法，将后面的数据清空
        self.json_file.truncate()
        # 重新输出'\n'，并输入']'，与 open_spider(self, spider) 时输出的 '['，构成一个完整的数组格式
        self.json_file.write('\n]')
        # 关闭文件
        self.json_file.close()
