# -*- coding: utf-8 -*-
"""
@author:             Gonzalo M.F. 
Gonzalo Martínez-Fornos
gmartinez@icm.csic.es
Research institute:  ICM-CSIC 
Collaboration:       EBD-CSIC 
"""
import zipfile
import glob
import os
import shutil
import subprocess
from ndci_generator import ndci_generator
from datetime import datetime,timedelta
#The Acolite file creation function is somewhat cumbersome and the process is rather slow.
def acolite_fun (acolite_dir,root_dir,lat,lon)->str:
    def descomprimir_archivo(archivo_zip, directorio_destino):
        with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
            zip_ref.extractall(directorio_destino)
        print("Archivo descomprimido con éxito.")
    
    downloads = root_dir +"Downloads/"
    tmp = root_dir+"tmp/"
    output = root_dir+"output/"
    output_dat = root_dir.replace('Sentinel', 'output')
    
    #decompress
    dir_zip = glob.glob(downloads+"*.zip")
    for i in dir_zip:
        try:
            descomprimir_archivo(i, tmp)
        
            # create folder
            dir_safe            = glob.glob(tmp+"/*")
            dir_safe            = dir_safe[0].replace("\\","/")
            name                =dir_safe[dir_safe.find('MS'):dir_safe.find('.SAFE')]
            
            dir_folder = os.path.join(output, name)
            os.makedirs(dir_folder)
            settings = dir_dest = output + "/" + name + "/Settings_file.txt"
            new = open(settings, "w")
        
            # copy of .txt
            def mod_txt(arch_origen, dir_dest, remplazo):
                shutil.copy(arch_origen, settings)
                with open(settings, 'r') as file:
                    cambio = file.read()
        
                modif = cambio.replace(remplazo, name_arch)
                with open(settings, 'w') as file:
                    file.write(modif)
        
            arch_origen = output+"/NDCI_doc/Settings_file.txt"
            name_arch = dir_safe[dir_safe.find('S2'):]
            dir_dest = output + name_arch
            remplazo = "[change]"
        
            mod_txt(arch_origen, dir_dest, remplazo)
                
            #ACOLITE ACTIVATE
            os.chdir(acolite_dir)
            comando =  'dist\\acolite\\acolite.exe --cli --settings='+root_dir+'Output\\'
            comando = comando.replace("/", "\\")
            comando = comando + name + '\\Settings_file.txt"'
            subprocess.run(comando, shell=True)
            print("Acolite ok")
            
            #Acolite data is created in this dir due to lack of permissions when executing the command
            #now we move them to the created folder
            
            origin_folder = acolite_dir+"/Output/"
            destination_folder= output+"/" +name
            arch = os.listdir(origin_folder)
            
            
            dir_nc= glob.glob(origin_folder + "/"+ "*L2W.nc")
            dir_nc= dir_nc[0]
            #This is in case it fails at some point.
            data= name[41:49]
            if len(dir_nc)==0:
                print("FAIL:"+data)
            #Continue if there are no errors
            dir_nc= dir_nc.replace("\\","/")
            ndci= ndci_generator(dir_nc,destination_folder,name,origin_folder,lat,lon)
            

            fecha = datetime.strptime(data, "%Y%m%d")  
            doy                 = str(fecha.strftime('%Y'))+str(fecha.strftime('%j'))
            
            
            def c_m_arch(Today,appended):
               # Copy current file to previous file (rename)
               # Open the current file in append mode (append to the end)
               with open(Today, 'a') as Today:
                   Today.writelines(appended)
                   print("Operación completada sin errores.")
            
            Today               = output_dat + "sentinel_ndci.dat"
            if len(glob.glob(Today))==0:
                with open(Today, 'w') as archivo:
                    archivo.write("Doy;Station\n")
                
                  
            appended = [ str(doy) + ";"+ str(ndci) + "\n"]
            c_m_arch(Today,appended)
             
            def eliminar_carpeta_safe(carpeta_safe):
                try:
                    
                    shutil.rmtree(carpeta_safe)
                    print("Carpeta .SAFE eliminada:", carpeta_safe)
                except Exception as e:
                    print("Error al eliminar la carpeta .SAFE:", e)
            # Example of use
            carpeta_safe = acolite_dir+"//Tmp//"
            eliminar_carpeta_safe(carpeta_safe)
            eliminar_carpeta_safe(tmp)
        except Exception as e:
            print("Error por no ser .zip ", e)
            
        origin_folder = acolite_dir+"/Output/"
        for j in os.listdir(origin_folder):
            os.remove(os.path.join(origin_folder,j))
    
    

     
