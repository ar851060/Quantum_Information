# Quantum_Information
These are homeworks for quantum information in Technion.  
QIHW is my answers and codes of the homeworks.  
pset is the questions of homeworks.  
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
Since the original link of the picture is failed, I change the link to the pi cture from wikipedia.   
In order words, the code still work although the pictures between documents and code are different.  
### test_1
Find SVD of the picture and show the singular values.  
### test_2
Create a random matrix, find SVD of it, and show its singular values.
### SVDcompress
This function compress the pictures by slice parts of unitaries and singular values.
### test_3
With SVDcompress, I print out 6 pictures with different kinds of compression.  
### test_4
I forget why I do this function, but it seems to find the error between original picture and compressed picture.  

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
