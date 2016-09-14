import numpy as np
import matplotlib.pyplot as plt
import bootcamp_utils
import seaborn as sns
sns.set()

# Load the beak depth data
bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

# # Use the bootstrap method to generate new samples
# n_reps = 100000
# bs_repl1975_mean = np.empty(n_reps)
# bs_repl2012_mean = np.empty(n_reps)
# for i in range(n_reps):
#     bs_sample_1975 = np.random.choice(bd_1975, replace=True, size=len(bd_1975))
#     bs_sample_2012 = np.random.choice(bd_2012, replace=True, size=len(bd_2012))
#     bs_repl2012_mean[i] = np.mean(bs_sample_1975)
#     bs_repl2012_mean[i] = np.mean(bs_sample_2012)

# Use the bootstrap function in utils
bs_repl1975_mean = bootcamp_utils.draw_bs_reps(bd_1975, np.mean, size=100000)
bs_repl2012_mean = bootcamp_utils.draw_bs_reps(bd_2012, np.mean, size=100000)

conf_int_1975 = np.percentile(bs_repl1975_mean, [2.5, 97.5])
conf_int_2012 = np.percentile(bs_repl2012_mean, [2.5, 97.5])
print('Confidence Interval for 1975 is {0}\n\
Confidence Interval for 2012 is {1}'.format(conf_int_1975, conf_int_2012))

# # Get the eCDF
# x_1975, y_1975 = bootcamp_utils.ecdf(bd_1975)
# x_2012, y_2012 = bootcamp_utils.ecdf(bd_2012)
#
# # Plot the eCDF
# plt.plot(x_1975, y_1975, marker='.', linestyle='none')
# plt.plot(x_2012, y_2012, marker='.', linestyle='none')
# plt.xlabel('Beak Depth (mm)')
# plt.ylabel('eCDF')
# plt.legend(('1975', '2012'), loc='lower right')
# plt.show()
