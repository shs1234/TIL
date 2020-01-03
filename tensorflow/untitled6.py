# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 14:26:18 2019

@author: student
"""

#다중 로지스틱 회귀분석 (시그모이드 함수), tf.sigmoid() 함수 사용

import tensorflow as tf 
import numpy as np

x_data = np.array( [[2,3],[4,3],[6,4],[8,6],[10, 7], [12, 8], [14, 9]] )
y_data= np.array([0, 0, 0, 1, 1, 1,1] ).reshape(7, 1)

#입력값을 placeholder에 저장
X= tf.placeholder(tf.float64, shape=[None, 2])
Y = tf.placeholder(tf.float64, shape=[None, 1])
 
#실행할 때마다 동일한 출력(결과)를 얻기 위한 값 설정
seed = 0
np.random.seed(seed)
tf.set_random_seed(seed)

#임의의 a, b 값을 변수로 정의
a = tf.Variable(tf.random_uniform([2, 1], dtype=tf.float64))  #[2, 1]은 들어오는  값은 2개 나가는 값은 1개
b = tf.Variable(tf.random_uniform([1], dtype=tf.float64))

#시그모이드 함수 방정식 정의
y = tf.sigmoid(tf.matmul(X, a) + b)

#오차 loss 구하는 함수
loss = -tf.reduce_mean(Y*tf.log(y)+(1-Y)*tf.log(1-y))

#학습률
learning_rate = 0.1

# 오차 loss 값이 최소인 값 찾는 식 정의
gradient_descent = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

predicted = tf.cast(y >0.5, dtype=tf.float64)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float64))

#tf.cast() 함수는 형변환(캐스팅) 수행 => 부동소수점형(실수)를 정수형으로 변환할때는 소수점이하 버림
                                                    #bool (논리) 자료형을 정수형으로 변환할때는 True는 1, False는 0으로

#텐서플로 이용하여 학습
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())     # 변수들을 메모리에 생성, 초기화
    for step in range(5001):
        a_, b_, loss_, _ = sess.run([a, b, loss, gradient_descent], feed_dict={X:x_data, Y:y_data})
        if step % 500 == 0:
            print("Epoch: %.f , loss=%.4f,  기울기 a1=%.4f, 기울기 a2=%.4f, 절편 b= %.4f" % (step,  loss_,  a_[0], a_[1],  b_))