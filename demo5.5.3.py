#百度搜索

import requests

keyword='python'
kv={'wd':keyword}
url='http://www.baidu.com/s'
try:
    r=requests.get(url,params=kv)
    print(r.text)
except:
    print('error')