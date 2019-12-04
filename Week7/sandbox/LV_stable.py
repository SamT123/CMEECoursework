import scipy as sc
import scipy.integrate as integrate
import sys

r = 1.
a = 0.1 
z = 0.7
e = 0.75
K = 20

def dCR_dt(pops, t=0):

    R = pops[0]
    C = pops[1]
    dRdt = r * R * (1 - R / K) - a * R * C 
    dCdt = -z * C + e * a * R * C
    
    return sc.array([dRdt, dCdt])



t = sc.linspace(0, 15, 1000)

R0 = 10
C0 = 5 
RC0 = sc.array([R0, C0])

pops, infodict = integrate.odeint(dCR_dt, RC0, t, full_output=True)

print("Final resource density = \t{}\nFinal consumer density = \t{}".format(pops[-1][0],pops[-1][1]))
# plotting

import matplotlib.pylab as p
f1 = p.figure()
p.plot(t, pops[:,0], 'g-', label='Resource density') # Plot
p.plot(t, pops[:,1]  , 'b-', label='Consumer density')
p.grid()
p.legend(loc='best')
p.text(s = "r = {}\na = {}\nz = {}\ne = {}".format(r,a,z,e),  x = -0.5, y = 35,  bbox=dict(facecolor='white', edgecolor='black'))

p.xlabel('Time')
p.ylabel('Population density')
p.title('Consumer-Resource population dynamics')

f1.savefig('../Results/LV3_model_vs_t.pdf') #Save figure 


f2 = p.figure()

p.plot(pops[:,0], pops[:,1]  , 'r-')
p.grid()


p.text(s = "r = {}\na = {}\nz = {}\ne = {}".format(r,a,z,e), x = 35, y = 20,  bbox=dict(facecolor='white', edgecolor='black'))


p.xlabel('Resource density')
p.ylabel('Consumer density')
p.title('Consumer-Resource population dynamics')

f2.savefig('../Results/LV3_model_C_vs_R.pdf') #Save figure 
