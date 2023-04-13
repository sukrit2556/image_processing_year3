import cv2
from matplotlib import pyplot as plt
import numpy as np


    

img = cv2.imread("zebra.jpeg", cv2.IMREAD_GRAYSCALE)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1])) #magnitude of real and imaginary

rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
zero = np.zeros((rows, cols, 2), np.uint8)
one = np.ones((rows, cols, 2), np.int8)


r = 100
mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r * r
mask[mask_area] = 1
fshift = dft_shift * mask
fshift_mask_mag = 2000 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

cv2.waitKey(0)
cv2.destroyAllWindows()