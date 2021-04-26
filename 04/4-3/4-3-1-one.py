import hashlib
from random import randint, sample
from time import time

import requests


def hex5(value):
    # 使用 md5 加密值并返回加密后的字符串
    manipulator = hashlib.md5()
    manipulator.update(value.encode('utf-8'))
    return manipulator.hexdigest()


# 生成1-9之间的5个随机数字
action = "".join([str(randint(1, 9)) for _ in range(5)])
# 生成当前时间戳
tim = round(time())
# 生成5个随机大写字母
randstr = "".join(sample([chr(_) for _ in range(65, 91)], 5))
# 三个参数拼接后进行md5加密
value = action+str(tim)+randstr
hexs = hex5(value)
print(action, tim, randstr, hexs)


def uri():
    args = '?actions={}&tim={}&randstr={}&sign={}'.format(
        action, tim, randstr, hexs)
    return args


url = 'http://localhost:8206/fet' + uri()
resp = requests.get(url)
print(resp.status_code, resp.text)
