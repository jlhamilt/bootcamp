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
im_blur = skimage.filters.gaussian(phase_im, 100.0)
plt.imshow(im_blur, cmap=plt.cm.viridis)

# Subtract the background. Blurred image is a float so must convert
phase_float = skimage.img_as_float(phase_im)
phase_sub = phase_float - im_blur

# Plot both to see the difference
plt.close('all')
plt.figure()
plt.imshow(phase_float, cmap=plt.cm.viridis)
plt.title('Original')
plt.show()

plt.figure()
plt.imshow(phase_sub, cmap=plt.cm.viridis)
plt.title('Subtracted Image')
plt.show()

# Segment the image using otsu
thresh = skimage.filters.threshold_otsu(phase_sub)
segmented = phase_sub < thresh

plt.close('all')
plt.imshow(segmented, cmap=plt.cm.Greys_r)
plt.show()

# Label our cells!
seg_lab, num_cells = skimage.measure.label(segmented, return_num=True, background=0)
plt.close()
plt.imshow(seg_lab, cmap=plt.cm.Spectral_r)
plt.show()

# Compute the region properties and extract the area of each object.
ip_dis = 0.063 # microns per pixel
props = skimage.measure.regionprops(seg_lab)

# Get the areas as an array
areas = np.array([prop.area for prop in props])
cutoff = 300

# Copy the original to a binary mask
im_cells = np.copy(seg_lab) > 0

# Erase the small objects
for i, _ in enumerate(areas):
    if areas[i] < cutoff:
        im_cells[seg_lab==props[i].label] = 0

area_filt_lab = skimage.measure.label(im_cells)
plt. figure()
plt.imshow(area_filt_lab, cmap=plt.cm.Spectral_r)
plt.show()
