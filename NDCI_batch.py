# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 02:03:37 2024

@author: Gonzalo Martínez Fornos
gmail:gmartinez@icm.csic.es
"""

from download_map  import download_map
from acolite_fun import acolite_fun
import os
from dateconverter import doytodate
#funcion que activa el ndci desde sentinel
def NDCI_batch(doy,root_dir)->float:
    
    download_dir                 = root_dir+"downloads/"
    date = doytodate(doy)
    response = download_map(date,download_dir,'ndci')
    if response == "ok":
        # Decompress and acolite
        print("Download ok  " + str(date))
        acolite_fun(root_dir)
        # Clear tmp files
        for f in os.listdir(download_dir):
            os.remove(os.path.join(download_dir, f))
        print("Process completed for  " + str(date))
    else:
        print("No satellite image for  " + str(date))