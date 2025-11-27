# -*- coding: utf-8 -*-
"""
@author:             Gonzalo M.F. 
Gonzalo Martínez-Fornos
gmartinez@icm.csic.es
Research institute:  ICM-CSIC 
Collaboration:       EBD-CSIC 
"""
import os
import glob
import numpy as np
dir_ini = "directory of the main folder /cyanobacteria_detector/"
os.chdir((dir_ini+'lib/'))
import chl_pcu_run as cp
import NDCI_run as ndci
import functions as fn
import read_trios as rt
import plot_run as pl
dirs               = {
    'input':dir_ini+ "input/",
    'output':dir_ini+ "output/",
    'tmp': dir_ini+ "tmp/",
    'sentinel': dir_ini+ "Sentinel/",
    'procesado': dir_ini+ "datos_procesados/",
    'acolite': dir_ini +"acolite_py_win"}

#open station.txt with the information
with open(dir_ini + "station.txt", "r") as f:
    lineas = [l.strip() for l in f.readlines()]
keys = lineas[0].split(';')
file = [dict(zip(keys, linea.split(';')))for linea in lineas[1:]][0]

#loading coordinates
#This section should be replaced with information about your stations and the radiometer codes. 
site                          = file['site']
site_latitude                      = file['lat']
site_longitude                     = file['lon']
user                               =  file['user']
passw                              = file['password']

#We add information about the sensor codes; these depend on the station.
so                  = {'ed': file['ed'], 'li':file['li'], 'lt': file['lt'] }
# add for site

#basic renaming function to avoid file errors
fn.renombr(dirs['input'],site)


#Now we call a function that does pre-processing. There are two processors:
    #1 - We separate the .dat files by sensor measurements and time in the temp folder.
    #2 - We generate RRS information by combining LT, LI, and ED sensors.
    
repro_data                         = glob.glob(dirs['input']+ "*.dat") 
lat                                = site_latitude
lon                                = site_longitude
for repro in repro_data:
    rt.pre_run(repro,dirs['tmp'])
    rt.rrs_run(dirs['output']+site+ "_rrs.dat",so,dirs['tmp'],lat,lon)
    #delete tmp   
    for f in os.listdir(dirs['tmp']):
        os.remove(os.path.join(dirs['tmp'], f)) 
    print("Arch ----> ......   Complete")
    
    if os.path.exists(repro):
        os.remove(repro)
        print(f"Archivo '{os.path.basename(repro)}' \n DELETED")
    
#Up to this point, we have saved all the daily RRS data.
#Now we will process the RRS for indexing.

#######index conversion
ID=cp.index_run(dirs['output']+site)
print("Index Complete "+site+" Station")
## normalize and create pcu and chl index 
cp.normalize_fun(dirs['output']+site)
# pcu and chl index document 
cp.pcu_chl(dirs['output']+site)
#procesing the Acolite program for detect the NDCI
doy=np.unique(ID.astype(int))  
ndci.NDCI_run(doy,dirs['sentinel'],dirs['output'],dirs['acolite'],user,passw ,lat,lon)
print ("Ndci and water detection Complete "+str(doy))
#plots
pl.plot_run(dirs['output'], site)




      
