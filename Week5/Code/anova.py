import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import random

def make_data(means):
    d = []
    for mean in means:
        d.append(list(np.random.randn(100)+mean))
    dflat = [j for i in d for j in i]

    plt.hist(dflat)
    plt.show()
    return d,dflat


def random_anova(dset):
    dflat = [j for i in dset for j in i]

    random.shuffle(dflat)
    dshuf = np.reshape(np.array(dflat), (len(dset), len(dset[0])))

    print(stats.f_oneway(dshuf[0], dshuf[1], dshuf[2], dshuf[3]))
    print(stats.f_oneway(dset[0], dset[1], dset[2], dset[3]))

    return 



a = 10
print('a')