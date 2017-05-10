import requests

url = 'https://imgsa.baidu.com/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=f2e674053bfa828bc52e95b19c762a51/060828381f30e924f6416c3144086e061c95f7cd.jpg'
url1='http://i1.1100lu.xyz/1100/201604/19/5l3up2p43fu.jpg'
#root = "C://Users/nyhz/Pictures/spiderpic"

r = requests.get(url1)
path = "C://Users/nyhz/Pictures/spiderpic/"+url.split('/')[-1]
print(path)
r.encoding = r.apparent_encoding
with open(path, 'wb') as f:
    f.write(r.content)

def getpic(url):
    try:
        head = {'user-agent': 'mozilla/5.0'}
        r = requests.get(url, headers=head)
        path = "C://Users/nyhz/Pictures/spiderpic" + url.split('/')[-1]
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        with open(path, 'wb') as f:
            f.write(r.content)
        return '完成'
    except:
        return '异常'

#print(getpic(url))
