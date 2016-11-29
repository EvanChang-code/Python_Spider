from bs4 import BeautifulSoup
import requests
import time
import pymongo

'''
建立数据库
'''
client = pymongo.MongoClient('localhost',27017)
phonenum = client['phonenum']
sheet_one = phonenum['sheet_one']
sheet_two = phonenum['sheet_two']

url = 'http://bj.58.com/shoujihao/'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}
web = 'http://bj.58.com/shoujihao/' # 在拼凑子网站的网址的时候使用
'''
14530330620680x
28026263316910x
28026580026684x
'''
'''
http://bj.58.com/shoujihao/pn2/
http://bj.58.com/shoujihao/28091572851020x.shtml
http://t5840228025671687.5858.com/
http://t5838080819493131.5858.com/
http://t5838167572711431.5858.com/
http://t5840228208648961.5858.com/
http://bjsjhcs.5858.com/
'''
lin = []

def get_url(page):
    '''
    获取每个页面的手机号链接
    page访问到网址的最大值
    '''
    for page in range(1,page):

        sheet_one.remove()  # 清除数据库中的数据

        url = 'http://bj.58.com/shoujihao/pn{}/'.format(str(page))
        web_data = requests.get(url, params=header)
        soup = BeautifulSoup(web_data.content, 'html5lib')

        if soup.select('div > ul > li > a > strong.number'): # 判定网页时候存在需要获取的号码
            url_links = soup.select('div.boxlist > ul > li')
            for url_link in url_links:
                url = url_link.get('logr').split('_')   # 判断是个人还是商家
                if url[0]=='p':
                    url_href = web + url[3]+ 'x.shtml'
                    data = {
                        'person_url':url_href
                    }
                    sheet_one.insert_one(data)  # 插入到数据库中，数据格式为字典
                    lin.append(url_href)
                elif url[0]=='b':
                    print('This is a business')
            return 'The phone numbers are download'
        else:
            return 'The page no have phone number'
        print('Done')

def getMessageFromWeb():
    '''
    读取基本的信息
    '''

    sheet_two.remove() # 清除数据库中的数据

    for url in lin:
        time.sleep(1)
        web_data = requests.get(url,params=header)
        soup = BeautifulSoup(web_data.text, 'html5lib')
        title = soup.select('div.col_sub.mainTitle > h1')[0].get_text().replace(" ","").replace("\t","").replace("\n","")
        times = soup.select('ul.mtit_con_left.fl > li.time')[0].get_text().replace(" ","")
        prices = soup.select('span.price.c_f50')[0].get_text().replace(" ","").replace("\t","").replace("\n","")
        seller_number = soup.select('span.f20.arial.c_f50.l_phone')[0].get_text().replace(" ","").replace("\t","").replace("\n","")
        data = {
            "person_url":url,
            "title":title,
            "time":times,
            "price":prices,
            "seller_num":seller_number
        }
        sheet_two.insert_one(data)
        print('ok')

def get_input_url():
    num_one = [sheet_one_url['person_url'] for sheet_one_url in sheet_one.find()]  # num_one是一个list
    num_two = [sheet_two_url['person_url'] for sheet_two_url in sheet_two.find()]  # num_two是一个list
    x = set(num_one)
    y = set(num_two)
    input_url = x - y  # input_url 也是一个list
    return input_url

# 测试函数
# get_url(2)
# getMessageFromWeb()
get_input_url()
# for l in sheet_one.find():
#     print(l['person_url'])
# for ll in sheet_two.find():
#     print(ll['person_url'])
# sheet_one.remove()
# sheet_two.remove()


