import cv2
import numpy as np

# Define the HSV color values
H, S, V = 255, 180, 135

# Convert to RGB color space
hsv_color = np.uint8([[[H, S, V]]])
rgb_color = cv2.cvtColor(hsv_color, cv2.COLOR_HSV2RGB)

# Extract the RGB values
R, G, B = rgb_color[0][0]

# Print the RGB values
print("R: ", R)
print("G: ", G)
print("B: ", B)
