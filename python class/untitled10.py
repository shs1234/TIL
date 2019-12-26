# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 15:55:06 2019

@author: student
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.font_manager as fm

from matplotlib import font_manager, rc


df = pd.read_excel('C:/class/data/datas/2019년 11월  교통카드 통계자료.xls', header=None) # 지하철 시간대별 이용현황,
df.head()
# NaN 값 앞에 값으로 채우기
df = df.fillna(method='ffill', axis=1)
print(df.shape)
df.iloc[0,4:52] = df.iloc[0,4:52] + df.iloc[1,4:52]
df.columns = df.iloc[0,:]
df.drop([0,1],inplace=True)
# 불필요 항목 삭제
df.drop(['역ID','작업일시'], axis=1, inplace=True)
print(df.columns)
df.reset_index(drop=True, inplace=True)
df
#1. 지하철 시간대별 이용 현황 데이터 시각화
useage_list = df.iloc[:,4:].sum()
useage_list

#그래프 서식 지정
plt.style.use('ggplot')


useage_list.plot(kind='bar', color='blue', figsize=(20,10))

plt.xlabel('시간 및 승/하차')
plt.ylabel('이용자 수 ')
