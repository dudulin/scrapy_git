### 存放 scrapy 项目

基础操作  

    pip install scrpay #
    cd projectFile 
    
    
            
    

####1. music163  网易云 音乐下载

    # 创建music163文件 内有基础配置
    scrapy startproject music163 #

    # 进入项目文件
    cd music163

    # spiders 文件生产 downloadMusic.py
    # downloadMusic   +  域名
    scrapy genspider downloadMusic music.163.com


####2. comicK 漫画人 漫画下载

    # 创建music163文件 内有基础配置
    scrapy startproject comicK #

    # 进入项目文件
    cd comicK

    # spiders 文件生产 comic.py
    # comic   +  域名
    scrapy genspider comic www.1kkk.com