# -*- coding: utf-8 -*-
"""
@author:             Gonzalo M.F. 
Gonzalo Martínez-Fornos
gmartinez@icm.csic.es
Research institute:  ICM-CSIC 
Collaboration:       EBD-CSIC 
"""
import numpy as np
from index_alg import index_alg
import pandas as pd
# function that generates the indices based on res

def index_run (output_dir)->str:

    # We open the file created by group 1
    with open(output_dir + "_rrs.dat", "r") as rrs_doc:
        lines = rrs_doc.readlines()
 
    # Process the lines and split them by ';'
    linelist = [line.strip().split(";") for line in lines]
 
    # Convert the list of lists to a NumPy array
    ID                  = np.array(linelist)[1:,0].astype(int)
    doy                 = np.array(linelist)[1:,2].astype(float)
    year                = np.array(linelist)[1:,1].astype(int)
    Rrs                 = np.array(linelist)[1:,5:].astype(float)


    #We begin with the indexes; for this, we will have selected some
    index_data,index_name          = index_alg(Rrs)  
    
    
    #We created the code again to save it in .dat
    def c_m_arch(Today,appended):
        # Copy current file to previous file (rename)
        # Open the current file in append mode (append to the end)
        with open(Today, 'a') as Today:
            Today.writelines(appended)
    
    Today                               = output_dir+ "_index" +".dat"
    title                               =["ID","Year","Doy"] 
    
    with open(Today, 'w') as archivo:
       # Convert column3 into a text string where each value is separated by a ;
       columna2_str = ';'.join(map(str, index_name))
       columna1_str = ';'.join(map(str, title))
    
     # Write the data in one row, with the values ​​from column3 as columns separated by ;
       archivo.write(columna1_str + ";"+columna2_str+"\n")
        #create backup
    index_data             = np.transpose(index_data)
    for data in range(len(index_data)):
        columna2_str = ';'.join(map(str, index_data[data,:]))
        appended     =  (str(ID[data])+";"+str(int(year[data]))+";"+str(doy[data])+";"+columna2_str+"\n")
        c_m_arch(Today,appended)
    return ID

def normalize_fun (output_dir):
    with open(output_dir + "_index.dat", "r") as index_doc:
        lines = index_doc.readlines()
        
    # Process the lines and split them by ';'
    linelist = pd.DataFrame([line.strip().split(";") for line in lines])
    linelist.columns = linelist.iloc[0]
    linelist = linelist[1:].reset_index(drop=True)
    for i in linelist.columns:
        if i not in ('ID', 'Year', 'Doy'):
            tmp                = [np.nanmin(abs(linelist[i].values.astype(float))), np.nanmax(abs(linelist[i].values.astype(float)))]
            ecuation           = (abs(linelist[i].values.astype(float))-tmp[0])/(tmp[1]-tmp[0])
            linelist[i]        = ecuation
    linelist.to_csv(output_dir+ "_normalized_index" +".dat", sep=';', index=False) 
    
    
    
def pcu_chl (output_dir):
    with open(output_dir + "_normalized_index.dat", "r") as index_doc:
        lines = index_doc.readlines()
        
    # Process the lines and split them by ';'
    linelist = pd.DataFrame([line.strip().split(";") for line in lines])
    linelist.columns = linelist.iloc[0]
    linelist = linelist[1:].reset_index(drop=True)
    keys = ["PC_D", "PC_SY", "PC_S", "PC_RV", "PC_H1", "PC_H1b",
        "PC_H3", "PC_W", "PC_L", "PC_Lu", "PC_Br1", "PC_Br2", "PC_Br3"]
    
    values = np.array([linelist[k] for k in keys])
    values = np.where(values == '', np.nan, values).astype(float)
    pcu_index                 = np.nanmean(values,axis=0)
    keys = ["Chla_NDCI", "Chla_G08","chla_OC4Me", "CHL_m", "CHL2D_m", "CHL2C_m", "CHL_P", "CHL2_P"]
    values = np.array([linelist[k] for k in keys])
    values = np.where(values == '', np.nan, values).astype(float)
    chl_index                 = np.nanmean(values,axis=0)
    
    arrays = [np.array(a).reshape(-1,1) for a in [
    linelist['ID'], linelist['Year'], linelist['Doy'], pcu_index, chl_index,linelist['NDCI']]]
    new_text = np.concatenate(arrays, axis=1)
    title = np.array(['ID','Year','Doy','PCu','Chl','NDCI'])

    new_text = pd.DataFrame(new_text, columns=title)
    new_text.to_csv(output_dir+ "_pcu_chl_index" +".dat", sep=';', index=False) 
