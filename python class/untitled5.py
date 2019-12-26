# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:37:12 2019

@author: student
"""


import pandas as pd
import numpy as np

data1=pd.read_csv('C:/class/data/datas/dpu.csv')
data2=pd.read_csv('C:/class/data/datas/dau.csv')
data3=pd.read_csv('C:/class/data/datas/install.csv')

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
df3=pd.DataFrame(data3)

df1.drop('app_name', inplace=True, axis=1)
df2.drop('app_name', inplace=True, axis=1)
df3.drop('app_name', inplace=True, axis=1)

df4=pd.merge(df3,df2,on='user_id',how='outer')
df5=pd.merge(df4,df1,on=['user_id','log_date'],how='outer')

df5['payment'].fillna(0,inplace=True)
df5.set_index('user_id',inplace=True)

df5['install_date']=pd.to_datetime(df5['install_date'])
df5['month']=df5['install_date'].dt.month

group_month=df5['payment'].groupby(df5['month'])
print(group_month.sum())