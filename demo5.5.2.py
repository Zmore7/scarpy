import requests
#requests的post方法，数组放form，数据放data
fa={'fasd':'fdfda','fsd':'23r'}
r=requests.post('http://httpbin.org/post', data= fa)
print(r.text)
