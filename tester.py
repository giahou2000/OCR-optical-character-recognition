import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 2D numpy array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create a meshgrid from the array indices
x, y = np.meshgrid(range(arr2d.shape[0]), range(arr2d.shape[1]))

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface with x, y, and z values
ax.plot_surface(x, y, arr2d)
print(arr2d)

# Set the axis labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Show the plot
plt.show()
