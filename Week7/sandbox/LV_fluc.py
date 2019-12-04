import sys
import numpy as np


R0, C0, K, r, a, z, e,  gens = map(float,sys.argv[1:])
gens = int(gens)

densities = np.zeros([gens,2])
densities[0] =  np.array([R0,C0])
fluctuations = np.random.randn(gens-1,2)/10

for gen in range(1,gens):
    R = densities[gen-1][0]
    C = densities[gen-1][1]
    densities[gen][0] = R * (1 + (r + fluctuations[gen-1,0]) * (1 - R / K) - a * C)
    densities[gen][1] = C * (1 - z + e * a * R + fluctuations[gen-1,1])


import matplotlib.pylab as p
f1 = p.figure()
p.plot(range(gens), densities[:,0])
p.plot(range(gens), densities[:,1])
p.show()

if __name__ == '__main__':
    status = main(list(map(float, sys.argv[1:])))
    sys.exit(status)