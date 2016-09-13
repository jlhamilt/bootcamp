import numpy as np

xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

def xa_to_diam(x):
    """Converts an array of cross-sectional areas to
    diameters with commensurate units"""

    # Compute diameter
    diam = np.sqrt(x * 4 / np.pi)
    return diam
