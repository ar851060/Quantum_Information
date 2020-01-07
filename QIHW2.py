import matplotlib.pyplot as plt
import numpy as np
import math
import pdb
import random

def test_1():
    deltat = 0.05
    totalstep = 5000
    for jdx in range(5):
        result = []
        num = []
        alpha = 0.7
        for idx in range(totalstep):
            alsq = pow(alpha, 2)
            result.append(alsq)
            num.append(idx)
            R = random.random()
            prob = 0.5 * math.sqrt(1.0 + deltat * (2 * pow(alpha, 2) - 1))
            if prob >R:
                alpha = (math.sqrt(1.0+deltat)*alpha)/(math.sqrt(1.0+deltat*(2.0*pow(alpha,2)-1.0)))
                continue
            else:
                alpha = (math.sqrt(1.0 - deltat) * alpha) / (math.sqrt(1.0 - deltat * (2.0*pow(alpha,2)-1.0)))
                continue
        plt.plot(num,result,linewidth=1)
    plt.ylabel("alpha^2")
    plt.xlabel("step")
    plt.show()

test_1()

def test_2():
    deltat = 0.05
    N = 10000
    totalstep = 5000
    result = []
    for jdx in range(N):
        alpha = 0.6
        for idx in range(totalstep):
            R = random.random()
            prob = 0.5*math.sqrt(1.0 + deltat * (2*pow(alpha, 2) - 1))
            if prob > R:
                alpha = (math.sqrt(1.0 + deltat) * alpha) / (math.sqrt(1.0 + deltat * (2*pow(alpha, 2) - 1)))
                continue
            else:
                alpha = (math.sqrt(1.0 - deltat) * alpha) / (math.sqrt(1.0 - deltat * (2*pow(alpha, 2) - 1)))
                continue
        result.append(alpha)
    up = 0
    down = 0
    for kdx in result:
        if pow(kdx,2)>0.5:
            up +=1
        else:
            down+=1
    print("the value of alpha square: ",pow(0.6,2))
    print("number of spin up: ",up)
    print("error of expected value and real value: ",abs(pow(0.6,2)-up*0.0001)/pow(0.6,2))
#test_2()



