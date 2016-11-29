from bs4 import BeautifulSoup
import requests
import time
import pymongo

url= 'http://3g.ganji.com/bj_shouji/'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Cookie':'GANJISESSID=3604786c786fe09f5d2e52151f99a478; cityDomain=bj; mobversionbeta=3g; __utmganji_v20110909=0xcd6acb863605895f4e8129533d91e1e; index_city_refuse=refuse; Hm_lvt_42c1a7031efc9970f51536db2fbbfd19=1479620039; Hm_lpvt_42c1a7031efc9970f51536db2fbbfd19=1479620932'
}

client = pymongo.MongoClient('localhost', 27017)
goodsurl = client['goodsurl']
sheet_one = goodsurl['sheet_one']
sheet_two = goodsurl['sheet_two']

def getGoodsLink(cate_url, page, who_seller=0):

    for i in range(1,page):
        url = cate_url + '?page={}'.format(str(i)) # 组成一个完整的链接
        time.sleep(1)
        web_data = requests.get(url, params=header)
        soup = BeautifulSoup(web_data.text, 'html5lib')
        url_links = soup.select('li.zzitem a')
        print('ok')
        for url_link in url_links:
            link = url_link.get('href')
            if link.split('=')[-1] == "58":
                pass
            else:
                data = {
                    'link':link
                }
                sheet_one.insert_one(data)


def get_goods_information():
    for link in sheet_one.find():
        url = link['link']
        print(url)
        if len(url) < 5:
            pass
        else:
            web_data = requests.get(url,params=header)
            soup = BeautifulSoup(web_data.text, 'html5lib')
            try:
                title = soup.select('div.miaoshu')[0].get_text().split(' ')[0:3]
            except:
                title = None
            finally:
                title = None
            try:
                price = soup.select('strong')[0].get_text()
            except:
                price = None
            finally:
                price = None
            data = {
                'title':title,
                'price':price
            }
            sheet_two.insert_one(data)
            print('ok')


# getGoodsLink(url, 2)
get_goods_information()
