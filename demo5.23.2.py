#我能爬图片的哦~
import requests
import re
from bs4 import BeautifulSoup
def downpic(url,i):
    path = "C://Users/nyhz/Pictures/spiderpic/" + str(i) + '.jpg'
    r=requests.get(url)
    r.encoding=r.apparent_encoding
    with open(path, 'wb') as f:
        f.write(r.content)
    return 0

def getpic(lib):
    #src="https://jp.netcdn.space/digital/video/h_113cb00015/h_113cb00015ps.jpg"
    pattern=re.compile(r'https://jp.netcdn.space/digital/video/.*?jpg',re.S)
    for i in range(len(lib)):
        url=lib[i]
        a=re.findall(pattern,str(url))
        downpic(a[0],i)
    return 'ok'


def main():
    root = 'https://avio.pw/cn/'
    keywords = input()
    url = root + keywords
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, "html.parser")
    img_url = soup.find_all('img')

    i=getpic(img_url)
    print(i)


main()
