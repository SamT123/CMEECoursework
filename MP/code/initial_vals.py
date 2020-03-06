""" Generate initial values for Non Linear Least Squares model fitting """

# IMPORTS

import pandas as pd
import os
import matplotlib.pyplot as plt
from collections import Counter
import scipy.stats as stats
import numpy as np
import math

# load data
data = pd.read_csv("../data/LogisticGrowthDataLogClean.csv",index_col=0, sep="\t")
# get unique IDs
IDs = set(data["ID"])

# get unique parameter combinations
combos = list(set(zip(data["ID"],data["Species"],data["Medium"],data["Temp"],data["Rep"])))

# ID --> parameter combination dictionary
combos_dic = {l[0]:l[1:] for l in combos}

# get r for gompertz and baranyi
# this is the maximum gradient of the log10 time series
def log_inits(id, plot_fig):
    time_series = data[data["ID"] == id].sort_values("Time")
    time_series.index = range(0,time_series.shape[0]) 
    #print(time_series)
    n_rolls = time_series.shape[0]
    r_max = 0
    tlag_est = 0
    N0 = min(time_series["logPopBio"])
    if plot_fig:
        fig, ax = plt.subplots()
        ax.scatter(time_series["Time"], time_series["logPopBio"])

    chunk_size = min(int(np.ceil(time_series.shape[0]/4)),5)
    chunk_size = max(chunk_size,3)
    #print(chunk_size)

    for i in range(0,n_rolls-chunk_size-1):
        subset = time_series.iloc[i:i+chunk_size,:]
        fit = stats.linregress(subset["Time"],subset["logPopBio"])
        if fit[0] > r_max :
            r_max = fit[0]
            tlag_est = (N0-fit[1]) /  fit[0]

        if plot_fig:
            ax.plot(subset["Time"], subset["Time"]*fit[0]+fit[1], color = "red")


    if plot_fig:
        plt.show()
    return [min(time_series["logPopBio"]), max(time_series["logPopBio"]), r_max*math.log(10), max(0,tlag_est)]


def lin_inits(id, plot_fig):
    time_series = data[data["ID"] == id].sort_values("Time")
    time_series.index = range(0,time_series.shape[0]) 

    n_rolls = time_series.shape[0]
    r_max = 0
    tlag_est = 0

    if plot_fig:
        fig, ax = plt.subplots()
        ax.scatter(time_series["Time"], time_series["PopBio"])

    for i in range(0,n_rolls-4):
        subset = time_series.iloc[i:i+5,:]
        fit = stats.linregress(subset["Time"],subset["PopBio"])
        if fit[0] > r_max :
            P = np.mean(subset["PopBio"])
            K = np.max(time_series["PopBio"])
            r_max = 1.5*fit[0] / (P * (1 - P / K)) 
            tlag_est = -fit[1] /  fit[0]

        if plot_fig:
            ax.plot(subset["Time"], subset["Time"]*fit[0]+fit[1], color = "red")


    if plot_fig:
        plt.show()
    return [min(time_series["PopBio"]), max(time_series["PopBio"]), r_max, max(0,tlag_est)]


inits = pd.DataFrame(columns = ["ID", "loglin", "param", "value"], index = range(len(IDs)*2))

i = 0
params = ["N0", "Nmax", "rmax", "tlag"]
for id in IDs:
    init_val_id = {"log" : log_inits(id,0), "lin" : lin_inits(id,0)}
    for loglin in init_val_id.keys():
        for j in range(len(params)):
            inits.loc[i] = [id, loglin, params[j], init_val_id[loglin][j]]
            i+=1

inits.to_csv("../data/inits.csv")
