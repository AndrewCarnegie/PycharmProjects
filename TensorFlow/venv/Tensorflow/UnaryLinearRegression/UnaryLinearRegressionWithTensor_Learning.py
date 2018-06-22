import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# import sys
# sys.path.append("C:\\Users\\fenye\PycharmProjects\\TensorFlow\\venv\\Tensorflow\\UnaryLinearRegression\\UnaryLinearRegressionWithTensor_V1.py")
# import UnaryLinearRegressionWithTensor_V1



# Write one or multiple data set input method as generic type input
# Figure out what's the input pipeline and its mechanism, how to build customized input pipeline
# How to define the data structure for input

def input_data_set():
    max_value_of_data_set = tf.placeholder(tf.int64, shape=[])
    data_set = tf.data.Dataset.range(max_value_of_data_set)
    iterator = data_set.make_initializable_iterator()
    next_element = iterator.get_next()
    with tf.Session() as sess:
        sess.run(iterator.initializer, feed_dict={max_value_of_data_set:10})
        for i in range(10):
            value = sess.run(next_element)
            assert i == value


# Define the feature column
feature_column_x = tf.feature_column.numeric_column('feature_column_x')
feature_column_y = tf.feature_column.numeric_column('feature_column_y')
loss = tf.feature_column.numeric_column('loss')


# Instantiate an estimator, passing the feature column

estimator = tf.estimator.LinearClassifier(feature_columns=[feature_column_x, feature_column_y, loss])


# Invoke train, estimator method

estimator.train(input_fn=input_data_set(), steps= 1000)

