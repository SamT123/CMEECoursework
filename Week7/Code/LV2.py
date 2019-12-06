#!/usr/bin/env python3

"""
Program to solve Lotka-Volterra model with prey density dependence by numerical integration. Parameter valeus for r,a,z,e are passed from command line, with K = 20, R0 = 10, C0 = 5 set. If no arguments are passed from command line, default values which give stable population sizes
are used. Outputs final population sizes and saves 'population size vs time' and 'consumer popn size vs resource popn size graphs to pdf.

INPUTS:
    r   =   intrinsic growth rate
    a   =   per capita search rate * attack success probability
    z   =   mortality rate
    e   =   consumer effciency

OUTPUTS:
    ../Results/LV2_C_vs_R.pdf   =   Counsumer and Resource popn sizes vs time
    ../Results/LV2_time.pdf     =   Consumer vs Resource population size plot

"""

__appname__ = 'LV2.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

# imports

import scipy as sc
import scipy.integrate as integrate
import sys

import scipy.integrate as integrate
import scipy as sc
import sys
import matplotlib.pylab as p



def dCR_dt(pops, t=0):
    """
    Calculate dR/dT and dC/dT ( = change in resource and consmer population sizes) given current popuation sizes
    for Lotka- Volterra model with prey density dependent growth.

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
    dRdt = r * R * (1 - R / K) - a * R * C 
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
# plotting

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
    p.text(s = "r = {}\na = {}\nz = {}\ne = {}".format(r,a,z,e),  x = -0.2, y = 9,  bbox=dict(facecolor='white', edgecolor='black',alpha=0.5))

    p.xlabel('Time')
    p.ylabel('Population density')
    p.title('C-R population dynamics - LV with prey density dependence')
    f1.savefig('../Results/LV2_model_vs_t.pdf') #Save figure 


    f2 = p.figure()
    p.plot(pops[:,0], pops[:,1]  , 'r-')
    p.grid()
    p.text(s = "r = {}\na = {}\nz = {}\ne = {}".format(r,a,z,e), x = 9.83, y = 5.4,  bbox=dict(facecolor='white', edgecolor='black',alpha=0.5))

    p.xlabel('Resource density')
    p.ylabel('Consumer density')
    p.title('C-R population dynamics - LV with prey density dependence')
    f2.savefig('../Results/LV2_model_C_vs_R.pdf') #Save figure 


    print("Final resource density = \t{}\nFinal consumer density = \t{}".format(pops[-1][0],pops[-1][1]))
    return



def check_args(args):
    """
    Check if arguments passed from command line are 4 numeric values
    PARAMETERS
    ----------
    args : list
        list of command line parameters


    RETURNS
    -------
    list or 1
        list of float parameter values if no error occurred; otherwise 1
    """
    if len(args) == 0:
        print("Using default parameter values giving stable population sizes: r = 1.0, a = 0.1, z = 0.70, e = 0.75 ")
        return [1.0, 0.1, 0.70, 0.75]


    if len(args) != 4:
        print("Please provide 4 parameter values: r, a, z, e")
        return 1


    try:
        numeric_list = list(map(float, args))
        return numeric_list
    except:
        print("Please provide 4 numeric arguments: r, a, z, e.")
        return 1

    return


def main(args):
    """
    Main entry point for program
    PARAMATERS
    ----------
    args : list
        list of parameters passed from command line, containing r, a, z, e LV parameter values.
        
    RETURNS
    -------
    0 or 1
        0 if no erros encountered; otherwise 1
    """
    # set params


    numeric_args = check_args(args)

    if numeric_args == 1:
        return 1
    
    global r,a,z,e
    r,a,z,e = numeric_args

    global t
    t = sc.linspace(0, 15, 1000)


    global K, R0, C0
    K, R0, C0 = 20, 10, 5

    global RC0
    RC0 = sc.array([R0, C0])

    pops, infodict = run_sim(RC0, t)
    make_plots(pops)

    return 0

if __name__ == '__main__':
    status = main(sys.argv[1:])
    sys.exit(status)









