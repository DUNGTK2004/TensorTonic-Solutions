import numpy as np
def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    image = np.asarray(image, dtype=int)
    histogram = [0 for i in range(256)]
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            histogram[image[i][j]] += 1

    return list(histogram)