# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 15:49:19 2019

@author: student
"""

import pandas as pd
uci_path='https://archive.ics.uci.edu/ml/machine-learning-databases/00292/Wholesale%20customers%20data.csv'
df = pd.read_csv(uci_path, header=0)

X=df.iloc[ : , : ]

from sklearn import preprocessing
X=preprocessing.StandardScaler().fit(X).transform(X)

from sklearn import cluster
kmeans = cluster.KMeans(init='k-means++', n_clusters=5, n_init=10)

kmeans.fit(X)

cluster_label = kmeans.labels_  #군집분석의 예측값
print('클러스터 라벨:',cluster_label)

df ['Cluster']=cluster_label 


import matplotlib.pyplot as plt
df.plot(kind='scatter', x='Grocery', y='Frozen', c='Cluster', cmap='Set1', colorbar=False, figsize=(10, 10))
df.plot(kind='scatter', x='Milk', y='Delicassen', c='Cluster', cmap='Set1', colorbar=False, figsize=(10, 10))
plt.show()
plt.close()

