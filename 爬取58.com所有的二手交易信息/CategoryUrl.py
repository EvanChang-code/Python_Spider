from bs4 import BeautifulSoup
import requests
import pymongo
import chardet

url = 'http://3g.ganji.com/'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Cookie':'GANJISESSID=3604786c786fe09f5d2e52151f99a478; cityDomain=bj; mobversionbeta=3g; __utmganji_v20110909=0xcd6acb863605895f4e8129533d91e1e; index_city_refuse=refuse; Hm_lvt_42c1a7031efc9970f51536db2fbbfd19=1479620039; Hm_lpvt_42c1a7031efc9970f51536db2fbbfd19=1479620932'
}

def getCategoryUrl(url):
    web_data = requests.get(url,params=header) # 可以添加IP
    soup = BeautifulSoup(web_data.text, 'html5lib')
    category_urls = soup.select('div.module-area > div.module-item.clear > a')
    for category_url in category_urls:
        url_link = category_url.get('href').split('?')[0]
        if url_link[0:4] == 'http':
            pass
        else:
            categoryurl = 'http://3g.ganji.com' + url_link
            data = {
                "catagoryurl": categoryurl
            }
    return data

# 对data进行的人工的筛选
data = '''
    http://3g.ganji.com/bj_shouji/
    http://3g.ganji.com/bj_ershoubijibendiannao/
    http://3g.ganji.com/bj_jiaju/
    http://3g.ganji.com/bj_motuoche/
    http://3g.ganji.com/bj_diandongche/
    http://3g.ganji.com/bj_shuma/
    http://3g.ganji.com/bj_taishidiannaozhengji/
    http://3g.ganji.com/bj_jiadian/
    http://3g.ganji.com/bj_zixingchemaimai/
    http://3g.ganji.com/bj_fushixiaobaxuemao/
    http://3g.ganji.com/bj_bangong/
    http://3g.ganji.com/bj_wujingongju/
    http://3g.ganji.com/bj_bangongjiaju/
    http://3g.ganji.com/bj_nongyongpin/
    http://3g.ganji.com/bj_shoucangpin/
'''
