# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 15:43:58 2019

@author: student
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

score=[56,60,61,67,69, 55,70,44,51,64, 60,50,68,72,90, 93,85,74,81,88, 92,97,77,78,98]
grade=[3.61, 2.93, 3.14, 4.00, 3.23,  3.89, 3.66, 3.51, 2.53, 3.61,  2.93, 3.14, 4.00, 3.23, 2.53, 3.23, 3.89, 3.66, 3.51, 3.89,  3.66, 3.51, 2.53 ,3.14, 4.00]
_pass = [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

df = pd.DataFrame( {"score":score, "grade": grade, "_pass":_pass})
print(df.info())

X=df[['score', 'grade']]
Y=df[['_pass']]

# train data 와 test data를 7:3 비율로 분리
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)   


from sklearn.linear_model import LogisticRegression 
logR = LogisticRegression() 
logR.fit(X_train, Y_train)   #학습

print('정확도: ' , logR.score(X_train, Y_train))
print('정확도: ' , logR.score(X_test, Y_test))


from sklearn.metrics import classification_report
y_predict = logR.predict(X_test)
print(classification_report(Y_test, y_predict ))   #실제 합격/불합격 테스트 데이터,  모형으로부터 예측된 합격/불합격 테스트 데이터 
