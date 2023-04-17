import numpy as np

# Define the RGB color values
R, G, B = 248, 142, 129

# Convert to YCrCb color space
Y = 0.299*R + 0.587*G + 0.114*B
Cr = 128 + 0.713*(R-Y)
Cb = 128 + 0.564*(B-Y)

# Round the values to integers
Y = int(Y)
Cr = int(Cr)
Cb = int(Cb)

# Print the YCrCb values
print("Y: ", Y)
print("Cr: ", Cr)
print("Cb: ", Cb)
