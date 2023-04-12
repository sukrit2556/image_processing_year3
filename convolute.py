import cv2
import numpy as np

img = cv2.imread("zebra.jpeg")

kernel1 = np.array([[0, 1/6, 0], [1/6, 1/3, 1/6], [0, 1/6, 0]])
print(kernel1)
kernel2 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
kernel3 = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

filtered_image1 = cv2.filter2D(src=img, ddepth = -1, kernel = kernel1)
filtered_image2 = cv2.filter2D(src=img, ddepth = -1, kernel = kernel2)
filtered_image3 = cv2.filter2D(src=img, ddepth = -1, kernel = kernel3)

cv2.imshow("original", img)
cv2.imshow("result1", filtered_image1)
cv2.imshow("result2", filtered_image2)
cv2.imshow("result3", filtered_image3)

#cv2.imwrite("convo1.jpg", filtered_image1)
#cv2.imwrite("convo2.jpg", filtered_image2)
#cv2.imwrite("convo3.jpg", filtered_image3)
cv2.waitKey(0)
cv2.destroyAllWindows()