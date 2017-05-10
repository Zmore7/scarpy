import re
import requests
from bs4 import BeautifulSoup
url='http://4444av.co/html/tupian/yazhou/2016/0923/388506.html'
r=requests.get(url)
r.encoding=r.apparent_encoding
soup=BeautifulSoup(r.text,"html.parser")
a=soup.find_all('img')
#print(a)
for i in range(len(a)):
    #print(a[i])
    reg = r'src="//(.+?\.jpg)"'  # 正则表达式，得到图片地址
    b = re.compile(reg)
    imglist = re.findall(b,str(a[i]))
    print(imglist)

