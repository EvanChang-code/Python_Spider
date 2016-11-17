from bs4 import BeautifulSoup
import requests
import urllib.request
import time

'''
被远程主机强制关闭了
'''

pic_link = []
header = {
    'Cookie':'vglnk.Agent.p=b83680e409308d1c7eb0504459135028',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
def get_one_page(url):
    time.sleep(4)
    web_data = requests.get(url, params= header)
    soup = BeautifulSoup(web_data.content, 'html5lib')
    pic_hrefs = soup.select('img.entry-thumbnail')

    for pic_href in pic_hrefs:
        pics = pic_href.get('src')
        pic_link.append(pics)
    print(pic_link)
    i = 1
    for pic in pic_link:
        urllib.request.urlretrieve(pic,'C:\\Users\\ZhangLi\\Desktop\\123\\1.jpg')
        i+=1
        print(i)

def get_all_pic(start, end):
    urls = ['http://weheartit.com/inspirations/taylorswift?scrolling=true&page={}&b'.format(str(i) for i in range(start,end))]
    for url in urls:
        get_one_page(url)


get_all_pic(1,2)












