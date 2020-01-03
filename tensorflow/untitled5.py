# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 14:04:03 2019

@author: student
"""


#로지스틱 회귀분석 (시그모이드 함수)

import numpy as np
import tensorflow as tf

data = [[2,0],[4,0],[6,0],[8,1],[10,1],[12,1],[14,1]]

# x 값과 y 값
x_data= [ i[0] for i in data]
y_data= [ i[1] for i in data]

a = tf.Variable(tf.random_uniform([1], dtype=tf.float64, seed=0))   #기울기 범위
b = tf.Variable(tf.random_uniform([1], dtype=tf.float64, seed=0))   #y절편 범위

#시그모이드 함수 방정식 정의
y=1/(1+np.e**(a*x_data+b))

loss=-tf.reduce_mean(np.array(y_data)*tf.log(y)+(1-np.array(y_data))*tf.log(1-y))

learning_rate = 0.5

# 오차 rmse 값이 최소인 값 찾는 식 정의
gradient_descent = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

#텐서플로으로 학습
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())     # 변수들을 메모리에 생성, 초기화
    for step in range(6001):
        sess.run(gradient_descent)
        if step % 1000 == 0:
            print("Epoch: %.f , Loss=%.4f,  기울기 a=%.4f, 절편 b= %.4f" % (step, sess.run(loss), sess.run(a), sess.run(b)))

#Epoch는 입력값에 대해 몇 번 반복 실험했는지를 나타내는 용어