# Quantum_Information
These are homeworks for quantum information in Technion.  
## QIHW2
### test_1
test_1 describes a random walk process.  
deltat means span of each step, which I set 0.05
totalstep means total steps, which I set 5000
alpha means probability amplitude for a going-up state, which I set 0.7.  
The range of alpha is [0,1].  
### test_2  
test_2 proves that if we do random walk many times, the probability will converge to the square of probility amplitude what we set  
The variables are the same as test_1, except one.  
N means number of times to run programs.  
The results will show up the value of alpha square, number of sipn up particles, and error of value.  

## QIHW5
In this exercise, we need to compress a picture of Richard Feynman using Singular Value Decomposition(SVD).  
However, since the link is broken. I will fix it another day.

## QIHW10
### figure
figure describes Discrete Fourier Transformation(DFT).  
We assume r divides N.  
Also we assume x_k = 1 if k=0 mod r, and x_k = 0 if others.  
The first graph is x v.s. k, and the second one is x v.s. j in the case of N=100 and r =20  
### Shor  
Shor finds x.  
x needs to be satisfy the remainder of x to the power of 7 divide by 11 equal to 9 in the range of 0 to 127.  
### DFT  
I calculate the state of DFT_128, and also plot a graph of j v.s. b_j^2.   
### omega   
I totally forgot the meaning of this function.
