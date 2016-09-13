"""
bootcamp_utils: A collection of statistical functions proved useful
during the course and in future endeavors
"""

import numpy as np

def ecdf(data):
    """Compute x, y values for an empirical distribution function.
    Input data set is a vector of values."""

    # Need data in order to sum
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y
