# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 11:13:50 2019

@author: student
"""

import numpy as np
from sklearn.preprocessing import LabelEncoder

X_train = np.array(['MOBILE', 'NOTEBOOK', 'DESKTOP'])
X_test = np.array(['MOBILE', 'NOTEBOOK', 'TABLET'])
np.array

encoder=LabelEncoder()

encoder.fit(X_train)

x_train_encoder=encoder.transform(X_train)

print(x_train_encoder)
print(encoder.classes_)

for label in np.unique(X_test):
    if label not in encoder.classes_:
        encoder.classes_ = np.append(encoder.classes_, label)
        
x_test_encoded  = encoder.transform(X_test)
print(x_test_encoded)
print(encoder.classes_)
print('\n')

result = encoder.inverse_transform([2, 1, 0, 3])
print(result)
print('\n')

