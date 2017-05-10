#爬虫雏形，先mark
import requests
from bs4 import BeautifulSoup
import re
def gethtml(url):
    r=requests.get(url)
    r.encoding=r.apparent_encoding
    return r.text
def getdetail(r,data):
    soup=BeautifulSoup(r,'html.parser')
    a=soup.find_all('a')
    return a
def getpicurl(url,data):
    r=requests.get(url)
    r.encoding=r.apparent_encoding
    soup=BeautifulSoup(r.text,"html.parser")
    a=soup.find_all('img')
    for i in range(len(a)):
        reg = r'src="//(.+?\.jpg)"'  # 正则表达式，得到图片地址
        b = re.compile(reg)
        data.append(re.findall(b, str(a[i])))
    return data

def getpic(data):
    print(len(data))
    for i in range (len(data)):
        url="http://"+str(data[i][0])
        headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H)"}
        print(url)#问题在于http://['xxx']先mark
        r=requests.get(url,headers=headers)
        path = "C://Users/nyhz/Pictures/spiderpic/" +str(i)+ '.jpg'
    #print(url)
    #r.raise_for_status()
        print(path)
        r.encoding = r.apparent_encoding
        with open(path, 'wb') as f:
            f.write(r.content)
    return 'ok'

url1='具体图片的那个页面'
url='网址'
data=[]
a=gethtml(url)
#print(getdetail(a,data))
getpicurl(url1,data)
#print(data[0])
#print(data[0])
getpic(data)


#reg = r'src="//(.+?\.jpg)"'  # 正则表达式，得到图片地址
        #b = re.compile(reg)
        #imglist = re.findall(b, a[i])
        #return imglist
