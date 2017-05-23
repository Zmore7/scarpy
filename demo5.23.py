#爬淘宝的，穆克，先mark一下
import requests
import re


def getHtmltext(url):
    try:
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        return ''


def parsePage(ilt, html):
    print()


def printGoodsList(ilt):
    print()


def main():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infolist = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHtmltext(url)
            parsePage(infolist, html)
        except:
            continue
        printGoodsList(infolist)
