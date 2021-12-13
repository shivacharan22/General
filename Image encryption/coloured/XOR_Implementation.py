# XOR implementation for Colour Image
import sys
sys.path.append(r"D:\Coding\Image Encryption\utils")

import numpy as np
from PIL import Image
from psnr import psnr
from ncorr import normxcorr2D
from mse import mse

def encrypt(input_image, share_size):
    image = np.asarray(input_image)
    (row, column, depth) = image.shape
    #row -> height
    #column -> width
    #depth -> no of channels
    shares = np.random.randint(0, 256, size = (row, column, depth, share_size) )

    #print(len(shares))
    shares[:, : , :, -1] = image.copy()
    
    for i in range(0, share_size-1):
        shares[:,:,:,-1] = shares[:,:,:,-1] ^ shares[:,:,:,i]

    return shares, image

def decrypt(shares):
    (row, column, depth, share_size) = shares.shape
    shares_image = shares.copy()
    for i in range(share_size-1):
    	shares_image[:,:,:,-1] = shares_image[:,:,:,-1] ^ shares_image[:,:,:,i]

    final_output = shares_image[:,:,:,share_size-1]
    output_image = Image.fromarray(final_output.astype(np.uint8))
    return output_image, final_output


if __name__ == "__main__":
    
    print("Save input image as 'Input.png' in the same folder as this file\n")

    share_size = int(input("Input the number of random images you want to create : "))


    try:
        input_image = Image.open('Colored\Input.png')

    except FileNotFoundError:
    	print("Input file not found!")
    	exit(0)

    print("Image upload was successfull!")
    print("Input image size (in pixels) : ", input_image.size)   
    print("Number of shares image = ", share_size)

    shares, input_matrix = encrypt(input_image, share_size)
    
    # Converting noise to noise_image.png
    for ind in range(share_size):
        image = Image.fromarray(shares[:,:,:,ind].astype(np.uint8))
        name = "Colored\outputs\XOR_Share_" + str(ind+1) + ".png"
        image.save(name)

    output_image, output_matrix = decrypt(shares)

    output_image.save('Colored\outputs\Output_XOR.png')
    print("Image is saved 'Output_XOR.png' ...")
    
    print("Evaluation metrics : ")    
    print(f"PSNR value is {psnr(input_matrix, output_matrix)} dB")
    print(f"Mean NCORR value is {normxcorr2D(input_matrix, output_matrix)}")
    print(f"MSE value is {mse(input_matrix, output_matrix)}")