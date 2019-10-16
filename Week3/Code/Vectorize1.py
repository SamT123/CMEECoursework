import numpy as np
import time

M = np.random.random([1000,1000])

def sum_all_elements(M):
    dims  = M.shape
    t=0
    for i in range(dims[0]):
        for j in range(dims[1]):
            t += M[i,j]
    return t



start = time.time()
sum_all_elements(M)
end = time.time()

sum_elems_time = end-start

start = time.time()
np.sum(M)
end = time.time()

sum_np_time = end-start

print("per element time is %f" %sum_elems_time)
print("np sum time is %f" %sum_np_time)