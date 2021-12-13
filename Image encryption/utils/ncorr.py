## Adapted from: https://xcdskd.readthedocs.io/en/latest/cross_correlation/cross_correlation_coefficient.html
import numpy as np
import math
from PIL import Image

def normxcorr2D(input_image, output_image):
    # Converting to nparray of type float
    t = np.asarray(output_image, dtype=np.float64)
    t = t - np.mean(t)
    denomt = math.sqrt(np.sum(np.square(t)))
 
    i = np.asarray(input_image, dtype=np.float64)
    i = i - np.mean(i)
    denomi = math.sqrt(np.sum(np.square(i)))

    num_sum = np.multiply(i, t)

    numerator = np.sum(num_sum)

    nxcorr = 0

    if denomt != 0 and denomi != 0:
        nxcorr = numerator / (denomt * denomi)

    return nxcorr
