import json

import requests

# Splash 接口
render = 'http://localhost:8050/execute'
# 需要执行的命令
with open('5-2-3-one.lua', 'r', encoding='utf-8') as file:
    script = file.read()
# 设置请求头
header = {'content-type': 'application/json'}
# 按照Splash规定提交命令
data = json.dumps({"lua_source": script})
# 向Splash接口发出请求并携带上请求头和命令参数
resp = requests.post(render, data=data, headers=header)
# 打印返回的json
print(resp.json())
