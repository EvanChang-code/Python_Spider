# -*- coding: utf-8 -*-

'''
author: zhangli
'''

from bs4 import BeautifulSoup
import requests
import time

def get_sex(name):
    if name == ['member_ico']:
        return 'man'
    elif name == ['member_ico']:
        return 'woman'
    else:
        return None

def get_one_room_infor(url):
    time.sleep(2)
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.content, 'html5lib')
    titles = soup.select('div.pho_info > h4 > em')
    adds = soup.select('span.pr5')
    pays = soup.select('div.day_l > span')
    imgs = soup.select('div.pho_show_small > ul.detail-thumb-nav > li > img')
    host_imgs = soup.select('div.member_pic > a > img')
    host_names = soup.select('a.lorder_name')
    host_sexs = soup.select('div.member_pic > div')
    #print(host_sexs)

    for title,add,pay,img,host_img,host_name,host_sex in zip(titles,adds,pays,imgs,host_imgs,host_names,host_sexs):
        sex = host_sex.get('class')
        print_sex = get_sex(sex)
        data = {
            'title':title.get_text().replace(' ',''),
            'add':add.get_text().replace(' ',''),
            'pay':pay.get_text(),
            'img':img.get('data-src'),
            'host_img':host_img.get('src'),
            'host_name':host_name.get_text(),
            'host_sex':print_sex
        }
        print(data)

def get_urls(add_page):
    for page in range(1,add_page):
        url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(page)
        host_page = requests.get(url)
        soup = BeautifulSoup(host_page.content,'html5lib')
        son_page = soup.select('ul[class="pic_list clearfix"] > li > a')
        for son_href in son_page:
            urls.append(son_href.get('href'))

urls = []
def get_room_info(number):
    get_urls(number)
    for url in urls:
        get_one_room_infor(url)

get_room_info(3)
'''
http://bj.xiaozhu.com/fangzi/5028993914.html
http://bj.xiaozhu.com/fangzi/5393993714.html
http://bj.xiaozhu.com/fangzi/5417240614.html
http://bj.xiaozhu.com/fangzi/1642469035.html
http://bj.xiaozhu.com/fangzi/5076532914.html
'''