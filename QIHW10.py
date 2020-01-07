import matplotlib.pyplot as plt
import numpy as np
import math
import pdb
import random
import cmath

def figure():
    xk = []
    k = []
    jk = []
    N = 100
    r = 20
    for idx in range(0, 99):
        if idx % r == 0:
            xk.append(1)
        else:
            xk.append(0)
        k.append(idx)
    plt.plot(k, xk)
    plt.xlabel("k")
    plt.ylabel("x")
    plt.show()

    for jdx in range(0, 99):
        tempj = 0
        for idx in range(0,99):
            if idx%r==0:
                tempj += cmath.exp(2j*math.pi*idx*jdx/N)
            else:continue
        jk.append(pow(abs(tempj),2)/math.sqrt(N))
    plt.plot(k,jk)
    plt.xlabel("j")
    plt.ylabel("|x|")
    plt.show()
    print(jk)

#figure()

def Shor():
    i = 0
    for idx in range(0,127):
        num = pow(7,idx)
        if num%11==9:
            i+=1
            print(idx)
    print(i)

#Shor()

def DFT():
    blist = []
    b = []
    pj = []
    s = 3
    r = 11
    L = 128
    m = 12
    for jdx in range(0, 127):
        ansj = cmath.exp(2j * s * math.pi * jdx / L)
        ansk = 0
        for kdx in range(3, 125, 11):
            ansk += cmath.exp(2j * math.pi * r * kdx * jdx / L)
            ans = ansk * ansj / math.sqrt(L * m)
        blist.append(pow(abs(ans), 2))
        if pow(abs(ans), 2) > 0.06:
            print(jdx)
            print(pow(abs(ans), 2))
        b.append(jdx)
    plt.plot(b, blist)
    plt.xlabel("j")
    plt.ylabel("|bj|^2")
    plt.show()

#DFT()

def omega():
    a = 0.309017+0.951057j
    b = cmath.exp(-2j*math.pi/16)
    for i in range(0,16):
        ans = 0
        for j in range(0,16):
            ans += b**(i*j)*a**(j)
        print(abs(ans))
omega()
