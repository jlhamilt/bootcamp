"""
bootcamp_utils: A collection of statistical functions proved useful
during the course and in future endeavors
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def ecdf(data):
    """Compute x, y values for an empirical distribution function.
    Input data set is a vector of values."""

    # Need data in order to sum
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y

# Bootstrap method functions
def draw_bs_reps(data, func, size=1):
    """Uses the bootstrap method to sample the data and return
    the statistic defined by the func."""

    # Initialize the array of replicates
    reps = np.empty(size)

    # Draw a bootstrap sample and compute the statistic
    for i in range(size):
        bs_rep = np.random.choice(data, replace=True, size=len(data))
        reps[i] = func(bs_rep)

    return reps

def bs_conf_int(data, func, size=1000, interval=95):
    """Uses the bootstrap method to compute the confidence interval
    of a given statistical function. Returns the confidence interval
    as a NumPy array."""

    # Get the bootstrap sample
    reps = draw_bs_reps(data, func, size=size)

    # Get the interval range for percentiles
    n = (100 - interval) / 2
    interval_range = [n, 100-n]

    # Create the confidence interval
    conf_int = np.percentile(reps, interval_range)
    return conf_int
