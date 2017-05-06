import requests

#爬虫框架
def gethtml(url):
    try:
        kv ={'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers=kv)
        r.raise_for_status()#抛出异常
        r.encoding=r.apparent_encoding
        return  r.status_code#r.text[1000:2000]
    except:
        return '异常'

url='https://www.amazon.cn/dp/B00J580BKM/ref=cngwdyfloorv2_recs_0/457-6640715-2122237?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2&pf_rd_r=1FAN4DHEBHTS4JPX19X9&pf_rd_r=1FAN4DHEBHTS4JPX19X9&pf_rd_t=36701&pf_rd_p=78d99717-ba38-48ca-89aa-e501d77b022f&pf_rd_p=78d99717-ba38-48ca-89aa-e501d77b022f&pf_rd_i=desktop'

print(gethtml(url))







