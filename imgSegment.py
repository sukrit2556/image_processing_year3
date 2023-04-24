import cv2
import numpy as np

img = cv2.imread("brain.png",0)



cv2.imshow("original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()