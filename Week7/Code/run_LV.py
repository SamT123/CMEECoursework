#!/usr/bin/env python3

""" Run and profile 4 Lotka Volterra programs. Prints the top 20 calls by tottime to terminal"""


__appname__ = 'LV_run.py'
__author__  = 'Sam Turner (sat19@ic.ac.uk)'
__version__ = '0.0.1'
__license__ = 'GNU public' 

# imports
import LV1
import LV2
import LV3
import LV4
import cProfile
import pstats


# LV1 : Simple LV

prof = cProfile.Profile()

prof.enable()
LV1.main()
prof.disable()

print("\nLV1 profile - top 20 by tottime:\n--------------------------------")
ps = pstats.Stats(prof)
ps.sort_stats("tottime").print_stats(20)

# LV2 : add resource density dependant growth

prof = cProfile.Profile()

prof.enable()
LV2.main([])
prof.disable()

print("\nLV2 profile - top 20 by tottime:\n--------------------------------")
ps = pstats.Stats(prof)
ps.sort_stats("tottime").print_stats(20)

# LV3 : discrete time LV model

prof = cProfile.Profile()

prof.enable()
LV3.main([])
prof.disable()

print("\nLV3 profile - top 20 by tottime:\n--------------------------------")
ps = pstats.Stats(prof)
ps.sort_stats("tottime").print_stats(20)

# LV4 discrete time with random Gaussian fluctuations each timestep

prof = cProfile.Profile()

prof.enable()
LV4.main([])
prof.disable()

print("\nLV4 profile - top 20 by tottime:\n--------------------------------")
ps = pstats.Stats(prof)
ps.sort_stats("tottime").print_stats(20)






