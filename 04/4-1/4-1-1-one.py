import requests
from parsel import Selector

url = 'http://localhost:8205/verify/uas/index.html'
# 向目标网址发起网络请求
response = requests.get(url)
# 输出请求头
for header in response.headers.items():
    print(header)

# 打印输出状态码
print(response.status_code)
# 如果本次请求的状态码为200则继续，否则提示失败
if response.status_code == 200:
    sel = Selector(response.text)
    # 根据HTML标签和属性从响应正文中提取新闻标题
    res = sel.css('.list-group-item::text').extract()
    print(res)
else:
    print('This request is fial.')
