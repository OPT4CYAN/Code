# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 02:03:37 2024

@author: Gonzalo Martínez Fornos
gmail:gmartinez@icm.csic.es
"""
#Suavizado de index for plots
import numpy as np
#filtro sutil de los datos para eliminar el ruido entre medidas
def Smoo_filter (index:float,n:int)->float:
    index_                      = np.zeros((0,))
    # n this number is for the amount of surrounding data it takes to smooth
    for i in range(len(index)):
        if i < n:
            y                   = np.mean(index[i:i+(n+1)])
        elif i >= n and i != len(index) - n:
            y                   = np.mean(index[i-n:i+(n+1)])
        else:
            y                   = np.mean(index[i-n:len(index)])
        
        index_                  = np.append(index_, y)
    
    return index_