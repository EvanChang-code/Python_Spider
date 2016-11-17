from bs4 import BeautifulSoup
import requests
import time

'''
#jingzhun > tbody > tr:nth-child(2) > td.t > a.t
'''

url_link = []
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}

def get_urls(father_url):
    time.sleep(2)
    web_data = requests.get(father_url, params=headers)
    soup = BeautifulSoup(web_data.content, "html5lib")
    goods_link = soup.select('tr.zzinfo > td.img > a')

    for goods in goods_link:
        good_link = goods.get('href')
        url_link.append(good_link)   # 提取所有的网页
    return url_link


def get_info():

    urls = get_urls(url)
    time.sleep(2)
    for boy_url in urls:
        web_data = requests.get(boy_url, params=headers)
        soup = BeautifulSoup(web_data.content, 'html5lib')
        lists = soup.select('span.crb_i > a')
        titles = soup.select('div.box_left_top > h1')
        prices = soup.select('span.price_now > i')
        places = soup.select('div.palce_li > span > i')
        biaoqians = soup.select('div.biaoqian_li > span')
        look_times = soup.select('p.info_p > span')

        '''
        可以不用for循环这么麻烦的方式
        因为select返回的是列表，先判断一下返回的列表有几个元素
        所以可以按照取元素的方法给标记出来
        '''
        for list,title,price,place,biaoqian,look_time in zip(lists,titles,prices,places,biaoqians,look_times):

            data = {
                "list":list.get_text().replace(" ",""),
                "title":title.get_text().replace(" ",""),
                "price":price.get_text().replace(" ",""),
                "place":place.get_text().replace(" ",""),
                "biaoqian":biaoqian.get_text(),
                "look_time":look_time.get_text()
            }
            print(data)

url = 'http://bj.58.com/pbdn/0'

get_info()

