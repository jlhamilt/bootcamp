import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# For image processing
import skimage.io
import skimage.exposure
import skimage.morphology
import skimage.filters

# Load the images
phase_im = skimage.io.imread('data/bsub_100x_phase.tif')
cfp_im = skimage.io.imread('data/bsub_100x_cfp.tif')

# Show the phase image
plt.imshow(phase_im, cmap=plt.cm.viridis)

# Plot histogram of the phase image
plt.clf()
hist_phase, bins_phase = skimage.exposure.histogram(phase_im)
plt.plot(bins_phase, hist_phase)
plt.xlabel('pixel value')
plt.ylabel('count')

# Apply threshold to the image and plot it.
thresh = 275
im_phase_thresh = phase_im < thresh
plt.close()

with sns.axes_style('dark'):
    plt.imshow(im_phase_thresh, cmap=plt.cm.Greys_r)

with sns.axes_style('dark'):
    plt.imshow(cfp_im, cmap=plt.cm.viridis)

# Slice out revion with a hot pixel
plt.close()
with sns.axes_style('dark'):
    plt.imshow(cfp_im[150:250, 450:550]/cfp_im.max(), cmap=plt.cm.viridis)

# Generate a structural image and filter the image
selem = skimage.morphology.square(3)
cfp_filt = skimage.filters.median(cfp_im, selem)
with sns.axes_style('dark'):
    plt.imshow(cfp_filt[150:250, 450:550]/cfp_filt.max(), cmap=plt.cm.viridis)

# Let's look at the histogram of the median filtered image.
cfp_hist, cfp_bins = skimage.exposure.histogram(cfp_filt)
plt.close()
plt.plot(cfp_bins, cfp_hist)
plt.xlabel('pixel value')
plt.ylabel('counts')

# Threshold our fluorescence image.
cfp_thresh = cfp_filt > 120
plt.close()
with sns.axes_style('dark'):
    plt.imshow(cfp_thresh, cmap=plt.cm.Greys_r)

# Thresholding sucks by hand. Let's use otsu instead because it's a baller
phase_thresh = skimage.filters.threshold_otsu(phase_im)
cfp_thresh = skimage.filters.threshold_otsu(cfp_filt)
phase_otsu = phase_im < phase_thresh
cfp_otsu = cfp_filt > cfp_thresh

# Plot both on the same figure
with sns.axes_style('dark'):
    fig, ax = plt.subplots(1, 2, figsize=(8,6))

    ax[0].imshow(phase_otsu, cmap=plt.cm.viridis)
    ax[1].imshow(cfp_otsu, cmap=plt.cm.viridis)
