#我就是测试网反爬虫？
#没有反。。就是忘记加http而已
import requests
r=requests.get("http://"+'xx')

print(r.status_code)