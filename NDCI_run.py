# -*- coding: utf-8 -*-
"""
@author:             Gonzalo M.F. 
Gonzalo Martínez-Fornos
gmartinez@icm.csic.es
Research institute:  ICM-CSIC 
Collaboration:       EBD-CSIC 
"""

from download_map  import download_map
from acolite_fun import acolite_fun
import functions as fn
import numpy as np
import os
#function that activates the ndci from sentinel
def NDCI_run(doy,root_dir, output_dir, acolite_dir,user,passw,lat,lon)->float:
    download_dir                 = root_dir+"downloads/"
    ###We open the sentinel file if it exists and read the latest date we have.
    #If there are new dates processed, we continue with the analysis.
    pre_date                     = open(output_dir + "sentinel_ndci.dat", 'r')
    lines                        = pre_date.readlines()
    linelist                     = [line.strip().split(";") for line in lines]
    if len(linelist)==1:
        date_sentinel            = 0
    else:
        date_sentinel                = np.nanmax(np.unique(np.array(linelist)[1:,0]).astype(int))
    if np.nanmax(doy) > date_sentinel: 
        doy_max                  = np.nanmax(doy)
        date                     = doy-date_sentinel
        date                     = [n for n in date if n > 0]
        idx = min(range(len(date)), key=lambda i: abs(date[i]))
        date                     = doy[idx]
        fech_range               = list(range(date,doy_max,1))
        for i in fech_range:
            date_tmp             = fn.doy_to_date(i)
            response = download_map(date_tmp,download_dir, user,passw,lat,lon)
            print(date_tmp+"         No salellite data")
            
            if response == "ok":
                # Decompress and acolyte
                print("Download ok  " + str(date))
                #### hacemos presettings para acolite
                fn.settings_file(root_dir,acolite_dir)
                acolite_fun(acolite_dir,root_dir,lat,lon)
                # Clear tmp files
                for f in os.listdir(download_dir):
                    os.remove(os.path.join(download_dir, f))
                print("Process completed for  " + str(date))
            else:
                print("No satellite image for  " + str(date))