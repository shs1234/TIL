# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:53:24 2019

@author: student
"""

# 10개의 파일로 쪼개 테스트하는?10-fold cross validation을 실시하도록?n_fold의 값을 10으로 설정한 뒤?StratifiedKFold()?함수에 적용했습니다. 그런 다음 모델을 만들고 실행하는 부분을?for?구문으로 묶어?n_fold만큼 반복되게 합니다.
from keras.models import Sequential 
from keras.layers.core import Dense
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy
import tensorflow as tf

seed = 0
numpy.random.seed(seed)        # seed 값 설정
tf.set_random_seed(seed)

df = pd.read_csv('./dataset/sonar.csv', header=None)           # 데이터 입력
dataset = df.values
X = dataset[:,0:60]
Y_obj = dataset[:,60]

e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)            # 문자열 변환


from sklearn.model_selection import StratifiedKFold

n_fold = 10  #10겹 
skf = StratifiedKFold(n_splits=n_fold, shuffle=True, random_state=seed)

accuracy = []  # 빈 accuracy 배열

for train, test in skf.split(X, Y):  # 모델의 설정, 컴파일, 실행
    model = Sequential()
    model.add(Dense(24, input_dim=60, activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='mean_squared_error',  optimizer='adam',   metrics=['accuracy'])
    model.fit(X[train], Y[train], epochs=100, batch_size=5)
    k_accuracy = "%.4f" % (model.evaluate(X[test], Y[test])[1])
    accuracy.append(k_accuracy)

# 결과 출력
print("\n %.f fold accuracy:" % n_fold, accuracy)