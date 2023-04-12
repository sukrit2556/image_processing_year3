import cv2
import numpy as np

# Open the image.
img = cv2.imread('darkImg.png')
cv2.imshow('original', img)
H = img.shape[0]
W = img.shape[1]
print(str(H) + str(W))
# Trying 4 gamma values.
for gamma in [0.1, 0.5, 1.2, 2.2]:
	
	# Apply gamma correction.
	gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
	cv2.putText(img=gamma_corrected, text='gamma ' + str(gamma) , org=(200, 40), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 0, 255),thickness=2)
	# Save edited images.
	cv2.imwrite('gamma_transformed'+str(gamma)+'.jpg', gamma_corrected)
cv2.waitKey(0)
cv2.destroyAllWindows()
