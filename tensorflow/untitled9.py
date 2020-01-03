# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:38:56 2019

@author: student
"""

import numpy
import tensorflow as tf
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation

# 실행할 때마다 같은 결과를 출력하기 위해 설정하는 부분입니다.
seed = 0
numpy.random.seed(seed)
tf.set_random_seed(seed)

# 준비된 수술 환자 데이터를 불러들입니다.
Data_set = numpy.loadtxt('./dataset/ThoraricSurgery.csv',delimiter=',')

# 환자의 기록과 수술 결과를 X와 Y로 구분하여 저장합니다.
X = Data_set[:,0:17]
Y = Data_set[:,17]

# 딥러닝 구조를 결정합니다(모델을 설정하고 실행).
model = Sequential()   
# 첫 번째 은닉층에 input_dim을 적어 줌으로써 첫 번째 Dense가 은닉층 + 입력층의 역할을 겸합니다.
# 데이터에서 17개의 값을 받아 은닉층의 30개 노드로 보낸다 
model.add(Dense(30, input_dim=17, activation='relu'))  #activation : 출력층으로 전달할 때 사용할 활성화 함수
model.add(Dense(1, activation='sigmoid'))  #출력층의 노드 수는 1개, 최종 출력 값에 사용될 활성화 함수

# 딥러닝을 실행합니다. (오차 함수 :  평균 제곱 오차 함수 사용)
model.compile(loss='mean_squared_error', optimizer='adam',metrics=['accuracy'])
model.fit(X, Y, epochs=30, batch_size=10)

# 결과를 출력합니다.
print('\n Accuracy: %.4f' % (model.evaluate(X, Y)[1]))