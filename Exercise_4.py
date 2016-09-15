import numpy as np
import matplotlib.pyplot as plt
import bootcamp_utils
import seaborn as sns
import pandas as pd

# Set matplotlib rc parameters
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Exercise 4.1: Long-term trends in hybridization of Darwin finches
# Load each file as a DataFrame
grant73 = pd.read_csv('data/grant_1973.csv', comment='#')
grant75 = pd.read_csv('data/grant_1975.csv', comment='#')
grant87 = pd.read_csv('data/grant_1987.csv', comment='#')
grant91 = pd.read_csv('data/grant_1991.csv', comment='#')
grant12 = pd.read_csv('data/grant_2012.csv', comment='#')

# Get rid of the yearband column in the 1973 data
grant73 = grant73.loc[:, ['band', 'species', 'beak length', 'beak depth']]

# List of the files and desired column names
files = [grant73, grant75, grant87, grant91, grant12]
desired_cols = ['band', 'species', 'beak length (mm)', 'beak depth (mm)', 'year']
years = [1973, 1975, 1987, 1991, 2012]

# Iterate through and change the column names
for index, grant in enumerate(files):

    # Create the year column
    grant['year'] = pd.Series(np.full(len(grant['band']),
                              years[index], dtype=int))

    # Create the dictionary for column names
    column_names = {}
    for i in range(len(desired_cols)):
        column_names[grant.columns[i]] = desired_cols[i]

    # Rename the columns
    files[index] = grant.rename(columns=column_names)

# Save the new DataFrame to the variables
grant73 = files[0]
grant75 = files[1]
grant87 = files[2]
grant91 = files[3]
grant12 = files[4]

# Concatenate the list
grant_data = pd.concat((grant73, grant75, grant87, grant91, grant12),
                       ignore_index=True)

# Drop duplicate birds within the same year
grant_data = grant_data.drop_duplicates(['year', 'band'])

# Save this DataFrame as a csv
grant_data.to_csv('data/my_grant_complete.csv', index=False)

# Get the beak depths and lengths of fortis and scandens in every year
beaks = []

# Iterate through getting the beak depth and length
for _, yr in enumerate(years):
    fortis = grant_data.loc[(grant_data['year']==yr) &
                            (grant_data['species']=='fortis'),
                            ['beak depth (mm)', 'beak length (mm)']]
    scandens = grant_data.loc[(grant_data['year']==yr) &
                              (grant_data['species']=='scandens'),
                              ['beak depth (mm)', 'beak length (mm)']]
    beaks.append((fortis, scandens))

# Unpack the beak stuff
fortis_beak_73, scandens_beak_73 = beaks[0]
fortis_beak_75, scandens_beak_75 = beaks[1]
fortis_beak_87, scandens_beak_87 = beaks[2]
fortis_beak_91, scandens_beak_91 = beaks[3]
fortis_beak_12, scandens_beak_12 = beaks[4]

# Plot and ECDF of beak depths of fortis vs scandens in 1987
fortis_ecdf = bootcamp_utils.ecdf(fortis_beak_87['beak depth (mm)'])
scandens_ecdf = bootcamp_utils.ecdf(scandens_beak_87['beak depth (mm)'])
plt.close()
plt.plot(fortis_ecdf[0], fortis_ecdf[1], 'b.')
plt.plot(scandens_ecdf[0], scandens_ecdf[1], 'r.')
plt.xlabel('beak depth (mm)')
plt.ylabel('ECDF')
plt.legend(('Geospiza fortis', 'Geospiza scandens'), loc='lower right')
# plt.show()

# Plot all of the depth vs length for all years
show_plot = False
for i in range(len(beaks)):
    fortis, scandens = beaks[i]
    plt.close()
    plt.plot(fortis['beak depth (mm)'], fortis['beak length (mm)'], 'b.')
    plt.plot(scandens['beak depth (mm)'], scandens['beak length (mm)'], 'r.')
    plt.xlabel('beak depth (mm)')
    plt.ylabel('beak length (mm)')
    plt.legend(('Geospiza fortis', 'Geospiza scandens'), loc='lower right')
    plt.title('Beak Data ' + str(years[i]))
    if show_plot:
        plt.show()


# Exercise 4.2: Hacker stats on bee sperm data
# Load in the data
drone_weight = pd.read_csv('data/bee_weight.csv', comment='#')
drone_sperm = pd.read_csv('data/bee_sperm.csv', comment='#')

# Get the control and  pesticide data
cont_weight = drone_weight.loc[drone_weight['Treatment']=='Control', 'Weight']
pest_weight = drone_weight.loc[drone_weight['Treatment']=='Pesticide', 'Weight']
cont_sperm = drone_sperm.loc[(drone_sperm['Treatment']=='Control') &
                             (drone_sperm['Quality'] >= 0), 'Quality']
pest_sperm = drone_sperm.loc[(drone_sperm['Treatment']=='Pesticide') &
                             (drone_sperm['Quality'] >= 0), 'Quality']

# Get the ECDFs
cont_weight_x, cont_weight_y = bootcamp_utils.ecdf(cont_weight)
pest_weight_x, pest_weight_y = bootcamp_utils.ecdf(pest_weight)
cont_sperm_x, cont_sperm_y = bootcamp_utils.ecdf(cont_sperm)
pest_sperm_x, pest_sperm_y = bootcamp_utils.ecdf(pest_sperm)

# Plot the ECDFs
plt.close()
plt.plot(cont_weight_x, cont_weight_y, 'b.')
plt.plot(pest_weight_x, pest_weight_y, 'r.')
plt.xlabel('Weight (mg)')
plt.ylabel('ECDF')
plt.legend(('Control', 'Pesticide'), loc='lower right')
# plt.show()

plt.close()
plt.plot(cont_sperm_x, cont_sperm_y, 'b.')
plt.plot(pest_sperm_x, pest_sperm_y, 'r.')
plt.xlabel('Quantity')
plt.ylabel('ECDF')
plt.legend(('Control', 'Pesticide'), loc='lower right')
# plt.show()

# # Confidence intervals for the mean and median of the samples
# print('Confidence interval for mean weight of control: ',
#        bootcamp_utils.bs_conf_int(cont_weight, np.mean, 10000))
# print('Confidence interval for mean weight of pesticide treatment: ',
#        bootcamp_utils.bs_conf_int(pest_weight, np.mean, 10000))
# print('Confidence interval for mean sperm of control: ',
#        bootcamp_utils.bs_conf_int(cont_sperm, np.mean, 10000))
# print('Confidence interval for mean sperm of pesticide treatment: ',
#        bootcamp_utils.bs_conf_int(pest_sperm, np.mean, 10000))
# print('Confidence interval for median weight of control: ',
#        bootcamp_utils.bs_conf_int(cont_weight, np.median, 10000))
# print('Confidence interval for median weight of pesticide treatment: ',
#        bootcamp_utils.bs_conf_int(pest_weight, np.median, 10000))
# print('Confidence interval for median sperm of control: ',
#        bootcamp_utils.bs_conf_int(cont_sperm, np.median, 10000))
# print('Confidence interval for median sperm of pesticide treatment: ',
#        bootcamp_utils.bs_conf_int(pest_sperm, np.median, 10000))

# Exercise 4.3
