# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 14:16:35 2019

@author: student
"""
'''
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
#print(Y_obj.unique())

e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)            # 문자열 변환

model = Sequential()              # 모델 설정
model.add(Dense(24, input_dim=60, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='mean_squared_error',   optimizer='adam',    metrics=['accuracy'])  # 모델 컴파일
model.fit(X, Y, epochs=200, batch_size=10)                      # 모델 실행
print("\n Accuracy: %.4f" % (model.evaluate(X, Y)[1]))     # 결과 출력


'''
############################################


from keras.models import Sequential, load_model
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

# 학습셋과 테스트셋의 구분
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=seed)

model = Sequential()
model.add(Dense(24, input_dim=60, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='mean_squared_error',    optimizer='adam',    metrics=['accuracy'])
#학습 데이터로 학습
model.fit(X_train, Y_train, epochs=130, batch_size=5)
model.save('./output/my_model.h5')   # 학습을 통해 생성된 모델을 컴퓨터에 저장

del model   # 테스트를 위해 메모리 내의 모델을 삭제
model = load_model('./output/my_model.h5')   # 모델을 새로 불러옴

print("\n Test Accuracy: %.4f" % (model.evaluate(X_test, Y_test)[1]))   # 불러온 모델로 테스트 실행