# Reference website: https://www.tensorflow.org/tutorials/mandelbrot#mandelbrot-set
# import the libraries for simulation

import tensorflow as tf
import numpy as np

# imports for visualization
"""
import PIL 
this PIL module means Python Imaging Library and it has been replaced by Pillow module
PIL is only supported by Python V2.7; Pillow module will be supported by Python V3.5 
"""

import PIL.Image
from io import BytesIO
from IPython.display import Image, display

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def display_fractal(a, fmt='jpeg'):
    """Display an array of iteration counts as a
       colorful picture of a fractal.
    """
    a_cyclic = (6.28 * a / 20.0).reshape(list(a.shape) + [1])
    img = np.concatenate([10 + 20 * np.cos(a_cyclic),
                          30 + 50 * np.sin(a_cyclic),
                          155 - 80 * np.cos(a_cyclic)], 2)
    img[a == a.max()] = 0
    a = img
    a = np.uint8(np.clip(a, 0, 255))
    f = BytesIO()
    PIL.Image.fromarray(a).save(f, fmt)
    display(Image(data=f.getvalue()))


# interactive session


sess = tf.InteractiveSession()

# Use Numpy to create a 2D arrays of complex numbers

Y, X = np.mgrid[-1.3:1.3:0.005, -2:1:0.005]
Z = X+1j*Y

# Define and initialize TensorFlow tensors

xs = tf.constant(Z.astype(np.complex64))
zs = tf.Variable(xs)
ns = tf.Variable(tf.zeros_like(xs, tf.float32))

# Initialize variables before using them

tf.global_variables_initializer().run()

# Specify more of the computation

# Compute the new values of z: z^2 + x

zs_ = zs*zs + xs

# Have we diverged with this new value?

not_diverged = tf.abs(zs_) < 4

"""
Operation to update the zs and the iteration count.
Note: We keep computing zs after they diverge!
      This is very wasteful! There are better, if a little less simple, ways to do this.
"""

step = tf.group(
    zs.assign(zs_),
    ns.assign_add(tf.cast(not_diverged, tf.float32))
)

# run it for a couple hundred steps

for i in range(200):
    step.run()

display_fractal(ns.eval())


