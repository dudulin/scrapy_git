# 统一设置 scrapy 项目中的 setting.py

from settingConfig import *


class ChangeSetting:
    def __init__(self, obj):
        self.filePath = filePath_config
        self.newConfig = setting_new_config
        self.mongoDB = mongoDB_config
        self.runFile = run_file_config.format(obj)
        self.path = self.filePath[obj]
        self.spider = obj

    def __has_reset__(self, message):  # __  内部使用
        with open(self.path, 'r', encoding='utf-8') as file:
            return message in file.read()

    def __creat_run__(self):
        path = self.path.split('/')[0] + '/run.py'
        with open(path, 'w+', encoding='utf-8') as file:
            file.write(self.runFile)

    def reset(self):
        if not self.__has_reset__('已经reset成功'):
            with open(self.path, 'a+', encoding='utf-8') as file:
                file.write(self.newConfig)
                self.__creat_run__()
                print('设置成功')
        else:
            print('已设置')

    def add_mongoDB(self):
        if self.__has_reset__('mongoDB添加成功'):
            with open(self.path, 'a', encoding='utf-8') as file:
                file.write(self.mongoDB)
                print('设置mongoDB成功')
        else:
            print('已设置mongoDB')

    def read(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            file_str = file.read().split('\n')
            print(file_str)


comicK = ChangeSetting('comic')
comicK.reset()
