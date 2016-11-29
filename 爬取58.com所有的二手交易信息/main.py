from multiprocessing import Pool
from CategoryUrl import data
from GetGoodsUrl import getGoodsLink, get_goods_information

'''
需要改进的地方：
1. 页面的请求可以给requests.get()加上参数IP
2. 对于要抓取的元素有多个关键词是，可以使用匿名函数list(map(lambda......))
3. 在数据库中，为了防止重复，使用set()加迭代取值的方法取出重复
4. 使用try...except...finally的方法防止程序暂停
'''
def get_all(cate_url):
    page = 10
    getGoodsLink(cate_url,page)
    # print('ok')

if __name__ == '__main__':
    pool = Pool()

    # pool.map(get_all,data.split())
    get_goods_information()
    pool.close()
    pool.join()



