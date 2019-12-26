# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 13:56:29 2019

@author: student
"""

import pandas as pd
import numpy as np
from sklearn import tree

uci_path='http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data'
df = pd.read_csv(uci_path, header=None)

df.columns=['id', 'clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial', 'bare_nuclei', 'chromation', 'normal_nucleoli', 'mitoses', 'class']

df['bare_nuclei'].replace('?',np.nan,inplace=True)
df.dropna(subset=['bare_nuclei'],inplace=True)

df['bare_nuclei']=df['bare_nuclei'].astype(int)

X=df[['id', 'clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial', 'bare_nuclei', 'chromation', 'normal_nucleoli', 'mitoses']]
Y=df['class']

from sklearn import preprocessing 
X = preprocessing.StandardScaler().fit(X).transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=10)

tree_model=tree.DecisionTreeClassifier(criterion='entropy',max_depth=5)
#tree_model = tree.DecisionTreeClassifier(criterion='gini',  max_depth=5)

tree_model.fit(X_train,Y_train)

y_predict=tree_model.predict(X_test)

from sklearn import metrics
tree_metrics=metrics.confusion_matrix(Y_test,y_predict)
print(tree_metrics)

tree_report=metrics.classification_report(Y_test,y_predict)
print(tree_report)