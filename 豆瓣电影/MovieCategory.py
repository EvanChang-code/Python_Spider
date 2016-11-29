from bs4 import BeautifulSoup
import requests
import time
import pymongo
'''
最好的方法还是读文档

1.js加载的标签
2.本方法找到请求的网页，对网页为字典的数据进行分析
'''

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Cookie':'ll="118221"; bid=j1XP00A3xq0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1480418407%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DkgkAonW__3B6hSK16QLv1i71U3zKZgGq23o5tup7IzHVATYZs6hJYqxF9oan0SLz%26wd%3D%26eqid%3Dc68c595b0000e9f000000004583d6452%22%5D; _vwo_uuid_v2=6D16B8F7B6708BB901FE2A238163EF27|2b8a41d214570ac3bd0eabae643fdb0a; _pk_id.100001.4cf6=a4524143c9d6cba3.1478779675.2.1480420082.1478779675.; _pk_ses.100001.4cf6=*; __utma=30149280.750154763.1478779675.1478779675.1480418405.2; __utmb=30149280.0.10.1480418405; __utmc=30149280; __utmz=30149280.1480418405.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1975075460.1478779675.1478779675.1480418405.2; __utmb=223695111.0.10.1480418405; __utmc=223695111; __utmz=223695111.1480418405.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic'
}
'''
https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=20&page_start=0
https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%9C%80%E6%96%B0&page_limit=20&page_start=0
https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=20&page_start=0
'''

client = pymongo.MongoClient('client')
movie = client['movie']
movie_info = movie['movie_info']

web_data = requests.get(url, params=header)
soup = BeautifulSoup(web_data.content, 'html5lib')
category = soup.select('body')[0].get_text()  # 读取标签中的内容
# ii = [i['subjects'] for i in category]
# ii = category.find('subject')
ii = category['subjects']
print(type(ii))
print(ii)
'''
str 和 class str 一样么
怎么将str转换成dic或者是list，或者是利用split()
json是什么工具
'''


