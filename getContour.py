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
    contour_img = dil_img - x
    _, contour_img = cv2.threshold(contour_img, 125, 255, cv2.THRESH_BINARY)
    cv2.imshow('contour_img', contour_img)
    # cv2.imwrite('f-contour.png', contour_img)
    cv2.waitKey(0)

    # thinned = morph.thin(c, 1)
    # skeleton = morph.skeletonize(c)

    # cv2.imshow('thin', thinned.astype(np.uint8))
    # cv2.imshow('skeleton', skeleton.astype(np.uint8))
    # cv2.waitKey(0)
    cv2.destroyAllWindows()

    # find and store the contour
    contours, _ = cv2.findContours(contour_img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    M, N =  contour_img.shape
    img = np.ones((M, N, 3))
    cv2.drawContours(img, contours, -1, (0, 255, 0), 1)

    cv2.imshow("Contour", img)
    # cv2.imwrite('f-contour-green.png', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return contours