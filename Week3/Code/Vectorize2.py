
import numpy as np
import time
import math
def stochrick(p0 = (np.random.random(1000) + 0.5), r = 1.2, K = 1, sigma = 0.2, numyears = 100):

    N = np.full([numyears,len(p0)],np.nan)
    N[0,] = p0
    for i in range(len(p0)):
        for j in range(numyears):
            N[j,i]=N[j-1,i] * math.exp(r*(1-N[j-1,i]/K)+np.random.randn(1)*sigma)
    return N

start = time.time()
stochrick()
end = time.time()
print("Unvectorized time is " + str(end-start))

def stochrickvect(p0 = (np.random.random(1000) + 0.5), r = 1.2, K = 1, sigma = 0.2, numyears = 100):

    N = np.full([numyears,len(p0)],np.nan)
    N[0,] = p0
    for j in range(numyears):
        N[j,] = N[j-1,] * math.e**(r*(1-N[j-1,]/K)+np.random.randn(len(p0))*sigma)
    return N

start = time.time()
stochrickvect()
end = time.time()
print("Vectorized time is " + str(end-start))