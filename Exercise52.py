import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)
sns.set_style('dark')

# Our image processing tools.
import skimage.filters
import skimage.io
import skimage.measure
import skimage.morphology
import skimage.segmentation

im_phase = [1,]*8
im_fitc = [1,]*8
im_blur = [1,]*8
phase_float = [1,]*8
phase_sub = [1,]*8
seg_im = [1,]*8

# Load data
for i in range(0,8):
    j = str(i)
    im_phase[i] = skimage.io.imread('data/HG105_images/noLac_phase_000' + j + '.tif')
    im_fitc[i] = skimage.io.imread('data/HG105_images/noLac_fitc_000' + j + '.tif')

    # Apply Gaussian blur to the image.
    im_blur[i] = skimage.filters.gaussian(im_phase[i], 50.0)

    # Convert our phase image to a float.
    phase_float[i] = skimage.img_as_float(im_phase[i])
    phase_sub[i] = phase_float[i] - im_blur[i]

    # Perform segmentation on image files.
    thresh = skimage.filters.threshold_otsu(phase_sub[i])
    seg_im[i] = phase_sub[i] < thresh

    # Plot our segmentation.
    fig, ax = plt.subplots(1, 3)
    ax[0].imshow(im_phase[i], cmap=plt.cm.viridis)
    ax[1].imshow(phase_sub[i], cmap=plt.cm.viridis)
    ax[2].imshow(seg_im[i], cmap=plt.cm.Greys_r)
    ax[0].set_title('Original ' + str(i+1))
    ax[1].set_title('Subtracted ' + str(i+1))
    ax[2].set_title('Segmented ' + str(i+1))
    plt.show()
