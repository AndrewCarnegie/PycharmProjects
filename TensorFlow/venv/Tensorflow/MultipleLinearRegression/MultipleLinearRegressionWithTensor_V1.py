#! /usr/bin/env python
#-*- coding:utf-8 -*-
# version : Python 2.7.5

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

rng = np.random.RandomState(1)
N = 10

X = np.array(N * [10 * rng.rand(2)])
b = [2, 3]
Y = 1 + np.matmul(X,b)  + rng.randn(N)

print(X)
print(Y)

model = LinearRegression()
model.fit(X, Y)

x_fit = np.array(10 * [10 * rng.rand(2)])
y_fit = model.predict(xfit)

print("x_fit :")
print(x_fitfit)
print("y_fit :")
print(y_fit)