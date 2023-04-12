import cv2
import numpy as np

img = cv2.imread("darkImg.png")

#splitting color
b, g, r = cv2.split(img)
"""
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)
"""
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#c = 45
#red operation
c = 255/(np.log(1 + 255))
log_trans_red = c * np.log(1 + r)
log_trans_red = np.array(log_trans_red, dtype = np.uint8)
cv2.imshow("Red_after", log_trans_red)

#green operation
c = 255/(np.log(1 + 255))
log_trans_green = c * np.log(1 + g)
log_trans_green = np.array(log_trans_green, dtype = np.uint8)
cv2.imshow("Green_after", log_trans_green)

#blue operation
c = 255/(np.log(1 + 255))
log_trans_blue = c * np.log(1 + b)
log_trans_blue = np.array(log_trans_blue, dtype = np.uint8)
cv2.imshow("Blue_after", log_trans_blue)

#merge channel
zeros = np.zeros(img.shape[:2], dtype = "uint8")
zeros = cv2.merge([zeros, log_trans_red])
zeros = cv2.merge([zeros, log_trans_green])
zeros = cv2.merge([zeros, log_trans_blue])
cv2.imshow("mer", zeros)

#merge = np.dstack((log_trans_blue,log_trans_green,log_trans_red))

cv2.waitKey(0)

cv2.imwrite('test.png', zeros)