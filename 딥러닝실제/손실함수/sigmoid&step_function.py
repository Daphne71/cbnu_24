# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:15:09 2024

@author: user
"""
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int32)
"""
x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x,y)
plt.ylim(-0.1, 1.1)
plt.show()
"""

def sigmoid(x):
    return 1 / (1+np.exp(-x))
"""
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x,y)
plt.ylim(-0.1, 1.1)
plt.show()
"""
def relu(x):
    return np.maximum(0, x)

x = np.arange(-6,7)
y = relu(x)
plt.plot(x,y)
plt.ylim(-1, 6)
plt.show()