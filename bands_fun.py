# -*- coding: utf-8 -*-
"""
Created on Fri May 19 12:10:13 2023
@author: Gonzalo Martínez Fornos
gmail:gmartinez@icm.csic.es
"""
#funcion para crear la union de bandas para el indice Mndwi
import zipfile
import shutil
import glob
import os
import pathlib
from mndwi_fun import mndwi_fun
from qwip_fun import qwip_fun
from datetime import datetime,timedelta
def bands_fun (root_dir)->str:
    def descomprimir_archivo(archivo_zip, directorio_destino):
        with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
            zip_ref.extractall(directorio_destino)
        print("Archivo descomprimido con éxito.")
    
    def eliminar_carpeta_safe(carpeta_safe):
        shutil.rmtree(carpeta_safe)
    
    
    downloads                   = root_dir+"downloads/"
    tmp                         = root_dir+"tmp/"

    
    #decompress
    dir_zip                     = glob.glob(downloads +"*.zip")
    

    for i in dir_zip:
        try:
            #descomprimir archivos
            descomprimir_archivo(i, tmp)
            
            # create folder
          
            dir_safe            = glob.glob(tmp+"/*")[0]
            base_name           = os.path.basename(dir_safe)[:3]
            name                =os.path.basename(dir_safe[:dir_safe.find('.SAFE')])
            # Reemplaza con tu fecha almacenada
            ruta_safe           = glob.glob(tmp + "/*")
            ruta_safe           = ruta_safe[0]
    
    ############ Creacion de los valores utiles
            # MNDWI
            
            dir_bands           = dir_safe + "/GRANULE/" 
            directorio          = pathlib.Path(dir_bands)
            for fichero in directorio.iterdir():
                folder_in       = fichero.name
                
            dir_bands           = dir_bands + folder_in + "/IMG_DATA/"
            
            #dir bandas
            
            # 490
            dir_b02            = glob.glob(dir_bands + "R20m/" + "*B02_20m.jp2")[0]
            #560
            dir_b03             = glob.glob(dir_bands + "R20m/" + "*B03_20m.jp2")[0]
            #665
            dir_b04             = glob.glob(dir_bands + "R20m/" + "*B04_20m.jp2")[0]
            # 1600
            dir_b11             = glob.glob(dir_bands + "R20m/" + "*B11_20m.jp2")[0]
            
            mndwi_stations      = mndwi_fun(dir_b03, dir_b11)
            
            try:
                #443
                dir_b01             = glob.glob(dir_bands + "R20m/" + "*B01_20m.jp2")[0]
                qwip_stations       = qwip_fun(dir_b01,dir_b02,dir_b03,dir_b04)
            #ndwi_stations       = ndwi_fun(dir_b03_10, dir_b08_10)
            #swi_stations        = swi_fun(dir_b05, dir_b11)
            
            
                
    # Abrir el archivo actual en modo append (añadir al final)
            except:
                print('NOT b01 ...............NO')
                #443
                dir_b01             = glob.glob(dir_bands + "R60m/" + "*B01_60m.jp2")[0]
                # 490
                dir_b02            = glob.glob(dir_bands + "R60m/" + "*B02_60m.jp2")[0]
                #560
                dir_b03             = glob.glob(dir_bands + "R60m/" + "*B03_60m.jp2")[0]
                #665
                dir_b04             = glob.glob(dir_bands + "R60m/" + "*B04_60m.jp2")[0]
                
                
                qwip_stations       = qwip_fun(dir_b01,dir_b02,dir_b03,dir_b04)
            #ndwi_stations       = ndwi_fun(dir_b03_10, dir_b08_10)
            #swi_stations        = swi_fun(dir_b05, dir_b11)
           
            
            
           
            
    ######## guardar los datos en doc
    
            data                = name[11:19]
            fecha               = datetime.strptime(data, "%Y%m%d")  
            doy                 = str(fecha.strftime('%Y'))+str(fecha.strftime('%j'))
    
           #creamos el codigo otra vez para guardarlo en .dat 
            def c_m_arch(Today,appended):
               # Copy current file to previous file (rename)
               # Open the current file in append mode (append to the end)
               with open(Today, 'a') as Today:
                   Today.writelines(appended)
                   print("Operación completada sin errores.")
        
            Today               = root_dir + "mndwi.dat"
                
            appended            = [ str(doy) + ";"  +str(mndwi_stations['Santa_Olalla'])+";"  +str(mndwi_stations['Lucio_del_Rey'])+";"  +str(mndwi_stations['Hondon_del_Burro'])+";"  +str(mndwi_stations['Fuente_del_Duque'])+"\n"]
            c_m_arch(Today,appended)
            
            Today               = root_dir + "qwip.dat"
                
            appended            = [ str(doy) + ";"  +str(qwip_stations['Santa_Olalla'])+";"  +str(qwip_stations['Lucio_del_Rey'])+";"  +str(qwip_stations['Hondon_del_Burro'])+";"  +str(qwip_stations['Fuente_del_Duque'])+"\n"]
            c_m_arch(Today,appended)
            
            
            eliminar_carpeta_safe(tmp)

        except Exception as e:
                # Just print(e) is cleaner and more likely what you want,
                # but if you insist on printing message specifically whenever possible...
                if hasattr(e, 'message'):
                    print(e.message)
                else:
                    print(e)











































