# -*- coding: utf-8 -*-
"""
@author:             Gonzalo M.F. 
Gonzalo Martínez-Fornos
gmartinez@icm.csic.es
Research institute:  ICM-CSIC 
Collaboration:       EBD-CSIC 
"""
import netCDF4
import numpy as np
from map_ndci import map_ndci

def ndci_generator(dir_nc:str,destination_folder:str,name:str,origin_folder:str,lat,lon)->float:
    
    # Open the NetCDF file in read mode
    dataset = netCDF4.Dataset(dir_nc, "r")
    
    # Get a list of the variables available in the file
    variables = dataset.variables
    lon_aco= dataset.variables["lon"]
    lat_aco= dataset.variables["lat"]
    ndci= dataset.variables["ndci"]
    
    # Access the data of the variable
    datos_lon = lon_aco[:]
    datos_lat = lat_aco[:]
    datos_ndci= ndci[:]
    dataset.close()
    
    # Create NDCI image with respect to latitude and longitude
    # Convert matrices to arrays
    lat_array = np.array(datos_lat)
    lon_array = np.array(datos_lon)
    ndci_array = np.array(datos_ndci)
    
    map_ndci (ndci_array,destination_folder,name,origin_folder)
    
    
    ##############################################################
    
    # Calculating distances
    station = np.sqrt((lat_array - float(lat)) ** 2 + (lon_array - float(lon)) ** 2)
    
    # Create a mask to identify nan in ndci_array
    mask = np.isnan(ndci_array)
    
    # Apply the mask
    ndci_array_mask = ndci_array[~mask]
    lat_array_mask = lat_array[~mask]
    lon_array_mask = lon_array[~mask]
    
    #  new matrix without the NaN values
    dist_station=station[~mask]

    # Obtain values ​​from the 4 seasons
    station_idx = np.unravel_index(np.nanargmin(dist_station), dist_station.shape)
    
    # NDCI values
    station_ndci = ndci_array_mask[station_idx]
    
        
    # Find the new location to see if it is very far away
    station_lat_dif = lat_array_mask[station_idx]
    station_lon_dif = lon_array_mask[station_idx]
    #diiferencia de distancia 

    
    #SantaOlalla
    dif_lat= abs(float(lat)- station_lat_dif)
    dif_lon= abs(float(lon) - station_lon_dif)
    dif= dif_lat+dif_lon
    station=print("Station:", station_ndci)
    if dif> 0.0018:
        station_ndci= "Nan"
        
    station=print("station NDCI:", station_ndci)
   
    
    return station_ndci
    
   