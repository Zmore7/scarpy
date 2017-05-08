import requests
from bs4 import BeautifulSoup
ip=input()
url='http://m.ip138.com/ip.asp?ip='+ip
r=requests.get(url)
obs=BeautifulSoup(r.text,"html.parser")
p=obs.find_all('p')
q=p[-1].get_text()
#print(obs)
a=str(q).split('：')[-1]
print(a)


#print(r.text[-500:])