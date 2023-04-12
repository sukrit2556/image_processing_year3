import cv2
import numpy as np

# Load the reference image and the image to be matched
ref_image = cv2.imread('tajmahal.jpg', cv2.IMREAD_GRAYSCALE)
input_image = cv2.imread('flood.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate the histograms of the reference image and the input image
ref_hist = cv2.calcHist([ref_image], [0], None, [256], [0, 256])
input_hist = cv2.calcHist([input_image], [0], None, [256], [0, 256])

# Normalize the histograms
ref_hist_norm = ref_hist / ref_image.size
input_hist_norm = input_hist / input_image.size

# Calculate the cumulative distribution functions (CDFs) of the histograms
ref_cdf = ref_hist_norm.cumsum()
input_cdf = input_hist_norm.cumsum()

# Create a lookup table to map the input pixel intensities to the matched values
lookup_table = np.zeros(256, dtype=np.uint8)
for i in range(256):
    j = 255
    while j >= 0 and input_cdf[i] <= ref_cdf[j]:
        j -= 1
    lookup_table[i] = j

# Apply the lookup table to the input image
matched_image = cv2.LUT(input_image, lookup_table)

# Display the input image, reference image, and matched image
cv2.imshow('Input Image', input_image)
cv2.imshow('Reference Image', ref_image)
cv2.imshow('Matched Image', matched_image)
cv2.imwrite('histmatch.jpg', matched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()