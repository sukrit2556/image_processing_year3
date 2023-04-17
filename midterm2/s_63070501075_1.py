import cv2
import numpy as np

# Load the image
img = cv2.imread('test1.jpg',1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]
hsv_split = np.concatenate((h,s,v), axis=1)
cv2.imshow("hsv", hsv_split)

kernel = np.ones((3,3),np.uint8)
lower_skin = np.array([0,20,70], dtype=np.uint8)
upper_skin = np.array([20,255,255], dtype=np.uint8)

ret, min_sat = cv2.threshold(s,40,255, cv2.THRESH_BINARY)
cv2.imshow("min sat", min_sat)

ret, max_hue = cv2.threshold(h,15,255, cv2.THRESH_BINARY_INV)
cv2.imshow("max hue", max_hue)

before_final = cv2.bitwise_and(min_sat, max_hue)
cv2.imshow("before final", before_final)

before_final = cv2.inRange(hsv, lower_skin, upper_skin)
before_final = cv2.erode(before_final, kernel, iterations=1)

# Display the result
cv2.imshow('Skin detection', before_final)
cv2.waitKey(0)
cv2.destroyAllWindows()
