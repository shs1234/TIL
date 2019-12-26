# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 12:47:48 2019

@author: student
"""


import seaborn as sns

df = sns.load_dataset('titanic')

df.dropna(axis=0,inplace=True)
#df.dropna(subset=['embarked'],axis=0,inplace=True)

X = df[['pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
Y = df['survived']


from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()

sex_encoder=encoder.fit_transform(X['sex'])
embarked_encoder=encoder.fit_transform(X['embarked'])

X.iloc[:,1]=sex_encoder
X.iloc[:,-1]=embarked_encoder


from sklearn import preprocessing 
X = preprocessing.StandardScaler().fit(X).transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=10)

from sklearn import tree

#tree_model = tree.DecisionTreeClassifier(criterion='entropy',  max_depth=6)
tree_model = tree.DecisionTreeClassifier(criterion='gini',  max_depth=5)

tree_model.fit(X_train, Y_train)

y_predict = tree_model.predict(X_test) 

from sklearn import metrics
tree_matrix = metrics.confusion_matrix(Y_test, y_predict)
print(tree_matrix)

tree_report = metrics.classification_report(Y_test, y_predict)
print(tree_report)