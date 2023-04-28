import cv2
import numpy as np
from scipy.signal import find_peaks

# Load the input image
img = cv2.imread('text1.png', 0)
# cv2.imshow('img', img)

# Blur the input image
blurred_img = cv2.blur(img, (15, 15), cv2.BORDER_DEFAULT) 
cv2.imshow('blurred_img', blurred_img)

# # Apply Canny edge detection to the blurred image
# edges = cv2.Canny(blurred_img, 50, 150, apertureSize=3)

# # Compute the DFT of the edge image along the y-axis
# dft = np.fft.fft2(edges, axes=(0,))

# # Shift the zero frequency component to the center of the spectrum
# dft_shift = np.fft.fftshift(dft)

# # Compute the magnitude of the complex DFT coefficients
# magnitude_spectrum = np.abs(dft_shift)

# # Find the peaks in the magnitude spectrum
# peaks, _ = find_peaks(magnitude_spectrum[:, 0], distance=100, prominence=500)

# # Compute the angle of rotation from the first peak
# angle = np.arctan2(peaks[0], img.shape[1]//2)

# # Rotate the input image by the computed angle
# rotated_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
# M = cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), np.degrees(angle), 1)
# rotated_img = cv2.warpAffine(rotated_img, M, (img.shape[1], img.shape[0]))

# # Display the input and output images
# cv2.imshow('Input Image', img)
# cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
