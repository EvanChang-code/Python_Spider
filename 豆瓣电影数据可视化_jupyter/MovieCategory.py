# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time
import pymongo
import json
import urllib.request

'''
author: zhangli

Questions:
1. js加载的标签
Steps:
2. 下载到所有的标签
3. 对评分进行排序(在程序中)
'''

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=rank&page_limit=20&page_start=0'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Cookie':'ll="118221"; bid=j1XP00A3xq0; ap=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1480557360%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DtAgfOG4OTfz8DlExaM7LH4IIdYmOUmZfO_P15qjaitWGu7VZSKLBnsZHKCQui5DC%26wd%3D%26eqid%3Dcf8d958c0001eb6500000006583f8323%22%5D; _pk_id.100001.4cf6=a4524143c9d6cba3.1478779675.10.1480557360.1480497006.; _pk_ses.100001.4cf6=*; __utma=30149280.750154763.1478779675.1480494853.1480557361.10; __utmb=30149280.0.10.1480557361; __utmc=30149280; __utmz=30149280.1480557361.10.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1975075460.1478779675.1480496664.1480557362.10; __utmb=223695111.0.10.1480557362; __utmc=223695111; __utmz=223695111.1480557362.10.9.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=6D16B8F7B6708BB901FE2A238163EF27|2b8a41d214570ac3bd0eabae643fdb0a'
}

client = pymongo.MongoClient('localhost',27017)
movie = client['movie']
movie_information = movie['movie_information']

def moiveinformation(page): # 电影基本信息获取函数
    movie_information.remove()
    for i in range(0,page):
        url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=rank&page_limit=20&page_start={}'.format(str(i*20))
        time.sleep(1)
        web_data = requests.get(url, params=header)
        soup = BeautifulSoup(web_data.content, 'html5lib')
        category = soup.select('body')[0].get_text()  # 读取标签中的内容，类型为class str
        dic_cates = json.loads(category)['subjects']  # 利用json解析式顺利解决问题
        for dic_cate in dic_cates:   # 解析为字典的形式，然后按照字典的数据处理方法进行
            title = dic_cate['title']
            rate = dic_cate['rate']
            url_link = dic_cate['url']
            img_link = dic_cate['cover']
            data = {
                'title':title,
                'rate':rate,
                'url_link':url_link,
                'img_link':img_link
            }
            movie_information.insert_one(data)
        print('ok')

def get_moive_pic():   # 图片下载函数
    img_links = [img['img_link'] for img in movie_information.find()]
    titles = [title['title'] for title in movie_information.find()]
    rates = [rate['rate'] for rate in movie_information.find()]
    for img_link,title,rate in zip(img_links,titles,rates):
        img_name = '%s_%s.jpg' % (rate,title)
        urllib.request.urlretrieve(img_link,'C:/Users/ZhangLi/Desktop/123/%s' % img_name)
        time.sleep(1)
# print(dic_cates)
# print(type(category))
# dic_cate = ast.literal_eval(category)  # 不是标准的字典形式，所以将字符串转换成字典的时候会报错

# moiveinformation(10)
# get_moive_pic()


