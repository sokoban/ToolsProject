#-*- coding: utf-8 -*-
'''
Web Request Sample
Author : sokoban@naver.com
'''

import requests
import pandas as pd
from bs4 import BeautifulSoup, Comment
from urllib.parse import quote_plus
from selenium import webdriver
from urllib.parse import unquote

#base setting
UA = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14"


def getWebData(url):
    headers = {'Content-Type': 'application/json; charset=utf-8', 'User-Agent': UA}

    driver = webdriver.Chrome('/Users/hyunggi.kim/Documents/chromedriver')
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html)

    v = soup.select('.yuRUbf')
    result = ""

    for i in v:
        ret1 = ""
        ret1 = ret1 + i.select_one('.LC20lb.DKV0Md').text + "\n"
        ret1 = ret1 + i.a.attrs['href'] + "\n"
        ret1 = ret1 + "\n"
        result = result + quote_plus(ret1)

    result2 = { 'text': unquote(result) }

    driver.close()
    #result = quote_plus(result)
    print(result )
    ret = requests.post("", json=result2)
    print(ret)


if __name__ == '__main__':

    f = open("./infoSiteList.txt", "r")
    lines = f.readlines()
    for line in lines:
        print(line)
        getWebData(line)

