import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import imutils

def findRotationAngle(img):

    angle = 0

    # Blur the input image
    blurred_img = cv2.blur(img, (18, 18), cv2.BORDER_DEFAULT) 
    # cv2.imshow('blurred_img', blurred_img)

    # Compute the 2D Fourier Transform of the input image
    fourier = np.fft.fft2(blurred_img)

    # Shift the zero frequency component to the center of the spectrum
    fourier_shifted = np.fft.fftshift(fourier)

    # Compute the magnitude of the spectrum
    magnitude_spectrum = 20 * np.log(np.abs(fourier_shifted))
    M, N = magnitude_spectrum.shape
    # find the center of the DFT
    cx = M // 2
    cy = N // 2
    # delete the dc component
    magnitude_spectrum[cx, cy] = 0

    # Find the maximum frequency of change in the magnitude spectrum
    max_freq = np.argmax(magnitude_spectrum)

    # Compute the row and column indices of the maximum frequency of change
    max_row, max_col = np.unravel_index(max_freq, magnitude_spectrum.shape)
    print("The max frequency is spotted at")
    print(max_row, max_col)
    print("The magnitude has a shape of")
    print(magnitude_spectrum.shape)

    # Display the magnitude of the Fourier Transform
    # cv2.imshow('Magnitude Spectrum', magnitude_spectrum.astype(np.uint8))

    # Display the magnitude of the Fourier Transform along with the image
    plt.subplot(121), plt.imshow(blurred_img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

    # Make a 3D plot of the magnitude of the spectrum
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

    # compute the center of the magnitude of the spectrum
    center = [int(magnitude_spectrum.shape[0]/2), int(magnitude_spectrum.shape[1]/2)]
    print("center is")
    print(center)

    # compute the angle
    angle = np.arctan2(max_col - center[1], max_row - center[0])
    print(angle)

    # test some angles
    angle_test_list = range(int(angle) - 5, int(angle) + 6)
    projections = []
    for i in angle_test_list:
        rot = imutils.rotate(img, angle=i)
        # Calculate the vertical projection of the luminance
        projection = np.sum(rot, axis=0)
        # Normalize the projection to the range [0, 1]
        projections.append(projection.astype(float) / np.max(projection))
    # Plot the projections
    fig, axs = plt.subplots(3, 4)
    axs[0, 0].plot(projections[0])
    axs[0, 0].set_title('-5 degrees')
    axs[0, 1].plot(projections[1])
    axs[0, 1].set_title('Axis [0, 1]')
    axs[0, 2].plot(projections[2])
    axs[0, 2].set_title('Axis [0, 2]')
    axs[0, 3].plot(projections[3])
    axs[0, 3].set_title('Axis [0, 3]')
    axs[1, 0].plot(projections[4])
    axs[1, 0].set_title('Axis [1, 0]')
    axs[1, 1].plot(projections[5])
    axs[1, 1].set_title('Axis [1, 1]')
    axs[1, 2].plot(projections[6])
    axs[1, 2].set_title('Axis [1, 2]')
    axs[1, 3].plot(projections[7])
    axs[1, 3].set_title('Axis [1, 3]')
    axs[2, 0].plot(projections[8])
    axs[2, 0].set_title('Axis [2, 0]')
    axs[2, 1].plot(projections[9])
    axs[2, 1].set_title('Axis [2, 1]')
    axs[2, 2].plot(projections[10])
    axs[2, 2].set_title('Axis [2, 2]')
    plt.show()

    # detect the biggest changes in projections
    means = []
    for i in range(11):
        proj = [x for x in projections[i] if x != 1] # throw away the values that are equal to 1, because we do not need them and they give a wrong result
        # Compute the differences between consecutive numbers
        diffs = [abs(proj[j+1] - proj[j]) for j in range(len(proj)-1)]
        # Compute the average difference and save it
        avg_diff = sum(diffs) / len(diffs)
        means.append(avg_diff)
    
    print("The computed means of consecutive differences are:")
    print(means)

    print("The index we're looking for is:")
    max_index = means.index(max(means))
    print(max_index)
    print("The angle we're looking for is:")
    angle = angle_test_list[max_index]
    print(angle)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return angle
