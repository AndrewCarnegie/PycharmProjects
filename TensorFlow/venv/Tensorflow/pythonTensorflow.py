import tensorflow as tf
import numpy as np
# import iris_data
# -- Metadata describing the text columns
#
# W = tf.Variable([.3], tf.float32)
# b = tf.Variable([-.3], tf.float32)
# x = tf.placeholder(tf.float32)
# linear_model = W * x + b
#
# init = tf.global_variables_initializer()
# sess = tf.Session()
# sess.run(init)
#
# print(sess.run(linear_model, {x: [1, 2, 3, 4]}))
# squares = []
#
# for x in range(10):
#     squares.append(x**2)
#
# print(squares)
#
#
# squares1 = list(map(lambda y: y**2, range(10)))
# print(squares1)
#
#
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
#
# print(pairs)

g = tf.Graph()

with g.as_default():
    x = tf.constant(8, name="x_constant")
    y = tf.constant(5, name="y_constant")
    sum1 = tf.add(x, y, name="x_y_sum")
    z = tf.constant(4, name="z_const")
    new_sum = tf.add(sum1, z, name="x_y_z_sum")
    with tf.Session() as sess:
        print(new_sum.eval())


import re


p = re.compile('[A-Za-z0-9_]+@hotmail.com')
print(p)
# sess = tf.Session()
# with sess.as_default():
#     assert sess is tf.get_default_session()
#     assert z.eval() == sess.run(z)


# Model parameters
# W = tf.Variable([.3], tf.float32)
# b = tf.Variable([-.3], tf.float32)
# # Model input and output
# x = tf.placeholder(tf.float32)
# linear_model = W * x + b
# y = tf.placeholder(tf.float32)
# # loss
# loss = tf.reduce_sum(tf.square(linear_model - y))  # sum of the squares
# # optimizer
# optimizer = tf.train.GradientDescentOptimizer(0.01)
# train = optimizer.minimize(loss)
# # training data
# x_train = [1, 2, 3, 4]
# y_train = [0, -1, -2, -3]
# # training loop
# init = tf.global_variables_initializer()
# sess = tf.Session()
# sess.run(init)  # reset values to wrong
# for i in range(1000):
#     sess.run(train, {x: x_train, y: y_train})
#
# # evaluate training accuracy
# curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
# print("W: %s b: %s loss: %s" % (curr_W, curr_b, curr_loss))


# COLUMNS = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'label']
#
# FIELD_DEFAULTS = [[0.0], [0.0], [0.0], [0.0], [0]]
#
# # 创建一个或多个输入函数。
#
#
# def input_evaluation_set():
#     features = {'SepalLength': np.array([6.4, 5.0]),
#                 'SepalWidth':  np.array([2.8, 2.3]),
#                 'PetalLength': np.array([5.6, 3.3]),
#                 'PetalWidth':  np.array([2.2, 1.0])}
#     labels = np.array([2, 1])
#     return features, labels
#
#
# def train_input_fn(features, labels, batch_size):
#     """An input function for training"""
#     # Convert the inputs to a Dataset.
#     dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
#
#     # Shuffle, repeat, and batch the examples.
#     return dataset.shuffle(1000).repeat().batch(batch_size)
#
#
# # 定义模型的特征列。
#
#
# # Feature columns describe how to use the input.
# my_feature_columns = []
# for key in train_x.keys():
#     my_feature_columns.append(tf.feature_column.numeric_column(key=key))


# 实例化 Estimator，指定特征列和各种超参数。
# 在 Estimator 对象上调用一个或多个方法，传递适当的输入函数作为数据的来源

# # -- create standard data dictionary
#
#
# # -- create the basic data store structure
#
#
# def _characteristic_data():
#
#     features = dict(COLUMNS, FIELD_DEFAULTS)
#     label = features.pop('label')
#
#     return features, label
#
#
# print(_characteristic_data())
#
#
# def train_input_fn(features, labels, batch_size):
#     """An input function for training"""
#     # Convert the inputs to a Dataset
#     dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))
#
#     # Shuffle, repeat, and batch the examples.
#     dataset = dataset.shuffle(1000).repeat().batch(batch_size)
#
#     # Build the Iterator, and return the read end of the pipeline.
#     return dataset.make_one_shot_iterator().get_next()
#
#
# # create one data set to store the standardized reference data
#
# # create one dynamic data set to store the input data
#
# # --data
#
# # --algorithm
# # --algorithm
#

