# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 15:27:01 2019

@author: student
"""

import pandas as pd
import numpy as np
from sklearn.datasets import make_blobs


uci_path='https://archive.ics.uci.edu/ml/machine-learning-databases/00292/Wholesale%20customers%20data.csv'
df = pd.read_csv(uci_path, header=0)

X,y=make_blobs(n_samples=150,centers=3,cluster_std=0.5,random_state=0)

import matplotlib.pyplot as plt

plt.scatter(X[:,0],X[:,1],c='white',marker='o',edgecolors='black',s=50)
plt.grid()
plt.tight_layout()
plt.show()

from sklearn.cluster import KMeans

km=KMeans(n_clusters=3,init='random',max_iter=300,tol=0.0001,random_state=0)
y_km=km.fit_predict(X)



plt.scatter(X[y_km == 0, 0],
            X[y_km == 0, 1],
            s=50, c='lightgreen',
            marker='s', edgecolor='black',
            label='cluster 1')
plt.scatter(X[y_km == 1, 0],
            X[y_km == 1, 1],
            s=50, c='orange',
            marker='o', edgecolor='black',
            label='cluster 2')
plt.scatter(X[y_km == 2, 0],
            X[y_km == 2, 1],
            s=50, c='lightblue',
            marker='v', edgecolor='black',
            label='cluster 3')
plt.scatter(km.cluster_centers_[:, 0],
            km.cluster_centers_[:, 1],
            s=250, marker='*',
            c='red', edgecolor='black',
            label='centroids')
plt.legend(scatterpoints=1)
plt.grid()
plt.tight_layout()
plt.show()