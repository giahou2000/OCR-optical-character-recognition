import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def findRotationAngle(img):

    angle = 0

    # Blur the input image
    blurred_img = cv2.blur(img, (18, 18), cv2.BORDER_DEFAULT) 
    cv2.imshow('blurred_img', blurred_img)



    # Compute the 2D Fourier Transform of the input image
    fourier = np.fft.fft2(blurred_img)

    # Shift the zero frequency component to the center of the spectrum
    fourier_shifted = np.fft.fftshift(fourier)

    # Compute the magnitude of the spectrum
    magnitude_spectrum = 20 * np.log(np.abs(fourier_shifted))

    # Find the maximum frequency of change in the magnitude spectrum
    max_freq = np.argmax(magnitude_spectrum)

    # Compute the row and column indices of the maximum frequency of change
    max_row, max_col = np.unravel_index(max_freq, fourier_shifted.shape)
    print(max_row, max_col)

    # Display the magnitude of the Fourier Transform
    cv2.imshow('Magnitude Spectrum', magnitude_spectrum.astype(np.uint8))

    plt.subplot(121), plt.imshow(blurred_img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return angle
