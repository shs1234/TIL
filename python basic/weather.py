# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 16:05:17 2019

@author: student
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

data=pd.read_csv('C:/class/data/datas/weather.csv')

cols=['Temp', 'Sunshine',  'Humidity', 'Pressure', 'Cloud', 'RainToday' , 'RainTomorrow']

df=pd.DataFrame(data,columns=cols)
df.dropna(inplace=True)

df['RainTomorrow']=df['RainTomorrow'].map({'Yes':1,'No':0})
df['RainToday']=df['RainToday'].map({'Yes':1,'No':0})

X=df[['Temp', 'Sunshine',  'Humidity', 'Pressure', 'Cloud']]
Y=df['RainTomorrow']

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, train_size=0.7,random_state=0)

logR=LogisticRegression(solver='liblinear')
logR.fit(X_train,Y_train)

print('정확도: ' , logR.score(X_train, Y_train))
print('정확도: ' , logR.score(X_test, Y_test))

y_predict=logR.predict(X_test)
print(classification_report(Y_test, y_predict))