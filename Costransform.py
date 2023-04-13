import cv2
from matplotlib import pyplot as plt
import numpy as np

def process_spectrum(spectrum):
    mag = np.linalg.norm(spectrum, axis=2)
    mag /= mag.max()
    mag **= 1/1
    return mag

def low_pass_filter(radius):
    r = radius
    mask = np.zeros((rows, cols, 2), np.uint8)
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r * r
    mask[mask_area] = 1
    fshift = dft_shift * mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = process_spectrum(img_back)
    #img_back = cv2.magnitude(img_back[:, : 0], img_back[:, :, 1])
    return img_back
    
def high_pass_filter(radius):
    r = radius
    mask = np.ones((rows, cols, 2), np.uint8)
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r * r
    mask[mask_area] = 0
    fshift = dft_shift * mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = process_spectrum(img_back)
    #img_back = cv2.magnitude(img_back[:, : 0], img_back[:, :, 1])
    return img_back

img = cv2.imread("zebra.jpeg", cv2.IMREAD_GRAYSCALE)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1])) #magnitude of real and imaginary

rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]

result1 = low_pass_filter(100)
result2 = high_pass_filter(100)
result3 = high_pass_filter(low_pass_filter(100))
result4 = low_pass_filter(high_pass_filter(100))
cv2.imwrite('low_pass_only.png', 255*result1)
cv2.imwrite('high_pass_only.png', 255*result2)
cv2.imwrite('low_then_high.png', 255*result3)
cv2.imwrite('high_then_low.png', 255*result4)

fig = plt.figure(figsize = (2, 2))
ax1 = fig.add_subplot(2, 2, 1)
ax1.imshow(result1, cmap = 'gray')
ax1.title.set_text('Low-pass')
ax2 = fig.add_subplot(2, 2, 2)
ax2.imshow(result2, cmap = 'gray')
ax2.title.set_text('High-pass')
ax3 = fig.add_subplot(2, 2, 3)
ax3.imshow(result3, cmap = 'gray')
ax3.title.set_text('low then high')
ax4 = fig.add_subplot(2, 2, 4)
ax4.imshow(result4, cmap = 'gray')
ax4.title.set_text('high then low')
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()