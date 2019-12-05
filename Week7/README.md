# Week 7
Coursework for CMEE week 7.
## Topics:
* PythonII

## Contents
### [Code](https://github.com/SamT123/CMEECoursework/tree/master/Week7/Code)
**blackbirds.py**
* Solution to regex practical, extracting Kingdom, Phylum, and Species information from text file

**DrawFW.py**
* Program generating random food web

**fmr.R**
* Plots log(field metabolic rate) against log(body size) and fits linear model for Nagy 1999 dataset

**run_fmr_R.py**
* Run fmr.R from python using a subprocess


**LV1.py**
* Solves basic Lotka Volterra model by numerical integration, outputting final population sizes and graphs of:
    * Consumer vs Producer population sizes
    * Consumer and Producer population size vs time

**LV2.py**
* Solves Lotka Volterra model with prey density dependence by numerical integration. Takes parameter values from command line (r, a, z, e), or if absent, uses defaults giving stable final population sizes. Outputs final population sizes and graphs of:
    * Consumer vs Producer population sizes
    * Consumer and Producer population size vs time
* Example usage:
`python3 LV2.py 1.0 0.1 0.70 0.75`

**LV3.py**
* Solves discrete time Lotka Volterra model with parameters R0, C0, K, r, a, z, e passed from command line. If absent, default
parameter values are used. Outputs final population sizes and graphs of:
    * Consumer vs Producer population sizes
    * Consumer and Producer population size vs time
* Example usage:
`python3 LV3.py 5 10 20 1.0 0.1 0.70 0.75 100`

**LV4.py**
* Solves discrete time Lotka Volterra model with random Gaussian fluctuation with parameters R0, C0, K, r, a, z, e passed from
command line. If absent, default parameter values are used. Outputs final population sizes and graphs of:
    * Consumer vs Producer population sizes
    * Consumer and Producer population size vs time
* Example usage:
`python3 LV4.py 5 10 20 1.0 0.1 0.70 0.75 100`

**LV_run.py**
* Runs and profiles all of LV1.py, LV2.py, LV3.py, LV4.py. Shows profile of top 20 calls by tottime.

**Nets.py**
* Makes graphs representing QMEE collaboration netwrok, with Node size representing number of collaborators within institution and 
edge width representing number of collaborations between institutions.

**Nets.R**
* Makes graphs representing QMEE collaboration netwrok, with Node size representing number of members within institution and 
edge width representing number of collaborations between institutions.

**profileme.py**
* Squaring and string concatenation functions inefficiently implemented to demonstrate optimization.
    * Squaring: uses for loop
    * Str conc: uses .join() method

**profileme2.py**
* Squaring and string concatenation functions more efficiently implemented.
    * Squaring: list comprehension
    * Str conc: direct str + str concatenation

**profileme_np.py**
* Squaring and string concatenation functions inefficiently implemented to demonstrate optimization.
    * Squaring: numpy array operations
    * Str conc: direct str + str concatenation


**timeitme.py**
* Times functions in profileme* scripts to show benefits of optimization

**regex.py**
* Script from regex lectures

**sc.py**
* Script from scipy lectures

**TestR.R**
* Test script to demonstrate subprocess

**using_os.py**
* Directory walking exercises



### [Data](https://github.com/SamT123/CMEECoursework/tree/master/Week7/Data)
**blackbirds.txt**
    * Text file with phylogeny data for balckbird species.

**NagyEtAl1999**
    * Field metabolic rate and body size data from Nagy et al. 1999.

**QMEE_Net_Mat_edges.csv**
    * Pairwise number of collaborations data for QMEE institutions.

**QMEE_Net_Mat_nodes.csv**
    * Number of members data for QMEE institutions.


### [Results](https://github.com/SamT123/CMEECoursework/tree/master/Week7/Results)
