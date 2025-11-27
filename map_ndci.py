# -*- coding: utf-8 -*-
"""
@author:             Gonzalo M.F. 
Gonzalo Martínez-Fornos
gmartinez@icm.csic.es
Research institute:  ICM-CSIC 
Collaboration:       EBD-CSIC 
"""
import numpy as np
import glob
from skimage import color
from PIL import Image
import matplotlib.pyplot as plt
import os
#ndci color map
def map_ndci (ndci_array:float,destination_folder:str,name:str,origin_folder)->float:
   
    
    # Crear una máscara para los valores NaN en la matriz NDCI
    mask = np.isnan(ndci_array)
    
    # Create a mask for NaN values ​​in the NDCI array
    ndci_array_clean = np.ma.masked_array(ndci_array, mask)
    
    
    # Open the TIFF image
    dir_rgb= glob.glob(origin_folder + "/"+ "*rhos.tif")
    dir_rgb= dir_rgb[0]
    dir_rgb= dir_rgb.replace("\\","/")
    rgb_image = Image.open(dir_rgb)
    
    
    # Convert RGB image to grayscale
    gray_image = color.rgb2gray(rgb_image)
    
    os.chdir(destination_folder)
    fig                      = plt.figure(figsize=(15,10))
    plt.imshow(gray_image, cmap='gray',alpha=0.5)
    plt.imshow(ndci_array_clean, cmap='jet')
    plt.colorbar()
    plt.axis('off')
    fig.savefig(name[0:19] + "Ndci", dpi=300)
