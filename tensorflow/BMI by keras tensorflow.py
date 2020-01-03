# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 10:41:54 2019

@author: student
"""

import pandas as pd
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import EarlyStopping


df = pd.read_csv("./dataset/bmi.csv")

#키와 몸무게 정규화
df["height"] /= 200
df["weight"] /= 100

X = df[["weight", "height"]].as_matrix()

#label 컬럼 변환 - thin[1, 0, 0]/normal[0, 1, 0]/fat [0, 0, 1]
bclass = {"thin": [1, 0, 0] , "normal":[0, 1, 0], "fat": [0, 0, 1]}
Y = np.empty((20000, 3))
for i, v in enumerate(df["label"]):
    Y[i] = bclass[v]
 
#학습데이터 , 테스트 데이터 분리
X_train, Y_train = X[1:15001], Y[1:15001]
X_test, Y_test = X[15001:20001], Y[15001:20001]

model = Sequential()  #모델 객체 생성
model.add(Dense(512, input_shape=(2, )))    #Dense(노드 수 , ....) 층을 의미하는 객체
model.add(Activation('relu'))   # 활성화 함수
model.add(Dropout(0.1))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(3))      # 분류하고 싶은 클래스 수 만큼 출력으로 구성
model.add(Activation('softmax'))  #활성화 함수

model.compile(loss="categorical_crossentropy", optimizer="rmsprop", metrics=['accuracy'])
hist = model.fit(X_train, Y_train, batch_size=100, nb_epoch=20, validation_split=0.1, callbacks=[EarlyStopping(monitor='val_loss', patience=2)], verbose=1)
                    
score = model.evaluate(X_test, Y_test)
print("loss=", score[0])
print("accuracy=", score[1])



# weight decay( 가중치 감소) - 학습중 가중치가 큰 것에 대해서 패널티를 부과해 과적합의 위험을 줄이는 방법
# Dropout - 복잡한 신경망에서 가중치 감소만으로 과적합을 피하기 어려운 경우 뉴런의 연결을 임의로 삭제시켜 신호를 전달하지 못하도록 하는 방법
# softmax 회귀 - 입력받은 값을 출력으로 0~1사이의 값으로 모두 정규화하여 출력값들의 총합은 항상 1이 되는 특성의 함수
#                       분류하고 싶은 클래스 수 만큼 출력으로 구성
