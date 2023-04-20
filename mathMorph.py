import cv2
import numpy as np

img = cv2.imread("bag.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv1 = hsv[:, :, 0]
hsv2 = hsv[:, :, 1]
hsv3 = hsv[:, :, 2]
cv2.imshow("result", hsv)
cv2.imshow("concate", (np.concatenate((hsv1, hsv2, hsv3), axis=1)))
cv2.waitKey(0)
cv2.destroyAllWindows()