import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Specify the parameters
n_gen = 16
r_mut = 1e-5
n_cells = 2**(n_gen - 1)

# Adaptive immunity: binomial distribution
ai_samples = np.random.binomial(n_cells, r_mut, 100000)

# Report statistics of adaptive immunity
print('AI mean: ', np.mean(ai_samples))
print('AI std: ', np.std(ai_samples))
print('AI fano factor: ', np.var(ai_samples) / np.mean(ai_samples))

def draw_random_mutation(n_gen, r):
    """Draw sample under random mutation hypothesis."""
    # Initialize number of mutants
    n_mut = 0

    for g in range(n_gen):
        # Mutants always double plus the chance of randomly mutating
        n_mut = 2*n_mut + np.random.binomial(2**g - 2*n_mut, r)

    return n_mut


def sample_random_mutation(n_gen, r, size=1):
    """Samples the random mutations created from draw_random_mutation."""
    # Initialize samples
    samples = np.empty(size)

    # Draw the samples
    for i in range(size):
        samples[i] = draw_random_mutation(n_gen, r)

    return samples

# Random mutation: Jackpot distribution
rm_samples = sample_random_mutation(n_gen, r_mut, size=10000)

# Report statistics of random mutation
print('RM mean: ', np.mean(rm_samples))
print('RM std: ', np.std(rm_samples))
print('RM fano factor: ', np.var(rm_samples) / np.mean(rm_samples))

# Parse the samples into eCDF
x_ai, y_ai = bootcamp_utils.ecdf(ai_samples)
x_rm, y_rm = bootcamp_utils.ecdf(rm_samples)

# Plot the eCDF of both samples
plt.semilogx(x_ai, y_ai, 'b.')
plt.semilogx(x_rm, y_rm, 'r.')
plt.xlabel('Number of mutations')
plt.ylabel('Frequency')
plt.show()
