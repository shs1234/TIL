# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 15:14:19 2019

@author: student
"""

import tensorflow as tf
import numpy as np


#가중치와 바이어스
w11 = np.array([-2, -2])
w12 = np.array([2, 2])

w2 = np.array([1, 1])

b1 = 3
b2 = -1
b3 = -1

#퍼셉트론
def MLP(x, w, b):
    y = np.sum(w*x) + b
    if y<=0:
        return 0
    else :
        return 1

#NAND게이트
def NAND(x1, x2):
    return MLP(np.array([x1, x2]), w11, b1)

#OR게이트
def OR(x1, x2):
    return MLP(np.array([x1, x2]), w12, b2)

#AND게이트
def AND(x1, x2):
    return MLP(np.array([x1, x2]), w2, b3)

#XOR게이트
def XOR(x1, x2):
    return  AND(NAND(x1,x2), OR(x1, x2))

if __name__ =='__main__' :
    for x in [(0, 0), (0, 1), (1, 0), (1, 1)] :
        y = XOR(x[0], x[1])
        print("입력값 :"+str(x) +"   출력값 :"+ str(y))