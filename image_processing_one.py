import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# For image processing
import skimage.io
import skimage.exposure
import skimage.morphology
import skimage.filters

# Load the images.
phase_im = skimage.io.imread('data/bsub_100x_phase.tif')
cfp_im = skimage.io.imread('data/bsub_100x_cfp.tif')

# Show the phase image.
# plt.imshow(phase_im, cmap=plt.cm.viridis)

# Plot the histogram of the phase image.
hist_phase, bins_phase = skimage.exposure.histogram(phase_im)
plt.plot(bins_phase, hist_phase)
plt.xlabel('pixel value')
plt.ylabel('count')

# Apply a threshold to our image.
thresh = 325
im_phase_thresh = phase_im < thresh

plt.close()

with sns.axes_style('dark'):
    plt.imshow(im_phase_thresh, cmap=plt.cm.Greys_r)

# Show the fluorescence image.
with sns.axes_style('dark'):
    plt.imshow(cfp_im, cmap=plt.cm.viridis)

# Slice out region with a hot pixel.
plt.close()
with sns.axes_style('dark'):
    plt.imshow(cfp_im[150:250, 450:550]/cfp_im.max(), cmap=plt.cm.viridis)


# Generate a structural element.
selem = skimage.morphology.square(3)
cfp_filt = skimage.filters.median(cfp_im, selem)

with sns.axes_style('dark'):
    plt.imshow(cfp_filt[150:250, 450:550] / cfp_im.max(), cmap=plt.cm.viridis)

# Look at the histogram of the median filtered image.
cfp_hist, cfp_bins = skimage.exposure.histogram(cfp_filt)
plt.close()
plt.plot(cfp_bins, cfp_hist)
plt.xlabel('pixel value')
plt.ylabel('counts')

# Threshold our fluourescence image
cfp_thresh = cfp_filt > 120
plt.close()
with sns.axes_style('dark'):
    plt.imshow(cfp_thresh, cmap=plt.cm.Greys_r)

plt.close()

# Apply an otsu threshold.
phase_thresh = skimage.filters.threshold_otsu(phase_im)
cfp_thresh = skimage.filters.threshold_otsu(cfp_filt)
phase_otsu = phase_im < phase_thresh
cfp_otsu = cfp_filt > cfp_thresh

with sns.axes_style('dark'):
    plt.figure()
    plt.imshow(phase_otsu, cmap=plt.cm.Greys_r)
    plt.title('phase otsu')

    plt.figure()
    plt.imshow(cfp_otsu, cmap=plt.cm.Greys_r)
    plt.title('cfp otsu')
