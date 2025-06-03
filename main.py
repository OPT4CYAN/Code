# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:51:11 2024

@author: gmart
"""
import os
os.chdir('C:/Users/gmart/Proyectos/opt4cyan_tmart/lib')
from activate import activate
import glob
import shutil

dir_ini = "C:/Users/gmart/Proyectos/opt4cyan_tmart/"
web_dir            ="C:/Users/gmart/Proyectos/Web_Control_Doñana/"
site               = ['Lucio_del_Rey','Hondon_del_Burro','Fuente_del_Duque','Santa_Olalla']

#iniciar proceso
alerta= activate(dir_ini,web_dir)

#hacer para mover la imgen que detecta alerta 
for f in site:
    name_alert =  web_dir+"Plots/Alert/"+f+".png"    
    out_imagen_dir =  web_dir+"Plots/Alert/"
    if alerta[f]== True:
        imagen_dir                        = glob.glob(out_imagen_dir +"Antes/"+ f+"_alert.png") 
        shutil.copy(imagen_dir[0],  name_alert)
        
    if alerta[f]== False:
        imagen_dir                        = glob.glob(out_imagen_dir +"Antes/"+ f+"_ok.png") 
        shutil.copy(imagen_dir[0],  name_alert)
    
    if alerta[f]== None:
        imagen_dir                        = glob.glob(out_imagen_dir +"Antes/"+ f+"_check.png") 
        shutil.copy(imagen_dir[0],  name_alert)
    
        