import requests
#from urllib import request
from bs4 import BeautifulSoup
ip=input()
#'202.204.80.1'
# input()
url='http://m.ip138.com/ip.asp?ip='+ip
r=requests.get(url)
obs=BeautifulSoup(r.text,"html.parser")
q=obs.find_all('p')[-1].get_text()
a=str(q).split('：')[-1]

print(a)


#print(r.text[-500:])