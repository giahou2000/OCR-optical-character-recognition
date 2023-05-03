import cv2
from angle_finder import findRotationAngle
from rotation import rotateImage

# Load the input image
img = cv2.imread('text1.png', 0)
cv2.imshow('img', img)

angle = findRotationAngle(img)

rot_image = rotateImage(img, angle)