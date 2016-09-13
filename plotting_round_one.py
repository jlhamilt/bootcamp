import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the food data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

# Set matplotlib rc parameters
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Make the bins
bins = np.arange(1700, 2500, 50)
# Plot the data as a histogram.
_ = plt.hist(xa_low, bins=bins)
plt.xlabel("Cross-sectional area ($\mu m ^2$)")
plt.ylabel('Count')
plt.show()
