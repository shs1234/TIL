import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('./dataset/iris.csv', names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])
print(df.head())

sns.pairplot(df, hue='species')  #속성별 연관성 파악
plt.show()

dataset = df.values
X = dataset[:,0:4].astype(float)
Y_obj = dataset[:,4]

from sklearn.preprocessing import LabelEncoder     
e = LabelEncoder()     # array(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])가 array([1,2,3])로 변환
e.fit(Y_obj)
Y = e.transform(Y_obj)

from keras.utils import np_utils
# array([1,2,3])가 다시 array([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])로 원-핫 인코딩(one-hot-encoding) 변환
Y_encoded = np_utils.to_categorical(Y)

from keras.models import Sequential
from keras.layers.core import Dense
import numpy
import tensorflow as tf

seed = 0
numpy.random.seed(seed) # seed 값 설정
tf.set_random_seed(seed)

model = Sequential() # 모델의 설정
model.add(Dense(16, input_dim=4, activation='relu'))
#최종 출력 값이 3개 중 하나여야 하므로 출력층에 해당하는 Dense의 노드 수를 3으로 설정
model.add(Dense(3, activation='softmax'))

# 모델 컴파일(다중 분류에 적절한 오차 함수인 categorical_crossentropy를 사용, 최적화 함수로 adam 사용)
model.compile(loss='categorical_crossentropy',    optimizer='adam',    metrics=['accuracy'])

# 모델 실행(한 번에 입력되는 값은 1개, 전체 샘플이 50회 반복될 때까지 실험을 진행
model.fit(X, Y_encoded, epochs=50, batch_size=1)   

print("\n Accuracy: %.4f" % (model.evaluate(X, Y_encoded)[1]))   # 결과 출력
