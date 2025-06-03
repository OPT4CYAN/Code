# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 14:17:05 2025

@author: gmart
"""
import os
os.chdir('C:/Users/gmart/Proyectos/opt4cyan_tmart/lib')
import glob
import numpy as np
import shutil
from pre_run import pre_run
from index_run import index_run
from water_batch import water_batch
from NDCI_batch import NDCI_batch
from plot_run import plot_run
from renombr import renombr
from ponderar import ponderar



dir_ini = "C:/Users/gmart/Proyectos/opt4cyan_tmart/"
web_dir            ="C:/Users/gmart/Proyectos/Web_Control_Doñana/"
site               = ['Lucio_del_Rey','Hondon_del_Burro','Fuente_del_Duque','Santa_Olalla']
input_dir          = dir_ini+ "input/"
output_dir         = dir_ini+ "output/"
temp_dir           = dir_ini+ "temp/"
sentinel_dir       = dir_ini+ "Sentinel/"
procesado          = dir_ini+ "datos_procesados/"
site               = ['Lucio_del_Rey','Hondon_del_Burro','Fuente_del_Duque','Santa_Olalla']
repro              = dir_ini+ "repro/"


doy_list=[2021181,2021186,2021201]
doy_list= np.array(doy_list)

doy= 2021181
NDCI_batch(doy,sentinel_dir)
print ("Ndci and water detection Complete "+str(doy))


doy= 2021186
NDCI_batch(doy,sentinel_dir)
print ("Ndci and water detection Complete "+str(doy))

doy= 2021201
NDCI_batch(doy,sentinel_dir)
print ("Ndci and water detection Complete "+str(doy))
