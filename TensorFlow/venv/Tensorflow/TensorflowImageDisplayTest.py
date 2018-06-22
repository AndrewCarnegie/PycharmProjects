import tensorflow as tf
import numpy as np

# imports for visualization
"""
import PIL 
this PIL module means Python Imaging Library and it has been replaced by Pillow module
PIL is only supported by Python V2.7; Pillow module will be supported by Python V3.5 
"""

import PIL.Image
from io import StringIO
from IPython.display import Image, display

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def show_array(a, fmt='jpeg'):
    a = np.uint8(np.clip(a, 0, 255))
    f = StringIO()
    PIL.Image.fromarray(a).save(f, fmt)
    display(Image(data=f.getvalue()))

