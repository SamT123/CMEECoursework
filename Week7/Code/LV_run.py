""" Run and profile 4 Lotka Volterra programs. """

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

print("LV1 profile - top 20 by tottime:")
ps = pstats.Stats(prof)
ps.sort_stats("tottime").print_stats(20)

# LV2 : add resource density dependant growth

prof = cProfile.Profile()

prof.enable()
LV2.main([])
prof.disable()

print("LV2 profile - top 20 by tottime:")
ps = pstats.Stats(prof)
ps.sort_stats("tottime").print_stats(20)

# LV3 : discrete time LV model

prof = cProfile.Profile()

prof.enable()
LV3.main([])
prof.disable()

print("LV3 profile - top 20 by tottime:")
ps = pstats.Stats(prof)
ps.sort_stats("tottime").print_stats(20)

# LV4 discrete time with random Gaussian fluctuations each timestep

prof = cProfile.Profile()

prof.enable()
LV4.main([])
prof.disable()

print("LV4 profile - top 20 by tottime:")
ps = pstats.Stats(prof)
ps.sort_stats("tottime").print_stats(20)






