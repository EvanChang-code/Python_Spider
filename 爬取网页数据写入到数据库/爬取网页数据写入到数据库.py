from bs4 import BeautifulSoup
import requests
import pymongo
import urllib

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Cookie':'gr_user_id=d78a7ab9-8e41-42db-9cfa-73052777dc38; abtest_ABTest4SearchDate=b; xzuuid=541ba828; __utmt=1; _gat_UA-33763849-7=1; __utma=29082403.533500442.1478695103.1478761173.1479287054.5; __utmb=29082403.5.10.1479287054; __utmc=29082403; __utmz=29082403.1478695593.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); gr_session_id_59a81cc7d8c04307ba183d331c373ef6=08a9f65a-6b2d-4235-8d2c-f3fe3362f4d6; OZ_1U_2282=vid=v82318bd401ee7.0&ctime=1479287367&ltime=1479287361; OZ_1Y_2282=erefer=-&eurl=http%3A//bj.xiaozhu.com/search-duanzufang-p1-0/&etime=1479287053&ctime=1479287367&ltime=1479287361&compid=2282; _ga=GA1.2.533500442.1478695103'
}


def get_web_data():
    client = pymongo.MongoClient('localhost', 27017)  # 和客户端进行连接
    wolden = client['wolden']  # 前边是表格的名称，后面是数据库的名称，也就是数据库
    sheet_lines = wolden['sheet_lines']  # 然后建立一个sheet

    for i in range(1,2):
        url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i))
        webdata = requests.get(url,params=header)
        soup = BeautifulSoup(webdata.content, 'html5lib')
        page_url = soup.select('div.result_btm_con.lodgeunitname')
        for url in page_url:
            url = url.get('detailurl')
            web_data = requests.get(url)
            soup2 = BeautifulSoup(web_data.text,'html5lib')
            titles = soup2.select('div.pho_info h4 em')
            title = titles[0].get_text().replace(' ','')
            addres = soup2.select('div.pho_info > p > span.pr5')
            addre = addres[0].get_text().replace(' ','')
            pays = soup2.select('div.day_l > span')
            pay = pays[0].get_text().replace(' ','')
            data = {
                'title': title,
                'addre': addre,
                'pay': pay
            }
            sheet_lines.insert_one(data)
            print('ok')

# def read_and_write_soup():
#     client = pymongo.MongoClient('localhost', 27017)  # 和客户端进行连接
#     wolden = client['wolden']  # 前边是表格的名称，后面是数据库的名称，也就是数据库
#     sheet_lines = wolden['sheet_lines']  # 然后建立一个sheet
#
#     soup = get_web_data()   # 返回网页的内容,然后到这里证明，数据有问题
#     sheet_lines.insert_one(soup)
#     print('ok')
#     lines = soup.readlines()    # 读取行数
#     for index line in enumerate(lines): # 这个函数的意思
#
#     print(type(lines)) # 应该是没有读出东西来

get_web_data()









