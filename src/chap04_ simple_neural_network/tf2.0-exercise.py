#!/usr/bin/env python
# coding: utf-8

# # Tensorflow2.0 小练习

# In[2]:

import tensorflow as tf
import numpy as np

# ## 实现softmax函数

# In[6]:

def softmax(x):
    """
    实现softmax函数，对输入张量的最后一维进行归一化。
    不允许使用 TensorFlow 自带的 softmax 函数。
    """
    # 计算每个元素的指数值，减去最大值以提高数值稳定性
    exp_x = tf.exp(x - tf.reduce_max(x, axis=-1, keepdims=True))
    # 计算 softmax 值
    prob_x = exp_x / tf.reduce_sum(exp_x, axis=-1, keepdims=True)
    return prob_x

# 测试 softmax 实现是否正确，使用随机数据对比 TensorFlow 的实现
test_data = np.random.normal(size=[10, 5])
(softmax(test_data).numpy() - tf.nn.softmax(test_data, axis=-1).numpy())**2 <0.0001

# ## 实现sigmoid函数

# In[9]:

def sigmoid(x):
    ##########
    '''实现sigmoid函数， 不允许用tf自带的sigmoid函数'''
    ##########
    return prob_x

# 测试 sigmoid 实现是否正确
test_data = np.random.normal(size=[10, 5])
(sigmoid(test_data).numpy() - tf.nn.sigmoid(test_data).numpy())**2 < 0.0001

# ## 实现 softmax 交叉熵loss函数

# In[32]:

def softmax_ce(x, label):
    ##########
    '''实现 softmax 交叉熵loss函数， 不允许用tf自带的softmax_cross_entropy函数'''
    ##########
    # 使用 clip 避免 log(0) 产生数值不稳定
    x = tf.clip_by_value(x, 1e-10, 1.0)
    # 计算交叉熵损失：-sum(y_true * log(y_pred))
    loss = -tf.reduce_mean(tf.reduce_sum(label * tf.math.log(x), axis=-1))
    ##########
    return loss

# 构造测试数据并验证 softmax_ce 函数正确性
test_data = np.random.normal(size=[10, 5])
prob = tf.nn.softmax(test_data)  # 得到 softmax 概率
label = np.zeros_like(test_data)   # 创建 one-hot 标签
label[np.arange(10), np.random.randint(0, 5, size=10)]=1.0  # 每行随机一个位置设为 1

# 对比手动实现和 TensorFlow 实现的 softmax 交叉熵结果
((tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(label, test_data))
  - softmax_ce(prob, label))**2 < 0.0001).numpy()

# ## 实现 sigmoid 交叉熵loss函数

# In[46]:

def sigmoid_ce(x, label):
    ##########
    '''实现 softmax 交叉熵loss函数， 不允许用tf自带的softmax_cross_entropy函数'''
    ##########
    # clip 避免 log(0) 的数值不稳定问题
    x = tf.clip_by_value(x, 1e-10, 1.0 - 1e-10)
    # 计算二分类交叉熵损失
    loss = -tf.reduce_mean(label * tf.math.log(x) + (1 - label) * tf.math.log(1 - x))
    ##########
    return loss

# 构造测试数据并验证 sigmoid_ce 函数正确性
test_data = np.random.normal(size=[10])
prob = tf.nn.sigmoid(test_data)  # 得到 sigmoid 概率
label = np.random.randint(0, 2, 10).astype(test_data.dtype)   # 随机生成 0 或 1 的标签
print (label)

# 对比手动实现和 TensorFlow 实现的 sigmoid 交叉熵结果
((tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(label, test_data))- sigmoid_ce(prob, label))**2 < 0.0001).numpy()

# In[ ]:
# In[ ]:




