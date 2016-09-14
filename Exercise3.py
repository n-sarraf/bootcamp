
import numpy as np
import scipy.stats
import bootcamp_utils

# Import Matplotlib module that we'll need.
import matplotlib.pyplot as plt

import seaborn as sns
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Load data
wt_data = np.loadtxt('data/wt_lac.csv',comments='#',delimiter=',', skiprows=3)
q18m_data = np.loadtxt('data/q18m_lac.csv',comments='#',delimiter=',', skiprows=3)
q18a_data = np.loadtxt('data/q18a_lac.csv',comments='#',delimiter=',', skiprows=3)

# Slice out iptg and fc
wt_iptg = wt_data[:,0]
wt_fc = wt_data[:,1]
q18m_iptg = q18m_data[:,0]
q18m_fc = q18m_data[:,1]
q18a_iptg = q18a_data[:,0]
q18a_fc = q18a_data[:,1]

# Plot ipgt vs fc
plt.close()
plt.semilogx(wt_iptg, wt_fc, linestyle='none', marker='.', markersize=20)
plt.semilogx(q18m_iptg, q18m_fc, linestyle='none', marker='.', markersize=20)
plt.semilogx(q18a_iptg, q18a_fc, linestyle='none', marker='.', markersize=20)
plt.xlabel('IPTG (mM)')
plt.ylabel('Fold change')
plt.title('IPTG Titration')
plt.legend(('WT', 'Q18M', 'Q18A'), loc='lower right')
plt.show()
