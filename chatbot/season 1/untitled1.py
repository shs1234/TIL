# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 10:05:39 2020

@author: student
"""

import pandas as pd
import numpy as np




'''
def namecard():
    body = request.json

    url = body['action']['detailParams']['asd']['origin']
    print (url)





    urllib.request.urlretrieve(url, 'namecard.png')

'''
db = pd.read_excel('db.xlsx')
db.set_index('Unnamed: 0', inplace=True)

new_index = db.shape[0]


#데이터 프레임 엑셀로 저장
db.to_excel('db.xlsx')
