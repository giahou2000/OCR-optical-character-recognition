import cv2
import imutils

def rotateImage(x, angle):
    y = imutils.rotate(x, angle=angle)
    cv2.imshow('rotated image', y)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return y