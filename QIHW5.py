# -*- coding: utf-8 -*-
"""
Read and show Feynman image in Python.
"""

import urllib.request                      # url manipulation
import numpy as np                         # numpy
from pylab import imread,subplot,imshow    # image manipulation
import matplotlib.pyplot as plt            # plot manipulation
from functools import reduce

# create a file-like object from Moodle url
# and read it into a numpy array
imfile  = urllib.request.urlopen("https://upload.wikimedia.org/wikipedia/it/thumb/0/0b/Richard-feynman.jpg/900px-Richard-feynman.jpg")
Feynman = imread(imfile, format='jpg')

#print(Feynman)
# make it a black and white 2D float
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

#A = rgb2gray(Feynman*1.0)

A = Feynman

def test_1():
    u, s, v = np.linalg.svd(A) #find the SVD of A
    plt.title("the sigular values of A")
    plt.xlabel("sigular values")
    plt.ylabel("values")
    plt.loglog(s)
    plt.show()

#test_1()

def test_2():
    N,M = A.shape #find the size of A
    B = np.random.random_integers(0,255,(N,M)) #create a random integer matrix with size of A
    u,s,v = np.linalg.svd(B) #find SVD of B
    plt.title("the sigular values of B")
    plt.xlabel("sigular values")
    plt.ylabel("values")
    plt.loglog(s)
    plt.show()

#test_2()

def SVDcompress(A,n): #input is the matrix A and an integer n
    u,s,v = np.linalg.svd(A) #find SVD of A
    # I slice the unitaries and singular values
    d = s[:n]
    Ut = u[:,:n]
    Vt = v[:n,:] # v is already done the conjugate transpose
    return Ut, Vt, d #ouput is two unitaries and singular values

def test_3():
    plt.figure(num=1)
    plt.imshow(A, cmap='gray')
    plt.show()
    n = [10,20,50,100,150]
    for ndx in n:
        Ut ,Vt, d = SVDcompress(A,ndx)
        Ut = np.matrix(Ut)
        Dt = np.diag(d) # become the diagonal matrix
        Vt = np.matrix(Vt)
        At = reduce(np.matmul,[Ut,Dt,Vt]) #=(Ut*Dt)*Vt
        plt.figure(num=1)
        plt.imshow(At, cmap='gray')
        plt.show()
#test_3()

def norm(A):
    return np.sqrt(np.sum(np.square(A)))

def error(A,At):
    return norm(A-At)/norm(A)

def test_4():
    n = [10, 20, 50, 100, 150, 750]
    for ndx in n:
        u, s, v = np.linalg.svd(A)
        z = np.zeros((900,900))
        u = np.matrix(u)
        st = np.diag(s)
        z[:900,:900] = st
        v = np.matrix(v)
        A0 = reduce(np.matmul, [u, z, v])
        Ut, Vt, d = SVDcompress(A, ndx)
        Ut = np.matrix(Ut)
        Dt = np.diag(d)
        Vt = np.matrix(Vt)
        At = reduce(np.matmul, [Ut, Dt, Vt])
        x = error(A0,At)
        print(x)
        y = np.sqrt(np.sum(np.square(s[ndx:])))
        print(y)
        break

test_4()

def test(A):
    # plot the grayscale image
    plt.figure(num=1)
    plt.imshow(A, cmap='gray')
    plt.show()
