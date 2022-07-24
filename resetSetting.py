# 统一设置 scrapy 项目中的 setting.py

from settingConfig import *


class ChangeSetting:
    def __init__(self):
        self.filePath = filePath_config
        self.newConfig = setting_new_config
        self.mongoDB = mongoDB_config

    def has_reset(self, obj):
        with open(self.filePath[obj], 'r', encoding='utf-8') as file:
            return '已经reset成功' in file.read()

    def reset(self, obj):
        if not self.has_reset(obj):
            with open(self.filePath[obj], 'a+', encoding='utf-8') as file:
                file.write(self.newConfig)

    def add_mongoDB(self, obj):
        with open(self.filePath[obj], 'a', encoding='utf-8') as file:
            file.write(self.mongoDB_config)

    def read(self, obj):
        with open(self.filePath[obj], 'r', encoding='utf-8') as file:
            file_str = file.read().split('\n')
            print(file_str)


file = ChangeSetting()
file.reset('comicK')
