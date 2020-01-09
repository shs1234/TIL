# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 09:12:05 2019

@author: student
"""
#https://ko.wikipedia.org/wiki/K-%EC%B5%9C%EA%B7%BC%EC%A0%91_%EC%9D%B4%EC%9B%83_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

df=sns.load_dataset('titanic')

df.drop(['deck','embark_town'],axis=1,inplace=True) #없고 중복되는 데이터 열 삭제

df.dropna(subset=['age'],inplace=True) #나이값이 없는 열 삭제

most_freq=df['embarked'].value_counts().idxmax() #가장 많이 승선한 지역 선택
df['embarked'].fillna(most_freq, inplace=True) #embarked 행의 NaN값을 가장 많이 승선한 지역으로 대체

onehot_sex = pd.get_dummies(df['sex'])
df=pd.concat([df, onehot_sex],axis=1)

onehot_embarked = pd.get_dummies(df['embarked'],prefix='town')
df=pd.concat([df,onehot_embarked],axis=1)

X = df[ ['pclass', 'female', 'male', 'age', 'sibsp', 'parch', 'town_C','town_Q','town_S']]
Y = df['survived']

#KNN 분류 분석을 수행하려면 설명변수를 정규화 (평균 0, 표준편차1)
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

# train data: test data 을  7:3으로 데이터 분리
X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.3,random_state=0)

#KNN 분류 분석으로 모델 생성
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,Y_train)

#학습 데이터로부터 생성된 모델로부터 예측값 생성
y_predict=knn.predict(X_test)

knn_metrics=metrics.confusion_matrix(Y_test,y_predict)
print(knn_metrics)
knn_report=metrics.classification_report(Y_test,y_predict)
print(knn_report)