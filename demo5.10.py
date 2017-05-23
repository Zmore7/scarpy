import requests
from bs4 import BeautifulSoup

url='http://www.kepuchina.cn/qykj/yykx/201705/t20170510_197033.shtml'
r=requests.get(url)
r.encoding=r.apparent_encoding
soup=BeautifulSoup(r.text,"html.parser")
img=soup.find_all('img')
print(img)