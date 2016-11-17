from bs4 import BeautifulSoup

'''

body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > img
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.caption > h4:nth-child(2) > a
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.caption > h4.pull-right
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.ratings > p:nth-child(2) > span:nth-child(4)
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.ratings > p.pull-right
'''

with open("D:/MY_Program/Github/Python_爬虫/对本地网页进行元素分析/本地网页/index.html",'r') as web_data:
    soup = BeautifulSoup(web_data,'html5lib')
    images = soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    names = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    prices = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    stars = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p > span')
    reviews = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    web_data.close()
print(stars)

for image, name, price, review, star in zip(images, names, prices, reviews, stars):
    i = 0
    print(star.find_all("span",class_='glyphicon glyphicon-star')) 
    # if star.get('class')==['glyphicon','glyphicon-star']:
    #     i += 1
    date={'images':image.get('src'),
          'names':name.get_text(),
          'prices':price.get_text(),
          'reviews':review.get_text(),
          'stars':i}
    #print(date)
