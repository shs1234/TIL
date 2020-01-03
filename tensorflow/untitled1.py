# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 09:48:05 2019

@author: student
"""

import numpy as np

x=[2,4,6,8]
y=[81,93,91,97]

x_mean=np.mean(x)
y_mean=np.mean(y)

down=[]
for i in range(len(x)):
    down.append((x[i]-x_mean)**2)
    
down_sum=np.sum(down)

print(down_sum)

up=[]
for i in range(len(x)):
    up.append((x[i]-x_mean)*(y[i]-y_mean))
    
up_sum=np.sum(up)

print(up_sum)

lean=up_sum/down_sum

print('기울기:',lean)

b=y_mean-(x_mean*lean)

print('y절편:',b)

