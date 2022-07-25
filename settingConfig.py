# 放置 各种配置 字符串 让其他文件 看起来比较简洁

setting_new_config = '''
ROBOTSTXT_OBEY = False

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]

FEED_EXPORT_ENCODING = 'utf-8'  # 编码格式
IMAGES_STORE = 'images'  # 设置保存图片的根目录
FILES_STORE = 'files'
DOWNLOAD_DELAY = 1   # 操作都延迟1秒

# 418 反爬虫检测到了 添加 表头
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
}

IP_LIST = [
    # {"ip": "https://139.217.101.53:9080"}   # TCP connection timed out: 10060: 由于连接
    # {"ip": "http://122.6.226.55:9999"}  # Connection was refused by other side: 10061: 由于目标计算机积极拒绝，
    {"ip": "https://203.189.210.170:8888"}  # 可以使用  防火墙不影响  http://www.ip3366.net/ 比较靠谱
    # {"ip": "111.231.86.149:7890"}
]

COOKIES_ENABLED = True  # 使用 返回的cookie

# 已经reset成功
'''


mongoDB_config = '''

DB_PORT = 27017
DB_IP = '127.0.0.1'
DB_NAME = 'ipDB'
DB_USER = 'ipDB'
DB_PWD = 'ipDB'
DB_COLLECTION = 'ipCollection'

# mongoDB添加成功
'''

filePath_config = {
    'comic': 'comicK/comicK/settings.py',
    'downloadMusic': 'music163/music163/settings.py'
}
run_file_config = '''
from scrapy import cmdline

cmdline.execute('scrapy crawl {}'.split())
# cmdline.execute('scrapy crawl kkk2 -o kkk2.json'.split())  # 运行模式
# ctrl + shift + F10   运行当前文件


'''
