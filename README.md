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

问题1：scrapy 读取不到 iframe 里面的内容 需要用 selenium
问题2：scrapy 对页面接口的 抓取  之后 获取 接口 返回的数据
方案1：使用 selenium 来 抓取 iframe
    
        downloadMusic.py
        def __init__(self):
            #初始化一个web
            self.web=webdriver.Firefox()    

        
        middlerPip 文件
        def process_response(self, request, response, spider):
            web=spider.web
            if request.url in spider.mode_urls:
                web.get(request.url)
                time.sleep(2)
                page_text=web.page_source#包含动态加载数据
                #针对定位到这些response进行篡改
                #s实例化一个新的响应对象(符合需求：包含动态加载出的新闻数据） 替代原来旧的响应对象
                new_response=HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)
                return new_response
            else:
                return response

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


2.再 创建文件  和 下载图片 ---- piplines.py --用来下载实体文件例如：图片,音乐,文件

        # 少了一个插件 就失效了 也不报错  坑爹啊
        pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com pillow

            def parse(self, response):
        lists = response.xpath('//div[@class="mh-item"]')
        for i in lists:
            items = ComickItem()
            items['title'] = i.xpath('.//h2/a/text()').get()

        # 第二个坑  需要字符串，但是保持了 数组 需要 for

        # 请求图片的连接
        def get_media_requests(self, item, info):
            yield Request(item['image_urls'])  # 下载的路径  接收字符串
    
        # 返回保存路径和图片名称 函数
        def file_path(self, request, response=None, info=None, *, item=None):
            return f'{item["title"]}/{item["title"]}.jpg'
    
        # 结束函数
        def item_completed(self, results, item, info):


        核心 from scrapy.pipelines.images import ImagesPipeline  # 图片下载工具 内置函数


基础完成 图片功能



---