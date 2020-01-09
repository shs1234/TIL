# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 13:41:33 2019

@author: student
"""

from bs4 import BeautifulSoup
import urllib.request as req
# HTML 가져오기
url = "http://info.finance.naver.com/marketindex/"
res = req.urlopen(url)
# HTML 분석하기
soup = BeautifulSoup(res, "html.parser")
# 원하는 데이터 추출하기 
price = soup.select_one("div.head_info > span.value").string
print("usd/krw =", price)
