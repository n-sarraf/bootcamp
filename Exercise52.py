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
fitc_otsu = [1,]*8
fitc_hist = [1,]*8
fitc_bins = [1,]*8
phase_hist = [1,]*8
phase_bins = [1,]*8

for i in range(0,8):
    j = str(i)

    # Load data
    im_phase[i] = skimage.io.imread('data/HG105_images/noLac_phase_000' + j + '.tif')
    im_fitc[i] = skimage.io.imread('data/HG105_images/noLac_fitc_000' + j + '.tif')

    # Apply Gaussian blur to the image.
    im_blur[i] = skimage.filters.gaussian(im_phase[i], 50.0)

    # Convert our phase image to a float.
    phase_float[i] = skimage.img_as_float(im_phase[i])
    phase_sub[i] = phase_float[i] - im_blur[i]

    # Perform segmentation on phase image files.
    thresh = skimage.filters.threshold_otsu(phase_sub[i])
    seg_im[i] = phase_sub[i] < thresh

    # Perform fluorescence extraction on fitc image files.
    fitc_thresh = skimage.filters.threshold_otsu(im_fitc[i])
    fitc_otsu[i] = im_fitc[i] > fitc_thresh

    # Plot our segmentation and fluorescence extraction.
    plt.figure(i)

    plt.subplot(231)
    plt.imshow(im_phase[i], cmap=plt.cm.viridis)
    plt.title('Phase ' + str(i+1))

    plt.subplot(232)
    plt.imshow(phase_sub[i], cmap=plt.cm.viridis)
    plt.title('Subtracted Ph ' + str(i+1))

    plt.subplot(233)
    plt.imshow(seg_im[i], cmap=plt.cm.Greys_r)
    plt.title('Segmented Ph ' + str(i+1))

    plt.subplot(234)
    plt.imshow(im_fitc[i], cmap=plt.cm.viridis)
    plt.title('FITC ' + str(i+1))

    plt.subplot(235)
    plt.imshow(fitc_otsu[i], cmap=plt.cm.Greys_r)
    plt.title('Extracted F ' + str(i+1))

    plt.subplot(236)
    fitc_hist[i], fitc_bins[i] = skimage.exposure.histogram(im_fitc[i])
    plt.plot(fitc_bins[i], fitc_hist[i])
    plt.title('Histogram')
    plt.xlabel('pixel value')
    plt.ylabel('counts')

    plt.show()
