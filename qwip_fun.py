# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 17:38:39 2025

@author: gmart
"""

from dec_UTM import dec_UTM
import rasterio.warp
#def para generar el mdwi
def qwip_fun(b01:str, b02:str, b03:str,b04:str)->float:

    # environmental variables
    site_name           = ['Santa_Olalla','Lucio_del_Rey','Hondon_del_Burro','Fuente_del_Duque']
    site_latitude       = [         36.98,          36.92,             37.00,             37.00]
    site_longitude      = [         -6.48,          -6.35,             -6.42,             -6.43]
    site_heading        = [            45,              0,                 0,                45]
    
    SantaOlalla_lat = site_latitude[0]
    SantaOlalla_lon = site_longitude[0]
    Lucio_lat = site_latitude[1]
    Lucio_lon = site_longitude[1]
    Burro_lat = site_latitude[2]
    Burro_lon = site_longitude[2]
    Duque_lat = site_latitude[3]
    Duque_lon = site_longitude[3]

    # Cargar Bandas
    file_path_b1 = b01
    file_path_b2 = b02
    file_path_b3 = b03
    file_path_b4 = b04
    
    # Convertir a UTM
    SantaOlalla_x = dec_UTM(SantaOlalla_lat,SantaOlalla_lon)[0]
    SantaOlalla_y = dec_UTM(SantaOlalla_lat,SantaOlalla_lon)[1]
    
    Lucio_x = dec_UTM(Lucio_lat,Lucio_lon)[0]
    Lucio_y = dec_UTM(Lucio_lat,Lucio_lon)[1]
    
    Burro_x = dec_UTM(Burro_lat,Burro_lon)[0]
    Burro_y = dec_UTM(Burro_lat,Burro_lon)[1]
    
    Duque_x = dec_UTM(Duque_lat,Duque_lon)[0]
    Duque_y = dec_UTM(Duque_lat,Duque_lon)[1]
    
    estaciones = [(SantaOlalla_y, SantaOlalla_x),( Lucio_y,  Lucio_x), (Burro_y, Burro_x), (Duque_y,Duque_x)]
    
    #transformacion de bandas 
    
    def image_bounds(col, row, image_shape):
        return 0 <= col < image_shape[1] and 0 <= row < image_shape[0]
    
    with rasterio.open(file_path_b1) as dataset_b1, rasterio.open(file_path_b2) as dataset_b2, rasterio.open(file_path_b3) as dataset_b3, rasterio.open(file_path_b4) as dataset_b4:
        band_data_b1 = dataset_b1.read(1)
        band_data_b2 = dataset_b2.read(1)
        band_data_b3 = dataset_b3.read(1)
        band_data_b4 = dataset_b4.read(1)
        transform = dataset_b3.transform
        image_shape = band_data_b3.shape
        
        resultado = {}
        station_name = ['Santa_Olalla','Lucio_del_Rey','Hondon_del_Burro','Fuente_del_Duque']
        
        
        # Realizamos el analisis y recalcamos condicion de si esta fuera 
        #de rango se cambia por none
        for i, estacion in enumerate(estaciones):
            lat, lon = estacion
            col, row = ~transform * (lon, lat)
            col, row = int(round(col)), int(round(row))
    
            if image_bounds(col, row, image_shape):
                valor_b1 = float(band_data_b1[row, col])
                valor_b2 = float(band_data_b2[row, col])
                valor_b3 = float(band_data_b3[row, col])
                valor_b4 = float(band_data_b4[row, col])
                if valor_b1-valor_b2-valor_b3-valor_b4 != 0:
                    ndi = (valor_b4 - valor_b2) / (valor_b4 + valor_b2)
                    avw = (valor_b1 + valor_b2 + valor_b3 + valor_b4)/((valor_b1 / 443) + (valor_b2 / 490) + (valor_b3 / 560) + (valor_b4 / 665))
                    ndip = (-8.399885*10**-9 * avw**4) + (1.715532*10**-5 * avw**3) + (-1.301670*10**-2 * avw**2) + (4.357838*10**0 * avw) + (-5.449532 * 10**2) 
                    resultado_calculo = ndi - ndip
                    station = station_name[i]
                    resultado[station] = round(resultado_calculo,8)
                    print(f"Resultado del cálculo en la estación ({station}): {resultado[station]}")
                else:
                    station = station_name[i]
                    resultado[station] = None
                    print(f"Resultado del cálculo en la estación ({station}): None")
            else:
                station = station_name[i]
                resultado[station] = None
                print(f"Resultado del cálculo en la estación ({station}): None")
    return resultado