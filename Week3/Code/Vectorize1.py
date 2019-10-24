"""Comparison of element-wise matrix sum to built in vectorized sum function"""


import numpy as np
import time

M = np.random.random([1000,1000])

def sum_all_elements(M):
    """
    Calculate matrix sum by elementwise addition
    PARAMETERS
    ----------
    M : np.array
        array to sum
    
    RETURNS
    -------
    int
        sum of elements of matrix
    """
    dims  = M.shape
    t=0
    for i in range(dims[0]):
        for j in range(dims[1]):
            t += M[i,j]
    return t


# time elementwise function
start = time.time()
sum_all_elements(M)
end = time.time()

sum_elems_time = end-start

# time builtin funtion

start = time.time()
np.sum(M)
end = time.time()

sum_np_time = end-start


# print results

print(" Python\n--------")

print("Unvectorized:\t" + "{0:.3f}".format(sum_elems_time))

print("Vect (NumPy):\t" + "{0:.3f}".format(sum_np_time))