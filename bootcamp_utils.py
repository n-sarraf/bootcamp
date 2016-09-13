# Bootcamp utils: A collection of statistical functions.
# Proved useful to 55 students.

import numpy as np

def ecdf(data):
    '''
    Compute x, y values for an empirical distribution function
    '''

    # Sort data
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y
