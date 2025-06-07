'''
Author: sunjie
Date: 2025-04-02 21:45:53
LastEditors: sunj
LastEditTime: 2025-04-02 22:17:16
FilePath: /sunjPy/tensorflow/t-imdb.py
'''
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from tensorflow import keras
import numpy as np
from tensorflow.keras.datasets import imdb
(train_data, train_labels), (test_data,
                             test_labels) = imdb.load_data(num_words=10000)
print(train_data[0], len(train_data))
print(train_labels[0])
max([max(sequence) for sequence in train_data])
word_index = imdb.get_word_index()
reverse_word_index = dict(
    [(value, key) for (key, value) in word_index.items()])
decoded_review = " ".join(
    [reverse_word_index.get(i - 3, "?") for i in train_data[0]])


def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results


x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

# 修改这部分：直接将标签转换为numpy数组
y_train = np.array(train_labels)
y_test = np.array(test_labels)

model = keras.Sequential([
    layers.Dense(16, activation="relu"),
    layers.Dense(16, activation="relu"),
    layers.Dense(1, activation="sigmoid")
])

# optimizer = keras.optimizers.RMSprop(learning_rate=0.001)
# model.compile(optimizer=optimizer,
#               loss="binary_crossentropy",
#               metrics=["accuracy"])


x_val = x_train[:10000]
partial_x_train = x_train[10000:]
y_val = y_train[:10000]
partial_y_train = y_train[10000:]
model.compile(optimizer="rmsprop",
              loss="binary_crossentropy",
              metrics=["accuracy"])

history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=20,
                    batch_size=512,
                    validation_data=(x_val, y_val))

history_dict = history.history
print(history_dict.keys())


history_dict = history.history
loss_values = history_dict["loss"]
val_loss_values = history_dict["val_loss"]
epochs = range(1, len(loss_values) + 1)
plt.plot(epochs, loss_values, "bo", label="Training loss")
plt.plot(epochs, val_loss_values, "b", label="Validation loss")
plt.title("Training and validation loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()
