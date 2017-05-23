#这个就当判断吧
import requests
from bs4 import BeautifulSoup

#url='http://www.btmeet.org/search/'+'fa'
url='https://avio.pw/cn'
#add_header={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}
r=requests.get(url)
r.encoding=r.apparent_encoding
print(r.status_code)
print(r.text)
