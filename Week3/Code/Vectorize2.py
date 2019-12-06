"""
Runs the stochastic (with gaussian fluctuations) Ricker Equation. 
Compares speed of vectorised and non-vectorised methods.
"""

# imports
import numpy as np
import time
import math

def stochrick(p0 = (np.random.random(1000) + 0.5), r = 1.2, K = 1, sigma = 0.2, numyears = 100):
    """calculate population density matrix using stochastic Ricker equation, elementwise.

    PARAMETERS
    ----------
    p0 : np.array (default np.random.random(1000) + 0.5)
        array of t0 population densities
    
    r : float, int (default 1.2)
        intrinsic popoulation growth rate

    K : float, int (default 1)
        Population carrying capacity

    sigma : float, int (default 0.2)
        standard deviation of population density noise added each timestep

    numyears : int (default 100)
        number of timesteps to run simulation for

    RETURNS
    -------
    N : np.array
        array of population densities. N[i,j] = density for population i in year j
    """

    N = np.full([numyears,len(p0)],np.nan)
    N[0,] = p0
    for i in range(len(p0)):
        for j in range(numyears):
            N[j,i]=N[j-1,i] * math.exp(r*(1-N[j-1,i]/K)+np.random.randn(1)*sigma)
    return N


def stochrickvect(p0 = (np.random.random(1000) + 0.5), r = 1.2, K = 1, sigma = 0.2, numyears = 100):
    """calculate population density matrix using stochastic Ricker equation, using numpy vectorization.

    PARAMETERS
    ----------
    p0 : np.array (default np.random.random(1000) + 0.5)
        array of t0 population densities
    
    r : float, int (default 1.2)
        intrinsic popoulation growth rate

    K : float, int (default 1)
        Population carrying capacity

    sigma : float, int (default 0.2)
        standard deviation of population density noise added each timestep

    numyears : int (default 100)
        number of timesteps to run simulation for

    RETURNS
    -------
    N : np.array
        array of population densities. N[i,j] = density for population i in year j
    """

    N = np.full([numyears,len(p0)],np.nan)
    N[0,] = p0
    for j in range(numyears):
        N[j,] = N[j-1,] * math.e**(r*(1-N[j-1,]/K)+np.random.randn(len(p0))*sigma)
    return N
    

print(" Python\n--------")


start = time.time()
stochrick()
end = time.time()
print("Unvectorized:\t" + "{0:.3f}".format(end-start))


start = time.time()
stochrickvect()
end = time.time()
print("Vect (NumPy):\t" + "{0:.3f}".format(end-start))
