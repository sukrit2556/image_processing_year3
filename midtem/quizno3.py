
import cv2
import numpy as np
   
# Read an image
image8 = cv2.imread('lifting_gray.bmp')
cv2.imshow("example", image8)
print(image8.depth())