import re
import requests
a='<img alt="" src="xx"/>'
reg = r'src="//(.+?\.jpg)"'    #正则表达式，得到图片地址
b = re.compile(reg)
#b=re.compile(r'src="(.+?\.jpg)" pic_ext' )
imglist = re.findall(b,a)

#r=requests.get(imglist[0])
#r.text
print(imglist[0])