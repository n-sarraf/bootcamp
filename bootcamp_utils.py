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


def draw_bs_reps(data, func, size=1):
    '''
    Generate bootstrap replicates from an experimental data set.
    func refers to the statistical operation you would like to perform. ex: std, median, mean.
    '''

    # Draw bootstrap sample and store in array
    n=len(data)
    reps = np.empty(size)
    for i in range (size):
        bs_sample = np.random.choice(data, replace=True, size=n)
        reps[i] = func(bs_sample)

    return reps
