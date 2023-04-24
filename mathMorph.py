import cv2
import numpy as np
# Load image
img = cv2.imread("bag.png", 0)

# Apply thresholding
ret, thresh = cv2.threshold(img, 90, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3,3), np.uint8)
thresh = cv2.dilate(thresh, kernel, iterations=1)

num_labels, labels = cv2.connectedComponents(thresh)

img_labeled = cv2.applyColorMap(labels.astype(np.uint8)*10, cv2.COLORMAP_JET)

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Thresholded Image", thresh)
cv2.imshow("Labeled Regions", img_labeled)
cv2.waitKey(0)
cv2.destroyAllWindows()
