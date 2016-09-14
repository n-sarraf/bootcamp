
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


def fold_change(c, RK, KdA=.017, KdI=.002, Kswitch=5.8):
    '''
    Compute theoretical fold change of mutant.
    '''

    num = RK*(1+c/KdA)**2
    denom = ((1+c/KdA)**2 + Kswitch*(1+c/KdI)**2)
    fc = (1+num/denom)**-1

    return fc

# Create set of data for IPTG concentration
c_wt = np.logspace(1e-6, 15, 500)
c_q18m = np.logspace(1e-6, 15, 500)
c_q18a = np.logspace(1e-6, 15, 500)

plt.close()

# Plot theoretical and real data on same plot
wt_tfc = fold_change(c_wt, 141.5)
q18m_tfc = fold_change(c_q18m, 1332)
q18a_tfc = fold_change(c_q18a, 16.56)
plt.semilogx(wt_iptg, wt_fc, linestyle='none', marker='.', markersize=20)
plt.semilogx(q18m_iptg, q18m_fc, linestyle='none', marker='.', markersize=20)
plt.semilogx(q18a_iptg, q18a_fc, linestyle='none', marker='.', markersize=20)
plt.semilogx(c_wt, wt_tfc)
plt.semilogx(c_q18m, q18m_tfc)
plt.semilogx(c_q18a, q18a_tfc)
plt.xlabel('IPTG (mM)')
plt.ylabel('Fold change')
plt.title('IPTG Titration')
plt.legend(('WT', 'Q18M', 'Q18A', 'Th WT', 'Th Q18M', 'Th Q18A'), loc='upper left')
plt.show()


def bohr_parameter(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    '''
    Calculate Bohr parameter.
    '''

    num = (1 + c/KdA)**2
    denom = (1 + c/KdA)**2 + Kswitch*(1+c/KdI)**2
    fc = -np.log(RK)-log(num/denom)

    return fc


def fold_change_bohr(bohr_parameter):
    '''
    Calculate fold change as a function of the Bohr parameter.
    '''

    fc = 1/(1+np.exp(-bohr_parameter))

    return fc
