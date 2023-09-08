# -*- coding: utf-8 -*-
"""MNIST_CNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kHsu7S3RiIueh6yzBlSO6MdU75nxJBMJ

**Importing Libraries**
"""

import tensorflow.keras as tk

"""**Loading dataset**"""

mnist = tk.datasets.mnist

"""**Splitting Dataset**"""

(X_train,y_train),(X_test,y_test)=mnist.load_data()

X_train[0]

y_train[0]

X_train = X_train / 255
X_test = X_test / 255

"""**Reshaping data**"""

X_train = X_train.reshape(-1,28,28,1)    #training set
X_test = X_test.reshape(-1,28,28,1)      #test set

from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers import Dense
from keras.layers.convolutional import MaxPooling2D
from keras.layers import Flatten
model = Sequential()
model.add(Conv2D(25,(3,3),activation="relu",input_shape=(28,28,1)))
model.add(MaxPooling2D(2,2))
model.add(Conv2D(64,(3,3),activation="relu"))
model.add(MaxPooling2D(2,2))
model.add(Conv2D(64,(3,3),activation="relu"))
model.add(MaxPooling2D(2,2))
model.add(Flatten())
model.add(Dense(64,activation="relu"))
model.add(Dense(10,activation="softmax"))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train,y_train,epochs=10)
'''
convolutional_neural_network.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
convolutional_neural_network.fit(X_train, y_train, epochs=10)
'''

model.evaluate(X_test, y_test)

y_pred = model.predict(X_test)
y_pred[0]

import numpy as np
np.argmax(y_pred[0])

y_predicted_labels = [np.argmax(i) for i in y_pred]

y_predicted_labels[:5]