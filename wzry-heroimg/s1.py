# -*- codeing = utf-8 -*-
# @Time : 2021/4/18 14:52
# @Author : 彭晓春
# @File : s1.py
# @Software : PyCharm

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
if __name__ == '__main__':
    url = "https://pvp.qq.com/web201605/herolist.shtml"
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    req = requests.get(url=url,headers = head)
    req.encoding = 'gbk'
    html=req.text
    bs = BeautifulSoup(html, 'lxml')
    txts = bs.find('ul', class_='herolist clearfix')
    links = txts.find_all('a')
    imgs = txts.find_all('img')
    hero_names = []
    hero_urls = []
    for hero in links:
        name = hero.text
        hero_names.insert(0, name)
    for img in imgs:
        src = img.get('src')
        hero_urls.insert(0, src)
    print(hero_names)
    print(hero_urls)
    for i in range(0,len(hero_names)):
        dn_url = "http:"+hero_urls[i]
        urlretrieve(dn_url, 'D:/demo/demo1/spider/img/'+hero_names[i]+'.jpg')
