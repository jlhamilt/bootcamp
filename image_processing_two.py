import numpy as np

# Our image processing tools
import skimage.filters
import skimage.io
import skimage.measure
import skimage.morphology
import skimage.segmentation

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)
sns.set_style('dark')

# Load an example phase image.
phase_im = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')

# Show the image
plt.imshow(phase_im, cmap=plt.cm.viridis)
# plt.show()

# The image has uneven illumination :(
# Let's apply a gaussian blur with a large radius to see illumination
im_blur = skimage.filters.gaussian(phase_im, 50.0)
plt.imshow(im_blur, cmap=plt.cm.viridis)
