import cv2
import numpy as np
import skimage.morphology as morph

def getcontour(x):

    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((3, 3), np.uint8)

    # The first parameter is the original image,
    # kernel is the matrix with which image is
    # convolved and third parameter is the number
    # of iterations, which will determine how much
    # you want to dilate a given image.
    dil_img = cv2.dilate(x, kernel, iterations=1)

    # subtract the original image from the dilated one
    c = dil_img - x
    cv2.imshow('c', c)
    cv2.imwrite('c.png', c)
    cv2.waitKey(0)

    # thinned = morph.thin(c, 1)

    # cv2.imshow('thin', thinned.astype(np.uint8))
    # cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return c