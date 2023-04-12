
import cv2
import numpy as np
   
# Read an image
image = cv2.imread('brightImg.png')
   
# Apply log transformation method
c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(image + 1))
   
# Specify the data type so that
# float value will be converted to int
log_image = np.array(log_image, dtype = np.uint8)
   
# Display both images

cv2.imshow("log_darkImg", log_image)
cv2.waitKey(0)
#cv2.imwrite("after_lightImg.png", log_image)