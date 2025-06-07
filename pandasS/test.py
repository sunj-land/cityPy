'''
Author: sunjie
Date: 2025-03-24 22:40:51
LastEditors: sunj
LastEditTime: 2025-06-07 16:39:08
FilePath: /sunjPy/pandasS/test.py
'''
# 导入必要的库
from tensorflow.keras import layers
from tensorflow import keras
from tensorflow.keras.datasets import mnist
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 设置随机种子
tf.random.set_seed(42)     # TensorFlow随机种子
np.random.seed(42)         # NumPy随机种子

# 加载MNIST数据集,分为训练集和测试集
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print(train_images.shape)  # 打印训练图像的形状
print(len(train_labels))   # 打印训练标签的数量

# 构建神经网络模型
model = keras.Sequential([
    layers.Dense(512, activation='relu'),      # 第一层:512个神经元,使用ReLU激活函数
    # 输出层:10个神经元(对应0-9),使用softmax激活函数
    layers.Dense(10, activation='softmax')
])

# 编译模型
model.compile(
    optimizer="rmsprop",                       # 使用RMSprop优化器
    loss="sparse_categorical_crossentropy",    # 使用稀疏分类交叉熵损失函数
    metrics=["accuracy"]                       # 使用准确率作为评估指标
)

# 数据预处理
train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype("float32") / 255.0  # 添加归一化
test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype("float32") / 255.0    # 添加归一化

digit = train_images[4]
print(digit, train_labels[4])
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()


# # 训练模型
# model.fit(train_images, train_labels, epochs=1,
#           batch_size=128)  # 训练5轮,每批128个样本

# # 测试模型
# test_digits = test_images[0:10]                # 取前10个测试图像
# predictions = model.predict(test_digits)        # 进行预测
# print(predictions[0])                          # 打印第一个预测结果(概率分布)
# print(predictions[0].argmax())                 # 打印预测的数字(最大概率的索引)
# print(predictions[0][7])                       # 打印数字7的预测概率
# print(test_labels[0])                         # 打印第一个测试图像的真实标签

# # 评估模型
# test_loss, test_acc = model.evaluate(test_images, test_labels)  # 在测试集上评估模型
# print(f"test_acc: {test_acc}")                # 打印测试准确率
