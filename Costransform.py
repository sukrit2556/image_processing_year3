import cv2
from matplotlib import pyplot as plt
import numpy as np

def process_spectrum(spectrum):
    mag = np.linalg.norm(spectrum, axis=2)
    mag /= mag.max()
    mag **= 1/4
    return mag

def low_pass_filter(r, mask):
    r = r
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r * r
    mask[mask_area] = 1
    fshift = dft_shift * mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    return img_back
    
    

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
mask_for_LO = zero
mask_for_HI = one

result1 = low_pass_filter(100, mask_for_LO)
result2 = low_pass_filter(1000, mask_for_LO)

fig = plt.figure(figsize = (2, 2))
ax1 = fig.add_subplot(2, 2, 1)
ax1.imshow(result1, cmap = 'gray')
ax1.title.set_text('low')
ax2 = fig.add_subplot(2, 2, 2)
ax2.imshow(result2, cmap = 'gray')
ax2.title.set_text('low')
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()