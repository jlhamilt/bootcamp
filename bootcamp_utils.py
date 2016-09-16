"""
bootcamp_utils: A collection of statistical functions proved useful
during the course and in future endeavors
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)
# Our image processing tools
import skimage.filters
import skimage.io
import skimage.measure
import skimage.morphology
import skimage.segmentation


def ecdf(data):
    """Compute x, y values for an empirical distribution function.
    Input data set is a vector of values."""

    # Need data in order to sum
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y

# Bootstrap method functions
def draw_bs_reps(data, func, size=1):
    """Uses the bootstrap method to sample the data and return
    the statistic defined by the func."""

    # Initialize the array of replicates
    reps = np.empty(size)

    # Draw a bootstrap sample and compute the statistic
    for i in range(size):
        bs_rep = np.random.choice(data, replace=True, size=len(data))
        reps[i] = func(bs_rep)

    return reps

def bs_conf_int(data, func, size=1000, interval=95):
    """Uses the bootstrap method to compute the confidence interval
    of a given statistical function. Returns the confidence interval
    as a NumPy array."""

    # Get the bootstrap sample
    reps = draw_bs_reps(data, func, size=size)

    # Get the interval range for percentiles
    n = (100 - interval) / 2
    interval_range = [n, 100-n]

    # Create the confidence interval
    conf_int = np.percentile(reps, interval_range)
    return conf_int

def plot_bs_ecdf(data, size=1,show=True, plt_orig=True):
    """Plots the bootstrap of the data. Will not show the plot
    if show is false, allowing for later plot modifications."""
    # Plot the original
    if plt_orig:
        orig_x, orig_y = ecdf(data)
        plt.plot(orig_x, orig_y, 'r.', markersize=14)
    # Plot the bootstrap samples
    for i in range(size):
        bs_x, bs_y = ecdf(np.random.choice(data, replace=True, size=len(data)))
        plt.plot(bs_x, bs_y, 'b.', markersize=10, alpha=0.5)

    # Make a legend
    if plt_orig:
        plt.legend(('Data', 'Bootstrap'), loc='lower right')
    # Format the plot
    plt.ylabel('eCDF')
    plt.title('Bootstrap Method')
    if show:
        plt.show()

# Segmentation function
def my_segmentation(image, threshold='otsu', seg='below',
                    max_obj=1000, min_obj=250, plot=False):
    """
    Takes an imput image as an array and returns a labeled segmentation
    mask. Corrects for uneven illumination, performs a median filter,
    thesholds the image, then segments. The thresholding operation can
    be a specified integer value, but default uses otsu. Removes
    objects near the border and that are outside the object size range.
    Segmentation defaults to phase images, segmenting everything below
    the threshold. Can be changed to 'above' to segment above the
    threshold.
    """
    # Veryify inputs for threshold and segmentation
    if seg != 'below' and seg != 'above':
        raise RuntimeError("Segmentation can only be 'above' or 'below'")
    if threshold != 'otsu' and type(threshold) != int:
        raise RuntimeError("Threshold must be 'otsu' or an integer")

    # Perform a median filter to correct for hot pixels
    selem = skimage.morphology.square(3)
    image_filt = skimage.filters.median(image, selem)

    # Correct for uneven illumination
    im_blur = skimage.filters.gaussian(image_filt, 100.0)
    image_corrected = skimage.img_as_float(image_filt) - im_blur

    # Perform a Chambolle total variation filter to correct for dots
    image_tv = skimage.restoration.denoise_tv_chambolle(image_corrected,
                                                        weight=0.001)

    # Segmenting the image
    if threshold == 'otsu':
        threshold = skimage.filters.threshold_otsu(image_tv)
    if seg == 'below':
        img_bw = image_tv < threshold
    else:
        img_bw = image_tv > threshold

    # Clear border with 5 pixel buffer
    img_bw = skimage.segmentation.clear_border(img_bw, buffer_size=5)

    # Label the objects
    seg_lab = skimage.measure.label(img_bw, background=0)

    # Get the properties of each object
    props = skimage.measure.regionprops(seg_lab)
    im_filt = seg_lab > 0

    # Get rid of the objects outside our range
    for prop in props:
        if prop.area < min_obj or prop.area > max_obj:
            im_filt[seg_lab==prop.label] = 0

    # Relabel in image
    seg_lab = skimage.measure.label(im_filt, background=0)

    # Plot the image
    if plot:
        plt.close()
        with sns.axes_style('dark'):
            plt.imshow(seg_lab, cmap=plt.cm.Spectral_r)
        plt.show()
    return seg_lab
