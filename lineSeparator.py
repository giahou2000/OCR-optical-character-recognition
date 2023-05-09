import cv2

def lineSeparator(image):

    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    vertical_projection = cv2.reduce(gray_img, 0, cv2.REDUCE_SUM)

    threshold = 0.5 * gray_img.shape[0] # Set a threshold to detect transitions
    positions = []
    for i in range(1, len(vertical_projection)):
        if vertical_projection[i-1] < threshold and vertical_projection[i] >= threshold:
            positions.append(i)
        elif vertical_projection[i-1] >= threshold and vertical_projection[i] < threshold:
            positions.append(i)

    lines = []
    for i in range(0, len(positions), 2):
        lines.append(gray_img[:, positions[i]:positions[i+1]])

    return lines