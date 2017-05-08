import requests

url='https://imgsa.baidu.com/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=f2e674053bfa828bc52e95b19c762a51/060828381f30e924f6416c3144086e061c95f7cd.jpg'
path = "C://Users//nyhz//Pictures//spiderpic"

def getpic(url):
    try:
        path = "C://Users/nyhz/Pictures/spiderpic//1.jpg"
        head={'user-agent':'mozilla/5.0'}
        r=requests.get(url,headers=head)
        print(r.status_code)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
        return '完成'
    except:
        return '异常'
print(getpic(url))

'''
r=requests.get(url)
print(r.status_code)
r.encoding=r.apparent_encoding
r.encoding=r.apparent_encoding


r=requests.get(url)
print(r.status_code)
#r.raise_for_status()
with open(path, 'wb') as f:
    f.write(r.content)


def getpic(url):
    try:
        path = "C://Users/nyhz/Pictures/spiderpic"
        #head={'user-agent':'mozilla/5.0'}
        r=requests.get(url)
        print(r.status_code)
        #r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content) 
        return '完成'
    except:
        return '异常'
print(getpic(url))

'''

