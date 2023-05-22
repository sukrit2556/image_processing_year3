import cv2
from matplotlib import pyplot as plt
import numpy as np

#change
def process_spectrum(spectrum):
    mag = np.linalg.norm(spectrum, axis=2)
    mag /= mag.max()
    mag **= 1/1
    return mag

img = cv2.imread("zebra.bmp", cv2.IMREAD_GRAYSCALE)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1])) #magnitude of real and imaginary

rows, cols = img.shape
print(img.shape)
crow, ccol = int(rows/2), int(cols/2)
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
zero = np.zeros((rows, cols, 2), np.uint8)
mask = [zero, zero, zero]
radius = [0.1, 0.2, 0.3]
fshift = [zero, zero, zero]
fshift_mask_mag = [zero, zero, zero]
f_ishift = [zero, zero, zero]
img_back = [zero, zero, zero]
#img_processed = [zero, zero, zero]

for i in range (0,3):  
    r = int(radius[i] * rows)
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r * r
    mask[i][mask_area] = 1
    fshift[i] = dft_shift * mask[i]
    fshift_mask_mag[i] = 2000 * np.log(cv2.magnitude(fshift[i][:, :, 0], fshift[i][:, :, 1]))

    f_ishift[i] = np.fft.ifftshift(fshift[i])
    img_back[i] = cv2.idft(f_ishift[i])
    #img_processed[i] = process_spectrum(img_back[i])
    img_back[i] = cv2.magnitude(img_back[i][:, :, 0], img_back[i][:, :, 1])
    #cv2.imwrite('DFTTrans'+str(i)+'.jpg', 255*img_processed)

fig = plt.figure(figsize = (4, 4))
ax1 = fig.add_subplot(2, 4, 1)
ax1.imshow(img, cmap = 'gray')
ax1.title.set_text('Original Image')

ax2 = fig.add_subplot(2, 4, 2)
ax2.imshow(magnitude_spectrum, cmap = 'gray')
ax2.title.set_text('FFT of image')

ax3 = fig.add_subplot(2, 4, 3)
ax3.imshow(fshift_mask_mag[0], cmap = 'gray')
ax3.title.set_text('FFT + Mask r = 0.1 * cols')

ax4 = fig.add_subplot(2, 4, 4)
ax4.imshow(img_back[0], cmap = 'gray')
ax4.title.set_text('result r = 0.1')

ax5 = fig.add_subplot(2, 4, 5)
ax5.imshow(fshift_mask_mag[1], cmap = 'gray')
ax5.title.set_text('FFT + Mask r = 0.2 * cols')

ax6 = fig.add_subplot(2, 4, 6)
ax6.imshow(img_back[1], cmap = 'gray')
ax6.title.set_text('result r = 0.2')

ax7 = fig.add_subplot(2, 4, 7)
ax7.imshow(fshift_mask_mag[2], cmap = 'gray')
ax7.title.set_text('FFT + Mask r = 0.3 * cols')

ax8 = fig.add_subplot(2, 4, 8)
ax8.imshow(img_back[2], cmap = 'gray')
ax8.title.set_text('result r = 0.3')




plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()