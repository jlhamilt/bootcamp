import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.special

# Generate an array of x values
x = np.linspace(-15, 15, 400)

# Compute the normalized intensity
norm_I = 4 * (scipy.special.j1(x) / x)**2

# Plot our computation
plt.close()
plt.plot(x, norm_I, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('$x$')
plt.ylabel('$ I(x) / I_0$')

# Processing the spike data.
data = np.loadtxt('data/retina_spikes.csv', skiprows=2, delimiter=',')
t = data[:,0]
v = data[:,1]

# Plot the spike data
plt.close()
plt.plot(t, v)
plt.xlabel('t ($ms$)')
plt.ylabel('V ($\mu V$)')
plt.xlim(1395, 1400)
