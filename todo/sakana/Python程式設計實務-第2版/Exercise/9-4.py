# -*- coding: utf-8 -*-
# 程式 9-4 (Python 3 version)

import requests, re

#正規化表示式找出 e-mail
regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
#url = 'http://xxxx.xxx.xxx'
# 找網頁中有 電子郵件的 URL 測試
url = 'https://www.nchc.org.tw/posts/AGW1mIivFC/%E4%BA%A4%E9%80%9A%E8%88%87%E8%81%AF%E7%B5%A1%E8%B3%87%E8%A8%8A'

html = requests.get(url).text

# re.findall(pattern, string, flags=0)
emails = re.findall(regex,html)
# 列出符合正規化表示式的 e-mail
for email in emails:
    print(email)
