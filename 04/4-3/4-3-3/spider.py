import hashlib
import time
from random import randint

import requests

proxies = {
    "http": "http://127.0.0.1:8888",
    "https": "https: // 127.0.0.1: 8888",
}


class Youdao(object):
    """
    破解有道词典
    """

    def __init__(self, value):
        self.app_version = '5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
        self.start_url = 'http://fanyi.youdao.com/'
        self.translate_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.value = value
        self.time = str(round(time.time()))
        time.sleep(1)

    @staticmethod
    def hex5(code):
        """
        MD5加密
        """
        manipulator = hashlib.md5()
        manipulator.update(code.encode('utf-8'))
        return manipulator.hexdigest()

    def get_sign(self, salt):
        """
        获取sign参数
        """
        return self.hex5('fanyideskweb'+self.value+salt+']BjuETDhU)zqSxf-=B#7m')

    @property
    def _args(self):
        """
        获取Post参数
        """
        ts = str(round(time.time()))
        bv = self.hex5(self.app_version)
        salt = ts+str(randint(1, 9))
        sign = self.get_sign(salt)
        return {'ts': ts, 'bv': bv, 'salt': salt, 'sign': sign}

    @property
    def _cookie(self):
        """
        获取cookie
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
        }
        response = requests.get(
            url=self.start_url, headers=headers)
        return ';'.join([f'{cookie.name}={cookie.value}' for cookie in response.cookies])

    def translate(self):
        """
        进行翻译
        """
        post_data = {
            'i': self.value,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self._args.get('salt'),
            'sign': self._args.get('sign'),
            'lts': self._args.get('ts'),
            'bv': self._args.get('bv'),
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'OUTFOX_SEARCH_USER_ID=-1709221799@10.108.160.18; JSESSIONID=aaaeDhwYtihO1dXnsdDvx; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcB_lhiel_0Adv0wdDvx; OUTFOX_SEARCH_USER_ID_NCOO=1670706700.330219; _ntes_nnid=5e4a8c699c8d09f42631671a8973bb82,1603584041008; ___rl__test__cookies=1603590871786',
            # 'Cookie': self._cookie,
            # 'Cookie': 'OUTFOX_SEARCH_USER_ID=624778838@10.108.160.17; JSESSIONID=aaabA8zkGlgXnhsycZJvx; OUTFOX_SEARCH_USER_ID_NCOO=1287106614.80098; ___rl__test__cookies=1603697192597',
            'Host': 'fanyi.youdao.com',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        try:
            response = requests.post(
                url=self.translate_url, headers=headers, data=post_data)
            print(response.status_code)
            print(response.json())
            response.raise_for_status()
        except Exception as e:
            raise e


if __name__ == "__main__":
    # value = input('请输入带翻译的字符: ')
    youdao = Youdao('编程')
    youdao.translate()
