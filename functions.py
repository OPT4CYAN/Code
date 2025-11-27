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
import os
import math  
import datetime 
#A small function that renames files so they all have the same format
def renombr(repro_site,site)->str:
    input_data                         = glob.glob(repro_site+ "data*")
    if len(input_data)!=0:
        file_names = np.array([os.path.basename(file) for file in input_data])
        code=0
        for put in range(len(file_names)):
            numb=int(file_names[put][(file_names[put].find("data")+len("data")):(file_names[put].find(".dat"))])
            if len(str(numb))>3:
                numb=int(file_names[put][(file_names[put].find("data")+len("data")):(file_names[put].find("_2"))])
            if len(str(numb))<3:
                form_numb='{:05}'.format(numb)
            else:
                form_numb=numb
            fecha='_'+str(200000000000+code)
            code=code+1
            name=site+'_data'                  
            rename=name+str(form_numb)+fecha+'.dat'
            os.rename(input_data[put],repro_site+rename)
    
    input_data                         = glob.glob(repro_site+ "*.dat")
    file_names = np.array([os.path.basename(file) for file in input_data])
    for put in range(len(file_names)):
        numb=int(file_names[put][(file_names[put].find("_data")+len("_data")):(file_names[put].find("_2"))])
        if len(str(numb))<5:
            form_numb='{:05}'.format(numb)
            rename=file_names[put][:(file_names[put].find("data")+len("data"))]+form_numb+file_names[put][(file_names[put].find("_2")):]
            os.rename(input_data[put],repro_site+rename)
            
#separate and format the raw data from the trios
def read_TRSdata (file_path:str)->float: 
    spectrum = {}
    attributes = {}
    data = []

    section = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("[END]"):
                continue

            if line.startswith("[") and line.endswith("]"):
                section = line.strip("[]")
                if section == "Attributes":
                    spectrum["Attributes"] = attributes
                elif section == "DATA":
                    spectrum["DATA"] = data
                continue

            if section == "Spectrum":
                key, value = line.split("=", 1)
                spectrum[key.strip()] = value.strip()

            elif section == "Attributes":
                if "=" in line:
                    key, value = line.split("=", 1)
                    attributes[key.strip()] = value.strip()

            elif section == "DATA":
                values = list(map(float, line.split()))
                data.append(values)
        spectrum['DATA']=np.array(spectrum['DATA'])
    return spectrum

  

#A program to calculate Sun zenith and azimuth for given date, time, latitude, and longitude
def sunposition (doy:float, hour:float, lat:float, lon:float)->float:
    #Returns:It returns the sun position [zenith, azimuth]
    #transform time
    
    #mean solar time
    mean_solar_time= hour + float(lon)/15.0 

    #equation of time
    a1= 1.00554*float(doy) - 6.28306    
    a2= 1.93946*float(doy) + 23.35089 
    equation_of_time= -7.67825*math.sin(a1/180.0*math.pi) - 10.09176*math.sin(a2/180.0*math.pi)

    #true solar time
    true_solar_time= mean_solar_time + equation_of_time/60.0 - 12.0

    #hour angle in degrees
    hour_angle= true_solar_time*15.0

    #solar declination in degrees
    a3= 0.9683*float(doy) - 78.00878    
    solar_declination= 23.4856*math.sin(a3/180.0*math.pi)

    #elevation and azimuth
    sun_y= math.sin(float(lat)/180.0*math.pi)*math.sin(solar_declination/180.0*math.pi) + math.cos(float(lat)/180.0*math.pi)*math.cos(solar_declination/180.0*math.pi)*math.cos(hour_angle/180.0*math.pi)
    elevation= math.asin(sun_y)/math.pi*180.0
    sun_x= math.cos(solar_declination/180.0*math.pi)*math.sin(hour_angle/180.0*math.pi)/math.cos(elevation/180.0*math.pi)
    corrected_sun_x= (-math.cos(float(lat)/180.0*math.pi)*math.sin(solar_declination/180.0*math.pi) + math.sin(float(lat)/180.0*math.pi)*math.cos(solar_declination/180.0*math.pi)*math.cos(hour_angle/180.0*math.pi))/math.cos(elevation/180.0*math.pi)
    azimuth= math.asin(sun_x)/math.pi*180.0
    
    if(corrected_sun_x <= 0):
        azimuth= 180.0 - azimuth
    if(corrected_sun_x > 0) and (sun_x <= 0):
        azimuth= 360.0 + azimuth
    azimuth= azimuth + 180.0
    
    if(azimuth > 360.0):
        azimuth= azimuth - 360.0
    
    zenith= 90.0 - elevation
    
    
    sun_position= [zenith,azimuth]   
    return sun_position


def doy_to_date(dayofyear):
    year            = int(dayofyear / 1000)
    day             = int(dayofyear % 1000)
    date            = datetime.datetime(year, 1, 1) + datetime.timedelta(days=int(day)-1)
    return date.strftime("%Y-%m-%d")


def settings_file(sentinel_dir, acolite_dir):
    output_dir     = sentinel_dir.replace("/","\\")
    output_dir2     = acolite_dir.replace("/","\\")
    contenido = [
    "## ACOLITE Station",
    f"inputfile={output_dir}tmp\\[change]",
    f"output={output_dir2}\\Output",
    "atmospheric_correction=True",
    "aerosol_correction=dark_spectrum",
    "s2_target_res=10",
    "l2w_parameters=ndci",
    "l2w_mask=True",
    "l2w_mask_wave=2190",
    "l2w_mask_threshold=0.0561",
    "rgb_rhot=True",
    "rgb_rhos=True",
    "map_l2w=True",
    "map_raster=True",
    "map_colorbar=True",
    "map_ext=tif"
    ]

    with open(sentinel_dir + "output/NDCI_doc/Settings_file.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(contenido))
