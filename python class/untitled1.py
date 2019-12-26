# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:31:57 2019

@author: student
"""

import pandas as pd
import matplotlib.pyplot as plt


#시도별 전출입 인구수.xlsx파일을 결측치는 0으로 대체,  첫번째 행을 header로 데이터 프레임 생서
data=pd.read_excel('C:\class\data\datas/시도별 전출입 인구수.xlsx',fillna=0,header=0)
df=pd.DataFrame(data)


#데이터 프레임의 데이터중 누락값을 찾아서 앞 행의 동일컬럼의 값으로 채웁니다.
df = df.fillna(method='ffill')

#서울에서 다른 지역으로 이동한 데이터만 추출합니다.
mask = (df['전출지별'] =='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별': '전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

#서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']

plt.plot(sr_one.index, sr_one.values)
#plt.plot(sr_one)

#제목 추가
plt.title('transfer')
plt.plot(sr_one.index, sr_one.values, marker='o', markersize=5)


#축 이름 
plt.xlabel('year')
plt.ylabel('pop count')
plt.legend(labels=['seoul->kyungki'], loc='best')
plt.xticks(rotation='vertical')
plt.figure(figsize=(14, 5))

plt.show()   # 
