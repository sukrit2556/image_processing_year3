import numpy as np
import cv2

# Load image
img = cv2.imread('zebra.jpeg', 0)

# Perform DFT
dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)

# Define a circular low pass filter
rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)
mask = np.zeros((rows, cols), np.uint8)
r = int(0.1*cols)
color = (255, 255, 255)
cv2.circle(mask, (ccol, crow), r, color, -1)

# Apply the filter to the frequency domain representation of the image
dft_filtered = dft_shift * mask
cv2.imshow("filtered", dft_filtered)

result = np.zeros_like(dft_shift)

# Invert the filtered DFT to obtain the filtered image
idft_shift = np.fft.ifftshift(dft_filtered)
img_back = np.fft.ifft2(idft_shift)
img_filtered = np.abs(img_back)

# Display original and filtered images
#cv2.imshow('Original', img)
cv2.imshow('Filtered', img_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
