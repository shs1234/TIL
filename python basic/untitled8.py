# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 15:06:35 2019

@author: student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression 

#1단계: 데이터 준비
df = pd.read_csv('C:/class/data/datas/auto-mpg.csv', header=None)
print(df.info()) 


#컬럼 이름 (변수, 특성 이름) 지정
df.columns=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# horsepower열에서 ?를 NaN값으로 대체
df['horsepower'].replace('?', np.nan, inplace=True) 
#horsepower열이 NaN인 행을 삭제
df.dropna(subset=['horsepower'], axis=0, inplace=True)
#문자열 데이터를 실수형 데이터로 변환
df['horsepower'] = df['horsepower'].astype('float')

#3단계 : 분석에 사용할 특성(열, 변수) 선택 (연비, 실린더, 마력, 중력)
ndf = df[[ 'mpg', 'cylinders','horsepower', 'weight' ]]


# 4단계 : 훈련 데이터와 테스트 데이터로 분리
X= ndf[['cylinders', 'horsepower', 'weight']]   #독립변수 X : 무게
Y=ndf['mpg']    #종속변수 Y : 연비


# train data 와 test data를 7:3 비율로 분리
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=10)  #랜덤 추출값 10

#5단계 : 다중 회귀분석  


lr = LinearRegression()  #단순 선형회귀분석 객체 생성

lr.fit(X_train, Y_train)  #학습 => 모델 생성

r_square = lr.score(X_test, Y_test) # 결정 계수 계산
print(r_square )    #결정 계수 :  

print('기울기 a : ', lr.coef_)
print('절편 b : ', lr.intercept_)
#기울기 a :  
# 절편 b :   


y_predict =lr.predict(X_test)   #독립변수에 대한 예측된 종속변수값 

plt.figure(figsize=(10, 5))
ax1 = sns.distplot(Y, hist=False, label='Y_test')
ax2 = sns.distplot(y_predict, hist=False, label='y_predict', ax=ax1)
plt.show()
plt.close()