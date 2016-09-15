import numpy as np
import pandas as pd
import seaborn as sns

# Import the frog tongue data frame
df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

# Practice 1: Mstering loc
# Extract the impact time of large adhesive strength
df_big_adhesive = df.loc[np.abs(df['adhesive strength (Pa)']) > 2000,
                         'impact time (ms)']

# Extract the impact force and adhesive force for frog II's strikes
df_frog_ii = df.loc[df['ID']=='II',
                       ['impact force (mN)', 'adhesive force (mN)']]

# Extract adhesive force and pull time for juvenile frog_tongue_adhesion
df_juvenile = df.loc[df['ID'].isin(['III', 'IV'])]

# Practice 2: The power of groupby()

# Long way to find the mean impact force of each frog:
# Extract impact forces for each frog
impf_i = df.loc[df['ID']=='I', 'impact force (mN)']
impf_ii = df.loc[df['ID']=='II', 'impact force (mN)']
impf_iii = df.loc[df['ID']=='III', 'impact force (mN)']
impf_iv = df.loc[df['ID']=='IV', 'impact force (mN)']

# Loop though calculating the mean
frogs = [impf_i, impf_ii, impf_iii, impf_iv]
impf_mean = np.empty(len(frogs))
for i in range(len(frogs)):
    impf_mean[i] = np.sum(frogs[i])

# Now the short way using groupby
# Get the ID's and impact forces
df_impf = df.loc[:, ['ID', 'impact force (mN)']]

# Make a GroupBy object
grouped = df_impf.groupby('ID')

# Apply the np.mean function to the grouped object
df_mean_impf = grouped.apply(np.mean)

# Apply multiple functions to the goruped object
df_agg_impf = grouped.agg([np.mean, np.median])

# Apply the np.std function to the grouped object
df_std_impf = grouped.apply(np.std)

def coeff_of_var(data):
    """Computes the coefficient of variation of a data set.
    This is the std divided by the absolute value of the mean"""
    stdev = np.std(data)
    absmean = np.abs(np.mean(data))
    return stdev / absmean

# Compute the coefficient of variation of the impact and adhesive forces
df_forces = df.loc[:, ['ID', 'impact force (mN)', 'adhesive force (mN)']]
grouped_forces = df_forces.groupby('ID')
df_cov_forces = grouped_forces.apply(coeff_of_var)

# Compute mean, media, std, and cov for impact  and adhesive forces
df_agg_forces = grouped_forces.agg([np.mean, np.median, np.std, coeff_of_var])
