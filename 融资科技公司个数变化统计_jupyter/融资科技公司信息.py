# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import random
import json
import pymongo

headers = [
    'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
]
my_header = random.choice(headers)


header = {
    'User-Agent':my_header,
    'Cookie':'gr_user_id=fa5abfa0-3869-47de-95a0-c2273a15521d; acw_tc=AQAAAGPEWUgVpQ4A9HPJ2tMiSsL5fZyf; gr_session_id_eee5a46c52000d401f969f4535bdaa78=a7416a54-38f9-436d-aeb4-e65de96b1ee8; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1480495282,1480678966; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1480679441; session=528920b08a1a8fb0370859a7a656cb22898b9dee; _ga=GA1.2.95742166.1480495281; _gat=1; _hp2_ses_props.2147584538=%7B%22r%22%3A%22http%3A%2F%2Fwww.itjuzi.com%2Fcompany%22%2C%22us%22%3A%22itjuzi.com%22%2C%22ts%22%3A1480679199841%2C%22d%22%3A%22radar.itjuzi.com%22%2C%22h%22%3A%22%2F%22%7D; _hp2_id.2147584538=%7B%22userId%22%3A%226217513258194986%22%2C%22pageviewId%22%3A%228835738178325622%22%2C%22sessionId%22%3A%225975816553277620%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%223.0%22%7D'
}
ip = [
    'http://111.13.7.42:81',
    'http://59.107.26.220:10000',
    'http://211.153.17.151:80',
    'http://121.8.98.201:8080',
    'http://183.95.152.159:80',
    'http://124.160.225.37:3128',
    'http://183.95.152.159:3128'
]
proxies_ip = random.choice(ip)
proxies = {'http':proxies_ip}

client = pymongo.MongoClient('localhost',27017)
company_info = client['company_info']
information = company_info['information']

def getCompanyInformation(page):

    information.remove()

    for i in range(0,page):
        url = 'http://www.chinaventure.com.cn/event/searchInvestList/-1/-1/-1/-1/-1/-1/{}-16.shtml'.format(str(i*15))

        web_data = requests.get(url, params=header)
        soup = BeautifulSoup(web_data.content, 'html5lib')
        text = soup.select('body')[0].get_text()
        dict_text = json.loads(text)
        for text in dict_text['data']:
            company = text['title']
            date = text['happenedDateStr']
            local = text['targetEnterprise']['location']
            product = text['targetEnterprise']['products']
            industry = text['targetEnterprise']['industry']['name']
            amount = text['amountStr']
            data = {
                'company':company,
                'date':date,
                'local':local,
                'product':product,
                'industry':industry,
                'amount':amount
            }
            information.insert_one(data)
            print('down')

getCompanyInformation(9)


