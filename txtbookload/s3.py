# -*- codeing = utf-8 -*-
# @Time : 2021/4/24 9:44
# @Author : 彭晓春
# @File : s3.py
# @Software : PyCharm

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def get_content(url):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
            }
    req = requests.get(url=url, headers=head)
    req.encoding = "utf-8"
    html = req.text
    bs = BeautifulSoup(html,'lxml')
    txts = bs.find('div',id='content')
    content = txts.text.strip('').split('\xa0' * 4)
    return content

if __name__ == '__main__':
    target = "http://www.xbiquge.la/15/15409/"
    book_name = "牧神记.txt"
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/75.0.3770.100 Safari/537.36"
            }
    req = requests.get(url=target, headers=head)
    req.encoding = "utf-8"
    html = req.text
    bs = BeautifulSoup(html, 'lxml')
    chapter_bs = bs.find('div', id='list')
    chapters = chapter_bs.find_all('a')
    server = "http://www.xbiquge.la"
    for chapter in tqdm(chapters):
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')
