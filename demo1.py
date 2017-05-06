
import requests
from bs4 import BeautifulSoup


#http://www.44ttbt.com/
url='http://www.qiushibaike.com/text/'
try:
    r = requests.get(url)

       # 如果响应状态码不是 200，就主动抛出异常
except requests.RequestException as e:
    print(e)



print()
#print(r.text)
print(r.raw.read())

#data = data.decode('UTF-8')
#print(data.text)#响应
#print(data.content)#二进制响应

#soup = BeautifulSoup(['img'],'data.text')
#
#type(soup)


