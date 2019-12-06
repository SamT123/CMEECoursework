#!/usr/bin/env python3

"""
Program to solve Lotka-Volterra model with hard-coded paramterter values, by numerical integration. Outputs final population sizes and saves 'population size vs time' and 'consumer popn size vs
resource popn size' graphs to pdf.

INPUTS:
    None

OUTPUTS:
    ../Results/LV1_C_vs_R.pdf   =   Counsumer and Resource popn sizes vs time
    ../Results/LV1_time.pdf     =   Consumer vs Resource population size plot
"""

__appname__ = 'LV1.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

# imports
import scipy.integrate as integrate
import scipy as sc
import sys
import matplotlib.pylab as p



def dCR_dt(pops, t=0):
    """
    Calculate dR/dT and dC/dT ( = change in resource and consmer population sizes) given current popuation sizes
    for Lotka- Volterra model.

    PARAMETERS
    ----------
    pops : array, list
        list of length 2; first element is Resource population size, second element is Consumer population size
    t : float,int
        time

    RETURNS
    -------
    array
        array containing dR/dT and dC/dT
    """
    R = pops[0]
    C = pops[1]
    dRdt = r * R - a * R * C 
    dCdt = -z * C + e * a * R * C
    
    return sc.array([dRdt, dCdt])

def run_sim(RC0, t):
    """
    Solve Lotka-Volterra Model by numerical integraton, for a given initial population sizes
    
    PARAMETERS
    ----------
    RC0 : array, list
        inital Resource and Consumer population sizes
    t : array
        time values at which to perform numerical integration

    RETURNS
    -------
    pops : array
        array of Consumer and Resource population sizes at each timestep in argument t
    infodict : dict
        dictionary containing information about the integration
     """
    pops, infodict = integrate.odeint(dCR_dt, RC0, t, full_output=True)
    return pops, infodict

def make_plots(pops):
    """
    Make and save plots of population size vs time, and Consumer population size vs Resource population size

    PARAMETERS
    ----------
    pops : array
        array of population sizes at each timestep

    RETURNS
    -------
    None

    """
    f1 = p.figure()
    p.plot(t, pops[:,0], 'g-', label='Resource density') # Plot
    p.plot(t, pops[:,1]  , 'b-', label='Consumer density')
    p.grid()
    p.legend(loc='best')
    p.xlabel('Time')
    p.ylabel('Population density')
    p.title('Consumer-Resource population dynamics - Basic Lotka Volterra Model')

    f1.savefig('../Results/LV1_time.pdf') #Save figure 


    f2 = p.figure()

    p.plot(pops[:,0], pops[:,1]  , 'r-')
    p.grid()
    p.xlabel('Resource density')
    p.ylabel('Consumer density')
    p.title('Consumer-Resource population dynamics - Basic Lotka Volterra Model')

    f2.savefig('../Results/LV1_C_vs_R.pdf') #Save figure 

    print("Final resource density = \t{}\nFinal consumer density = \t{}".format(pops[-1][0],pops[-1][1]))

    return None

def main():
    """ Main entry point for program; set global variables to specify and evaluate LV model. """
    # set params

    global r,a,z,e
    r,a,z,e = 1., 0.1, 0.80, 0.75


    global t
    t = sc.linspace(0, 15, 1000)

    global R0, C0
    R0, C0 = 10, 5
    global RC0

    RC0 = sc.array([R0, C0])

    pops, infodict = run_sim(RC0, t)
    make_plots(pops)

    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)