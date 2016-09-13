import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats

# Load data sets
data_txt = np.loadtxt('data/collins_switch.csv', delimiter=',', skiprows=2)
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

# Slice out iptg and gfp
iptg = data_txt[:,0]
gfp = data_txt[:,1]
sem = data_txt[:,2]

# # Plot ipgt vs gfp
# plt.close()
# plt.semilogx(iptg, gfp, linestyle='none', marker='.', markersize=16)
# plt.xlim(8e-4, 15)
# plt.ylim(-0.02, 1.02)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')
# plt.title('IPTG Titration: semilog x')
# plt.show()

# Plot iptg vs gfp with error bars
# plt.close()
# plt.errorbar(iptg, gfp, yerr=sem, linestyle='none', marker='.', markersize=16)
# plt.xlim(8e-4, 15)
# plt.ylim(-0.02, 1.02)
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')
# plt.xscale('log')
# plt.title('IPTG Titration: semilog x')
# plt.show()

# Work for Exercise 3
def ecdf(data):
    """Compute x, y values for an empirical distribution function.
    Input data set is a vector of values."""

    # Need data in order to sum
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y

# Get the x and y for ecdf for the data
x_high, y_high = ecdf(xa_high)
x_low, y_low = ecdf(xa_low)

# Plot the data
plt.close()
plt.plot(x_high, y_high, marker='.', linestyle='none', markersize=16, alpha=0.5)
plt.plot(x_low, y_low, marker='.', linestyle='none', markersize=16, alpha=0.5)
plt.xlabel('Cross-sectional area ($\mu m^2$)')
plt.ylabel('eCDF')
plt.legend(('high food', 'low food'), loc='lower right')
plt.show()
