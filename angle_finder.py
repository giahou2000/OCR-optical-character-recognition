import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
    print("The max frequency is spotted at")
    print(max_row, max_col)
    print("The magnitude has a shape of")
    print(magnitude_spectrum.shape)

    # Display the magnitude of the Fourier Transform
    cv2.imshow('Magnitude Spectrum', magnitude_spectrum.astype(np.uint8))

    # Display the magnitude of the Fourier Transform along with the image
    plt.subplot(121), plt.imshow(blurred_img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

    # Make a 3D plot of the magnitude
    # Create a meshgrid from the array indices
    y, x = np.meshgrid(range(magnitude_spectrum.shape[0]), range(magnitude_spectrum.shape[1]))
    # Create a figure and a 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Plot the surface with x, y, and z values
    ax.plot_surface(x, y, magnitude_spectrum.T)
    # Set the axis labels
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    # Show the plot
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return angle
