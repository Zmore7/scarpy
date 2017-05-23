import requests
import re
from bs4 import BeautifulSoup
def downpic(url):

    return

def getpic(lib):
    #src="https://jp.netcdn.space/digital/video/h_113cb00015/h_113cb00015ps.jpg"
    pattern=re.compile(r'src="https://()')
    for i in range(len(lib)):
        url=lib[i]

    return url


def main():
    root = 'https://avio.pw/cn/'
    keywords = 'f'
    url = root + keywords
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, "html.parser")
    img_url = soup.find_all('img')

    i=getpic(img_url)
    print(i)


main()
