'''
Web Request Sample

Author : sokoban@naver.com
'''

import requests
import pandas as pd
from bs4 import BeautifulSoup, Comment
from urllib.parse import quote_plus
from selenium import webdriver

#base setting
UA = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14"

def getWebData(url):
    headers = {'Content-Type': 'application/json; charset=utf-8', 'User-Agent': UA}
    ret = requests.get(url, headers)

    if ret.status_code == 200:
        result = ret.text
    else:
        result = ""

    tables = pd.read_html(result, header=0, encoding='utf-8')
    print(tables)

    sp = BeautifulSoup(result, 'html.parser')
    att = sp.select('div')

    for i in att:
        print(i.select_one('LC20lb MBeuO DKV0Md').text)
        print(i.a.attrs['href'])
        print()


    return result

def googlesearch(url):

    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html)

    r = soup.select('.r')



if __name__ == '__main__':

    f = open("./infoSiteList.txt", "r")
    lines = f.readlines()
    for line in lines:
        print(line)
        getWebData(line)

    print('hello')
