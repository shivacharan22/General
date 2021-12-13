import math
import os
import numpy as np
from PIL import Image

def mse(original, decrypted):
    Square = (original - decrypted) ** 2
    Mean_squared_Error = np.mean(Square)
    return Mean_squared_Error
