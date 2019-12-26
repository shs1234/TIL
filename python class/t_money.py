'''
1. 지하철 시간대별 이용 현황 데이터 시각화
2. 출근 시간대 (7시 ~9시) 가장 많이 타고 내리는 역 찾기
3. 밤 11시에 가장 많이 타는 역 찾기
'''

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel('C:/class/data/datas/2019년 11월  교통카드 통계자료.xls',sheet_name='지하철 시간대별 이용현황',header=[0,1],thousands=',')

df_cols=df.iloc[:,4:51]
df_colsT=df_cols.T
df_sum=df_colsT.sum(axis=1)
ex1=df_sum.unstack()

#2출근 시간대 (7시 ~9시) 가장 많이 타고 내리는 역 찾기
ex2=df_colsT.iloc[6:10,:]
ex2T=ex2.T
ex2_sum=ex2T.sum(axis=1)
print('2. 출근 시간대 가장 많이 타고 내리는 역 : ',df.iloc[ex2_sum.idxmax(),3])

#3밤 11시에 가장 많이 타는 역 찾기
print('3. 밤 11시에 가장 많이 타는 역 :',df.iloc[df['23:00:00~23:59:59']['승차'].idxmax(),3])

#1지하철 시간대별 이용 현황 데이터 시각화
print('1. 지하철 시간대별 이용 현황 데이터 시각화')
plt.plot(ex1)

