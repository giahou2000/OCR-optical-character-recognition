import cv2
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

def findRotationAngle(img):

    angle = 0

    # Blur the input image
    blurred_img = cv2.blur(img, (15, 15), cv2.BORDER_DEFAULT) 
    cv2.imshow('blurred_img', blurred_img)

    # Compute the discrete Fourier Transform of the image
    fourier = cv2.dft(np.float32(blurred_img), flags=cv2.DFT_COMPLEX_OUTPUT)
    
    # Shift the zero-frequency component to the center of the spectrum
    fourier_shift = np.fft.fftshift(fourier)

    # calculate the magnitude of the Fourier Transform
    magnitude = 20*np.log(cv2.magnitude(fourier_shift[:,:,0],fourier_shift[:,:,1]))
    
    # Scale the magnitude for display
    magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)

    # Display the magnitude of the Fourier Transform
    cv2.imshow('Fourier Transform', magnitude)



    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return angle
