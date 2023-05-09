import cv2
from angle_finder import findRotationAngle
from rotation import rotateImage
from getContour import getcontour
from lineSeparator import lineSeparator

# Load the input image
img = cv2.imread('text1.png', 0)
# cv2.imshow('img', img)

angle = findRotationAngle(img)

rot_image = rotateImage(img, angle)

lines = lineSeparator(rot_image)

for line in lines:
    cv2.imshow('line', line)

cv2.waitKey(0)
cv2.destroyAllWindows()

# letters = cv2.imread('f.png', 0)
# c = getcontour(letters)