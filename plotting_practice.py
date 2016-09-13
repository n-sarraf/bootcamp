import numpy as np
import scipy.stats

# Import the module of Matplotlib we'll need.
import matplotlib.pyplot as plt

import seaborn as sns
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

data_txt = np.loadtxt('data/collins_switch.csv', delimiter=',', skiprows=2)

# Slice out iptg and gfp
iptg = data_txt[:,0]
gfp = data_txt[:,1]

# Plot ipgt vs gfp
plt.semilogx(iptg, gfp, linestyle='none', marker='.', markersize=20)
plt.xlabel('IPTG (mM)')
plt.ylabel('Normalized GFP')
plt.show()
