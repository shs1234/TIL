# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:19:35 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('C:/class/data/datas/auto-mpg.csv', header=None)
df.columns=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

pd.set_option('display.max_columns',10)
print(df.head())
df.info()
df.describe()
print(df['horsepower'].unique())
df['horsepower'].replace('?', np.nan,inplace=True)
df.dropna(subset=['horsepower'],axis=0,inplace=True)
df['horsepower']=df['horsepower'].astype('float')
print(df.describe())

ndf=df[['mpg','cylinders','horsepower','weight']]

ndf.plot(kind='scatter',x='weight',y='mpg',c='red',s=10,figsize=(10,5))
plt.show()
plt.close()

fig=plt.figure(figsize=(10,5))
ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)

sns.regplot(x='weight',y='mpg',data=ndf,ax=ax1)
sns.regplot(x='weight', y='mpg', data=ndf, ax=ax1, fit_reg=False)
plt.show()
plt.close()

sns.jointplot(x='weight', y='mpg', data=ndf)
sns.jointplot(x='weight', y='mpg', data=ndf, kind='reg')  #회귀선 표시
plt.show()
plt.close()