# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 13:40:23 2019

@author: student
"""

#다중 경사하강법

import tensorflow as tf
#시간,점수,과외횟수
data = [[2,81,0],[4,93,4],[6,91,2],[8,97,3]]

# x 값과 y 값
x_data= [ i[0] for i in data]
y_data= [ i[1] for i in data]
z_data= [ i[2] for i in data]

#임의의 기울기와 y절편의 값으로 변수로 정의
a = tf.Variable(tf.random_uniform([1], 0, 10, dtype=tf.float64, seed=0))   #기울기 범위 0~10
b = tf.Variable(tf.random_uniform([1], 0, 100, dtype=tf.float64, seed=0))   #y절편 범위 0~100
c = tf.Variable(tf.random_uniform([1], 0, 10, dtype=tf.float64, seed=0))   #두번째 항 범위 0~10

y = a*x_data+c*z_data+b  #1차방정식의 계산식 정의

#오차 계산 (평균 제곱근 오차 공식)
rmse = tf.sqrt(tf.reduce_mean(tf.square(y-y_data)))

#학습률
learning_rate = 0.1

# 오차 rmse 값이 최소인 값 찾는 식 정의
gradient_descent = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)

#텐서플로으로 학습
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())     # 변수들을 메모리에 생성, 초기화
    for step in range(4001):
        sess.run(gradient_descent)
        if step % 100 == 0:
            print("Epoch: %.f , RMSE=%.4f,  기울기 a=%.4f, 절편 b= %.4f, 과외 c=%.4f" % (step, sess.run(rmse), sess.run(a), sess.run(b), sess.run(c)))

#Epoch는 입력값에 대해 몇 번 반복 실험했는지를 나타내는 용어