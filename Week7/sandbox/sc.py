"""scipy notes from lectures"""

__appname__ = 'sc.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

# imports
import scipy as sc
a = sc.array(range(5)) # a one-dimensional array
a

print(type(a))
print(type(a[0]))

a = sc.array(range(5), float)
a
a.dtype


x = sc.arange(5)
x

x = sc.arange(5.) #directly specify float using decimal
x

b = sc.array([i for i in range(10) if i % 2 == 1]) #odd numbers between 1 and 10 
b

c = b.tolist() #convert back to list
c

mat = sc.array([[0, 1], [2, 3]])
mat.shape

mat[1]
mat[:,1]

mat[0,0]
mat[1,0]

mat[:,0]

mat[0,1]

mat[0,-1]
mat[-1,0]
mat[0,-2]

mat[0,0] = -1 #replace a single element
mat

mat[:,0] = [12,12] #replace whole column
mat

sc.append(mat, [[12,12]], axis = 0) #append row, note axis specification


newRow = [[12,12]]
mat = sc.append(mat, newRow, axis = 0) #append that existing row
mat
sc.delete(mat, 2, 0)

mat = sc.array([[0, 1], [2, 3]])
mat0 = sc.array([[0, 10], [-1, 3]])
mat_large = sc.concatenate((mat, mat0), axis = 0)


mat.ravel() 

mat_large.reshape([2,4])


sc.ones((4,2))
sc.zeros((4,2))
m = sc.identity(4) #create an identity matrix
m

m.fill(16) #fill the matrix with 16
m

mm = sc.arange(16)
mm = mm.reshape(4,4) #Convert to matrix
mm

mm + mm.transpose()
mm - mm.transpose()

mm * mm
mm.dot(mm)

mm = sc.matrix(mm) # convert to scipy matrix class
mm

mm * mm # now matrix multiplication is syntactically easier

# stats

import scipy.stats
sc.random.randn(10)
sc.stats.norm.rvs(size = 10)

# numerical integration

import scipy.integrate as integrate

def dCR_dt(pops, t=0):

    "generate lotka volterra derivatives"

    R = pops[0]
    C = pops[1]
    dRdt = r * R - a * R * C 
    dCdt = -z * C + e * a * R * C
    
    return sc.array([dRdt, dCdt])

r = 1.
a = 0.1 
z = 1.5
e = 0.75

t = sc.linspace(0, 15, 1000)

R0 = 10
C0 = 5 
RC0 = sc.array([R0, C0])

pops, infodict = integrate.odeint(dCR_dt, RC0, t, full_output=True)

pops

infodict.keys()
infodict['message']

# plotting

import matplotlib.pylab as p
f1 = p.figure()
p.plot(t, pops[:,0], 'g-', label='Resource density') # Plot
p.plot(t, pops[:,1]  , 'b-', label='Consumer density')
p.grid()
p.legend(loc='best')
p.xlabel('Time')
p.ylabel('Population density')
p.title('Consumer-Resource population dynamics')
p.show()# To display the figure
f1.savefig('../Results/LV_model.pdf') #Save figure 
