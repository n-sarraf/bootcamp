import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)
sns.set_style('dark')

# Our image processing tools.
import skimage.filters
import skimage.io
import skimage.measure
import skimage.morphology
import skimage.segmentation

# Load an example phase image.
phase_im = skimage.io.imread('data/HG105_images/noLac_phase_0004.tif')

# Show the image.
plt.imshow(phase_im, cmap=plt.cm.viridis)


# Apply Gaussian blur to the image.
im_blur = skimage.filters.gaussian(phase_im, 50.0)

# Convert our phase image to a float.
phase_float = skimage.img_as_float(phase_im)
phase_sub = phase_float - im_blur

# Show original and subtracted image.
plt.figure()
plt.imshow(phase_float, cmap=plt.cm.viridis)
plt.title('original')

plt.figure()
plt.imshow(phase_sub, cmap=plt.cm.viridis)
plt.title('subtracted')

# Apply otsu thresholding.
thresh = skimage.filters.threshold_otsu(phase_sub)
seg = phase_sub < thresh

# Plot our segmentation.
plt.close('all')
plt.imshow(seg, cmap=plt.cm.Greys_r)

# Label them. [seg_lab labels objects from top left corner]
seg_lab, num_cells = skimage.measure.label(seg, return_num=True, background=0)
plt.close()
plt.imshow(seg_lab, cmap=plt.cm.Spectral_r)
