import requests
from lxml import etree
from requests.utils import dict_from_cookiejar
from requests import Session

SESSION=Session()

url = 'http://localhost:8207/verify/cookie/content.html'
# 向目标网址发起网络请求
response=SESSION.get(url=url)
# response = requests.get(url)
# 打印输出状态码
print(response.status_code)
# 打印输出当前cookies
print(dict_from_cookiejar(response.cookies))
response=SESSION.get(url=url)
# 如果本次请求的状态码为200则继续，否则提示失败
if response.status_code == 200:
    # 将响应正文赋值给html变量
    html = etree.HTML(response.text)
    # 根据HTML标签和样式属性从文本中标题的Element对象
    title = html.cssselect('.page-header h1')[0].text
    print(title)
else:
    print('This request is fial.')
