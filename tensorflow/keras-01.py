'''
Author: sunjie
Date: 2025-04-06 21:31:42
LastEditors: sunj
LastEditTime: 2025-04-06 21:31:45
FilePath: /sunjPy/tensorflow/keras-01.py
'''
from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Dense(64, activation="relu"),
    layers.Dense(10, activation="softmax"),
])

model.weights

model.build(input_shape=(None, 3))
