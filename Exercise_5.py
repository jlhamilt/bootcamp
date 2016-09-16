import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize
import seaborn as sns
import bootcamp_utils
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)


# Exercise 5.3: Beak depth and lengths
# Load the tidy data from Exercise 4
grant_data = pd.read_csv('data/my_grant_complete.csv', comment='#')

# Linear model to perfom regression on
def beak_model(depth, m, d0):
    """Linear model for beak length as a function of depth."""
    return d0 + m * depth

# Get the beak depths and lengths of fortis and scandens in every year
beaks = []
beaks_model = []
years = [1973, 1975, 1987, 1991, 2012]

# Initial Guess
m = 1.0
depth0 = 0.0
guess = np.array([m, depth0])

# Iterate through getting the beak depth and length and perfoming regression
for _, yr in enumerate(years):
    # Get the depth and length for each year
    fortis = grant_data.loc[(grant_data['year']==yr) &
                            (grant_data['species']=='fortis'),
                            ['beak depth (mm)', 'beak length (mm)']]
    scandens = grant_data.loc[(grant_data['year']==yr) &
                              (grant_data['species']=='scandens'),
                              ['beak depth (mm)', 'beak length (mm)']]
    beaks.append((fortis, scandens))

    # Get the regression statistics
    p_f, _ = scipy.optimize.curve_fit(beak_model, fortis['beak depth (mm)'],
                                      fortis['beak length (mm)'], p0=guess)
    p_s, _ = scipy.optimize.curve_fit(beak_model, scandens['beak depth (mm)'],
                                      scandens['beak length (mm)'], p0=guess)
    beaks_model.append((p_f, p_s))

# # Unpack the beak stuff
# fortis_beak_73, scandens_beak_73 = beaks[0]
# fortis_beak_75, scandens_beak_75 = beaks[1]
# fortis_beak_87, scandens_beak_87 = beaks[2]
# fortis_beak_91, scandens_beak_91 = beaks[3]
# fortis_beak_12, scandens_beak_12 = beaks[4]
# p_f_73, p_s_73 = beaks_model[0]
# p_f_75, p_s_75 = beaks_model[1]
# p_f_87, p_s_87 = beaks_model[2]
# p_f_91, p_s_91 = beaks_model[3]
# p_f_12, p_s_12 = beaks_model[4]

# Plot all of the depth vs length for all years
show_plot = False
for i, _ in enumerate(beaks):
    # Unpack the beak data
    fortis, scandens = beaks[i]
    p_f, p_s = beaks_model[i]

    # Get the bound for the regressions
    depth = np.linspace(7, 13, 100)
    length_f = beak_model(depth, *tuple(p_f))
    length_s = beak_model(depth, *tuple(p_s))

    # Plot the data and regressions on the same plot
    plt.plot(fortis['beak depth (mm)'], fortis['beak length (mm)'], 'b.')
    plt.plot(scandens['beak depth (mm)'], scandens['beak length (mm)'], 'r.')
    plt.plot(depth, length_f, 'b-')
    plt.plot(depth, length_s, 'r-')
    plt.xlabel('beak depth (mm)')
    plt.ylabel('beak length (mm)')
    plt.legend(('Geospiza fortis', 'Geospiza scandens'), loc='lower right')
    plt.title('Beak Data ' + str(years[i]))
    if show_plot:
        plt.show()
        plt.figure()

    # Print the results
    print("""In {0:d}:
    Scandens: m = {1:.2f}, d0 = {2:.2f}
      Fortis: m = {3:.2f}, d0 = {4:.2f}""".format(years[i], p_s[0], p_s[1],
                                                p_f[0], p_f[1]))
