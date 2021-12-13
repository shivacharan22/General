## Adapted from: https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio
import math
import os
import numpy as np
from PIL import Image

def psnr(original, decrypted):
    mse = np.mean((original - decrypted) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    PSNR = 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
    return PSNR