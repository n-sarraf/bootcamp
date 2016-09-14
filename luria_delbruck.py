import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Specify parameters

# Number of generations
n_gen = 16

# Chance of having a beneficial mutation
r = 1e-5

# Total number of cells
n_cells = 2**(n_gen - 1)

# Adaptive immunity: binomial distribution
ai_samples = np.random.binomial(n_cells, r, size=100000)

# Report mean and standard deviation
print('AI mean: ', np.mean(ai_samples))
print('AI std: ', np.std(ai_samples))
print('AI Fano: ', np.var(ai_samples) / np.mean(ai_samples))
