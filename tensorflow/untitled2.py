# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 11:46:01 2019

@author: student
"""

import numpy as np

ab=[3,76]

data=[[2,81],[4,93],[6,91],[8,97]]

x=[i[0] for i in data]
y=[i[1] for i in data]

err=[]
for i in range(len(data)):
    a=x[i]*ab[0]+ab[1]
    err.append(a)
    print(a)


rmse=[]
for i in range(len(y)):
    (err[i]-y[i])
    
    
    
    np.sqrt(((err[i]-y[i])**2)*len(y))


np.sqrt(((err[i]-y[i])**2)*len(y))

print(rmse)

