### 存放 scrapy 项目

基础操作  

    pip install scrpay #
    cd projectFile 
    
    运行 resetSetting.py 修改 setting 的默认值
    
            
    

####1. music163  网易云 音乐下载

    # 创建music163文件 内有基础配置
    scrapy startproject music163 #

    # 进入项目文件
    cd music163

    # spiders 文件生产 downloadMusic.py
    # downloadMusic   +  域名
    scrapy genspider downloadMusic music.163.com
---

####2. comicK 漫画人 漫画下载

    # 创建music163文件 内有基础配置
    scrapy startproject comicK #

    # 进入项目文件
    cd comicK

    # spiders 文件生产 comic.py
    # comic   +  域名
    scrapy genspider comic www.1kkk.com

目标：

1.获取 url title path images

先修改 item.py

    class KkkspiderItem(scrapy.Item):

        title = scrapy.Field()
        image_urls = scrapy.Field()
        image_paths = scrapy.Field()
        images = scrapy.Field()

之后spider 下的主函数  parse 主动运行函数 , start_requests 分页函数

        def parse(self, response):
            lists = response.xpath('//div[@class="mh-item"]')


2.再 创建文件  和 下载图片 

        # 少了一个插件 就失效了 也不报错  坑爹啊
        pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com pillow

            def parse(self, response):
        lists = response.xpath('//div[@class="mh-item"]')
        for i in lists:
            items = ComickItem()
            items['title'] = i.xpath('.//h2/a/text()').get()

        # 第二个坑  需要字符串，但是保持了 数组 需要 for



---