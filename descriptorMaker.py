import numpy as np
import cmath

def descriptorMaker(contour):
    complex_array = []
    for i in range(len(contour)):
        for coord in contour:
            complex_array.append(cmath.complex(coord[0], coord[1]))
    fourier = np.fft.fft(complex_array)
    descriptor = np.abs(fourier)
    descriptor = descriptor[1:]
    return descriptor