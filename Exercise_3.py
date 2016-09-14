import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.integrate
rc={'lines.linewidth': 2, 'axes.labelsize':18, 'axes.titlesize':18}
sns.set(rc=rc)


# Exercise 3.2 Data Collapse

# Create a function for the theoretical fold change
def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """Compute the theoretical fold change based on the
    Monod-Wyman-Changeux model. Inputs should be numpy arrays
    or constants. Keyword args represend the parameter values
    but can modified."""

    fold = 1 + (RK*(1 + c/KdA)**2) / ((1 + c/KdA)**2 + Kswitch*(1 + c/KdI)**2)
    return fold**-1


def bohr_parameter(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """Compute the Bohr parameter for a concentration and R/K
    value. Inputs should be numpy arrays or constants."""

    indep = (1 + c/KdA)**2 / ((1 + c/KdA)**2 + Kswitch*(1 + c/KdI)**2)
    bohr = -np.log(RK) - np.log(indep)
    return bohr


def fold_change_bohr(bohr_parameter):
    """Gives the fold change as a function of Bohr parameter."""

    fold = 1 / (1 + np.e**(-bohr_parameter))
    return  fold


# Load the lac data
wt_lac = np.loadtxt('data/wt_lac.csv', delimiter=',', skiprows=3)
q18m_lac = np.loadtxt('data/q18m_lac.csv', delimiter=',', skiprows=3)
q18a_lac = np.loadtxt('data/q18a_lac.csv', delimiter=',', skiprows=3)

# Extract the IPTG and fold change
wt_iptg, wt_fold = (wt_lac[:, 0], wt_lac[:, 1])
q18m_iptg, q18m_fold = (q18m_lac[:, 0], q18m_lac[:, 1])
q18a_iptg, q18a_fold = (q18a_lac[:, 0], q18a_lac[:, 1])

# Create the theoretical fold data
x = np.logspace(-5, 1.5, 400)
wt_tfold = fold_change(x, 141.5)
q18a_tfold = fold_change(x, 16.56)
q18m_tfold = fold_change(x, 1332)

# Create the theoretical fold data using Bohr parameter
bohr_param = np.linspace(-6, 6, 400)
tfold = fold_change_bohr(bohr_param)

# Create the Bohr parameters for the mutants
wt_bohr = bohr_parameter(wt_iptg, 141.5)
q18a_bohr = bohr_parameter(q18a_iptg, 16.56)
q18m_bohr = bohr_parameter(q18m_iptg, 1332)

# Plot each of the mutants against the theoretical fold
plt.close()
plt.semilogx(wt_iptg, wt_fold, 'b.', markersize=14)
plt.semilogx(q18m_iptg, q18m_fold, 'g.', markersize=14)
plt.semilogx(q18a_iptg, q18a_fold, 'r.', markersize=14)
plt.semilogx(x, wt_tfold, 'b-')
plt.semilogx(x, q18m_tfold, 'g-')
plt.semilogx(x, q18a_tfold, 'r-')
plt.xlabel('IPTG (mM)')
plt.ylabel('Fold Change')
plt.legend(('Wild Type', 'Q18M', 'Q18A'), loc='upper left')
plt.title('Lac Repressor Theoretical Fold Change')
# plt.show()

# Plot each of the experimentals using the Bohr parameter
plt.close()
plt.plot(wt_bohr, wt_fold, 'b.', markersize=14)
plt.plot(q18m_bohr, q18m_fold, 'g.', markersize=14)
plt.plot(q18a_bohr, q18a_fold, 'r.', markersize=14)
plt.plot(bohr_param, tfold, color='gray')
plt.xlabel('Bohr Parameter')
plt.ylabel('Fold Change')
plt.legend(('Wild Type', 'Q18M', 'Q18A'), loc='upper left')
plt.title('Lac Repressor Bohr Fold Change')
# plt.show()


# Exercise 3.3: Solving difeqs with NumPy
# Solves the population equation for two coupled differential equations
# dr/dt = alpha*r - beta*f*r
# df/dt = delta*f*r - gamma*f

# Given parameter values:
alpha = 1
beta = 0.2
delta = 0.3
gamma = 0.8
delta_t = 0.001

# Make the time points and empty arrays
t = np.arange(0, 60, delta_t)
r = np.empty_like(t)
f = np.empty_like(t)

# Set the initial rabbits and foxes
r[0] = 10
f[0] = 1

# Use Euler's method to iterate through time
for i in range(1, len(t)):
    r[i] = r[i-1] + delta_t * r[i-1] * (alpha - beta * f[i-1])
    f[i] = f[i-1] + delta_t * f[i-1] * (delta * r[i-1] - gamma)

# Plot the rabbit and fox populations
plt.close()
plt.plot(t, r)
plt.plot(t, f)
plt.xlabel('Time')
plt.ylabel('Population')
plt.title("Euler's Method for Population Growth")
plt.legend(('Rabbit', 'Fox'))
# plt.show()

# Bonus exercise using odeint
