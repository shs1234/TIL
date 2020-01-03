# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 10:06:31 2019

@author: student
"""

import pandas as pd
import numpy as np
import tensorflow as tf

df = pd.read_csv("./dataset/bmi.csv")

#키와 몸무게 정규화
df["height"] = df["height"] / 200
df["weight"] = df["weight"] / 100

#label 컬럼 변환 - thin[1, 0, 0]/normal[0, 1, 0]/fat [0, 0, 1]
bclass = {"thin": [1, 0, 0] , "normal":[0, 1, 0], "fat": [0, 0, 1]}
df["label_fat"] = df["label"].apply(lambda x: np.array(bclass[x]))

#학습데이터와 테스트 데이터 분류
test_df = df[15000:20000]
test_fat= test_df[["weight", "height"]]
test_ans = list(test_df["label_fat"])

X = tf.placeholder(tf.float32, [None, 2]) #키, 몸무게 데이터 담을 placeholder  선언
Y = tf.placeholder(tf.float32, [None, 3])   #정답 레이블 데이터 담을 placeholder  선언

W = tf.Variable(tf.zeros([2, 3])) 
b = tf.Variable(tf.zeros([3])) 

y = tf.nn.softmax(tf.matmul(X, W) + b)  #소프트맥스 회귀 정의
cross_entropy = -tf.reduce_sum(Y * tf.log(y))  #오차함수 - 교차 엔트로피
train= tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)  #경사하강법으로 학습
 
#예측값, 정답률 계산
predict = tf.equal(tf.argmax(y, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer()) 
for step in range(3501):
    i = (step*100) % 14000
    rows = df[i+1:i+1+100]
    x_fat = rows[["weight", "height"]]
    y_ans =  list(rows["label_fat"])
    sess.run(train, feed_dict={X: x_fat  , Y: y_ans })
    if step%500  == 0 :
        cre = sess.run(cross_entropy, feed_dict={X: x_fat  , Y: y_ans })
        acc = sess.run(accuracy , feed_dict={X: test_fat  , Y: test_ans })
        print("Epoch=", step, "오차=", cre, "정확률(평균)=", acc)