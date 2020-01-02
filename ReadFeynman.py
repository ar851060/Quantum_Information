# -*- coding: utf-8 -*-
"""
Read and show Feynman image in Python.
"""

import urllib.request                            # url manipulation
import numpy as np                         # numpy
from pylab import imread,subplot,imshow    # image manipulation
import matplotlib.pyplot as plt            # plot manipulation


# create a file-like object from Moodle url
# and read it into a numpy array
imfile  = urllib.request.urlopen("https://moodle.technion.ac.il/pluginfile.php"
                          "/1016715/mod_resource/content/1/Richard-Feynman.jpg")
Feynman = imread(imfile, format='jpg')


# make it a black and white 2D float
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

A = rgb2gray(Feynman*1.0)


# plot the grayscale image
plt.figure(num=1)
plt.imshow(A, cmap='gray')
plt.show()
