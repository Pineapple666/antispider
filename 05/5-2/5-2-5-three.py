#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2021-04-26 14:11
# @Author   : Pineapple
# @Email    : pineapple_cpp@163.com
# @File     : 5-2-5-three.py
# @Desc     : 5.2.5第三个splash示例

# import lib
import json

import requests

# splash 接口
splash_api = 'http://localhost:8050/execute'
# 读取lua脚本
with open('5-2-5-three.lua', 'r', encoding='utf-8') as file:
    lua_script = file.read()

# # 设置请求头
headers = {'content-type': 'application/json'}
# 提交命令
data = json.dumps({'lua_source': lua_script})
res = requests.post(splash_api, data=data, headers=headers)
res_json = res.json()
png_str = res_json.get('png')

png_api = 'data:image/png;base64,' + png_str

res = requests.get(url=png_api)

with open('ituring_splash.png', 'wb') as file:
    file.write(res.content())
