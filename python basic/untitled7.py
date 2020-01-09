# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 14:03:39 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

#데이터 불러오기
df=pd.read_csv('https://raw.githubusercontent.com/rasbt/python-machine-learning-book-2nd-edition/master/code/ch10/housing.data.txt',header=None,sep='\s+')
df.columns=['CRIM', 'ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']

#데이터셋의 중요 특징 시각화
cols=['LSTAT','INDUS','NOX','RM','MEDV']
#sns.pairplot(df[cols],height=2.5)
#plt.tight_layout()
#plt.show()
'''
sns.pairplot(df)
plt.show()
'''

'''#상관관계 heatmap으로 표시
cm=np.corrcoef(df[cols].values.T)
sns.set(font_scale=1.5)
hm=sns.heatmap(cm,square=True,cbar=True,annot=True, annot_kws={'size':15},fmt='.2f')
plt.tight_layout()
plt.show()
'''
X=df['RM'].values
Y=df['MEDV'].values


lr=LinearRegression()
sc_x=StandardScaler()
sc_y=StandardScaler()
X_std=sc_x.fit_transform(X)
Y_std=sc_x.fit_transform(Y[:,np.newaxis]).flatten()

lr.fit(X,Y)