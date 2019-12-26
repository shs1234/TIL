# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 11:31:49 2019

@author: student
"""

from sklearn import svm
import seaborn as sns
import pandas as pd

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

from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

# train data: test data 을  7:3으로 데이터 분리
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.3,random_state=0)


svm_model=svm.SVC(kernel='rbf', gamma='auto')
svm_model.fit(X_train,Y_train)


y_predict=svm_model.predict(X_test)
from sklearn import metrics
svm_metrics=metrics.confusion_matrix(Y_test,y_predict)
print(svm_metrics)
svm_report=metrics.classification_report(Y_test,y_predict)
print(svm_report)