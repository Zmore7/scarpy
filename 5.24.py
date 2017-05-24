import re
import requests

root = 'https://avio.pw/cn/'
keywords = 'f'
url = root + keywords
r = requests.get(url)
r.raise_for_status()
r.encoding = r.apparent_encoding
#print(r.text)
pattern=re.compile(r'https://jp.netcdn.space/digital/video/.*?jpg',re.S)
a=re.findall(pattern,r.text)
print(a)