#!/usr/bin/env python3

"""
Program to simulate discrete time Lotka-Volterra model with paramterter values passed from command line, with random Gaussian fluctuation in both population size each generation.

INPUTS:
    R0  =   initial resource population size
    C0  =   initial consumer population size
    K   =   resource carrying capacity
    r   =   intrinsic growth rate
    a   =   per capita search rate * attack success probability
    z   =   mortality rate
    e   =   consumer effciency
    gens=   number of generations to run model for

OUTPUTS:
    ../Results/LV3_C_vs_R.pdf   =   Counsumer and Resource popn sizes vs time
    ../Results/LV3_time.pdf     =   Consumer vs Resource population size plot
    """

__appname__ = 'LV4.py'
__author__ = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

# imports
import sys
import numpy as np
import matplotlib.pylab as p

def main(args):
    """
    Main entry point for program.
    
    PARAMETERS
    ----------
    args : list
        list of parameters passed from command line
        
    RETURNS
    -------
    0 or 1
        0 if successful, 1 otherwise
    """
    numeric_args = check_args(args)

    if numeric_args == 1:
        return 1



    global R0, C0, K, r, a, z, e,  gens
    R0, C0, K, r, a, z, e,  gens = numeric_args
    gens = int(gens)
    densities = np.zeros([gens,2])
    densities[0] =  np.array([R0,C0])
    densities = simulate(densities)
    make_plots(densities)
    return 0


def simulate(densities):
    """
    Runs discrete time LV model with Gaussian fluctuations using paramters specified as globals in main()
    
    PARAMTERS
    ---------
    densities : array
        array of initial population densities [R0, C0]
    
    RETURNS
    -------
    array
        2D array of resource and consumer densities at each timestep
    """
    fluctuations = np.random.randn(gens-1,2)/10
    for gen in range(1,gens):
        R = densities[gen-1][0]
        C = densities[gen-1][1]
        densities[gen][0] = R * (1 + (r + fluctuations[gen-1,0]) * (1 - R / K) - a * C)
        densities[gen][1] = C * (1 - z + e * a * R + fluctuations[gen-1,1])


    return densities


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
    t = range(len(pops))

    f1 = p.figure()
    p.plot(t, pops[:,0], 'g-', label='Resource density') # Plot
    p.plot(t, pops[:,1]  , 'b-', label='Consumer density')
    p.grid()
    p.legend(loc='best')
    p.text(s = "r = {}\na = {}\nz = {}\ne = {}".format(r,a,z,e),  x = -0.5, y = 35,  bbox=dict(facecolor='white', edgecolor='black'))

    p.xlabel('Time')
    p.ylabel('Population density')
    p.title('C-R population dynamics - discrete time LV with popn. fluctuation')
    f1.savefig('../Results/LV4_model_vs_t.pdf') #Save figure 


    f2 = p.figure()
    p.plot(pops[:,0], pops[:,1]  , 'r-')
    p.grid()
    p.text(s = "r = {}\na = {}\nz = {}\ne = {}".format(r,a,z,e), x = 35, y = 20,  bbox=dict(facecolor='white', edgecolor='black'))

    p.xlabel('Resource density')
    p.ylabel('Consumer density')
    p.title('C-R population dynamics - discrete time LV with popn. fluctuation')
    f2.savefig('../Results/LV4_model_C_vs_R.pdf') #Save figure 


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
        print("Using default parameter values: R0 = 5, C0 = 10, K = 20, r = 1, a = 0.1, z = 0.70, e = 0.75, gens = 100")
        return [5, 10, 20, 1.0, 0.1, 0.70, 0.75,100]

    if len(args) != 8:
        print("Please provide 8 parameter values: R0, C0, K, r, a, z, e,  gens")
        return 1


    try:
        numeric_list = list(map(float, args))
        return numeric_list
    except:
        print("Please provide 8 numeric arguments: R0, C0, K, r, a, z, e,  gens.")
        return 1

    return



if __name__ == '__main__':
    status = main(list(map(float, sys.argv[1:])))
    sys.exit(status)