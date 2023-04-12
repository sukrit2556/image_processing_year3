# import Opencv
import cv2

# import Numpy
import numpy as np

# read a image using imread
img = cv2.imread('darkImg.png')

# creating a Histograms Equalization
# of a image using cv2.equalizeHist()
R, G, B = cv2.split(img)

output1_R = cv2.equalizeHist(R)
output1_G = cv2.equalizeHist(G)
output1_B = cv2.equalizeHist(B)

equ = cv2.merge((output1_R, output1_G, output1_B))

# stacking images side-by-side
res = np.hstack((img, equ))

# show image input vs output
cv2.imshow("after", equ)

cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite("dark_eq_after.png", equ)
