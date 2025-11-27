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
import functions as fn
from datetime import datetime
#preapracion de datos
def pre_run (file,temp_dir)->str:

    # We create a loop to process the file (it's a .dat file)
    # After opening the .dat file, we read the lines
    # And we use an if statement to remove any erroneous values ​​that don't end with END
    lines                          =open(file,"r").readlines()
    if lines[len(lines)-2]=='[END] of [Spectrum]\n':
        #We read every line and cut every time we find the word
        data                           = open(file,"r")
        for dummy in iter(data.readline,''):
            if not dummy:
                break
            if '#TBID:' in dummy:
                tmp_name                    = dummy.split('#TBID:')
                tmp_name                    = tmp_name[1].replace(" ", "_")
                tmp_name                    = tmp_name.replace(":", "-")
                fields                      = tmp_name.split(";")
                if fields[2]                == 'RAW':
                    fname_out               = (fields[1] + '_Spectrum_RAW_'  + fields[0] + '_000_' + fields[1]  + '_1234_RAW' + fields[0] + '_000_00.dat')
                else:
                    fname_out               = (fields[1] + '_Spectrum_Calibrated_' + fields[0] + '_000_' + fields[1] + '_1234_Calibrated_' + fields[0] + '_000_01.dat')
            if '[Spectrum]' in dummy:
                with open(temp_dir + fname_out, "w") as unit2:
                    unit2.writelines(str(dummy.format("%s\r\n")))
                    while True:
                        dummy               = data.readline()
                        unit2.writelines(str(dummy.format("%s\r\n")))
                        if '[END] of [Spectrum]' in dummy:
                            break
        
        data.close()
        
        
        

def rrs_run(output_dir,code,temp_dir,lat,lon):
       #Now it's time for a data cleaner to keep only a doc from social media
    wl                          = list(range(400,902,2))
    float_formatter                         = "{:.8f}".format #is for format 
    np.set_printoptions(formatter={'float_kind':float_formatter}) 
    #calculate es, lt and li with rearrange measurements script
    #a loop is needed to calculate ES, LT, and LI
    ##### calibrated #MT
    keys=['es','li','lt']
    sensors=[
        glob.glob(temp_dir + code['ed'] + "*Calibrated*" + "*.dat"),
        glob.glob(temp_dir + code['li'] + "*Calibrated*" + "*.dat"),
        glob.glob(temp_dir + code['lt'] + "*Calibrated*" + "*.dat"),]
    
    def c_m_arch(Today,appended):
                # Copy current file to previous file (rename)
                # Open the current file in append mode (append to the end)
                with open(Today, 'a') as Today:
                    Today.writelines(appended)
####
###We need to filter by hours of interest and angle
  
    all_data={}
    all_doy={}
    all_angle={}
    k=0
    for sensor in sensors:
        measurement                 = np.zeros((0,len(wl)))
        doy                         = np.zeros((0,1))
        year                        = np.zeros((0,1))
        angle                       = np.zeros((0,2))
        count                       = 0

        for s in sensor:
    
            #if sensor:
            #We structure data in a variable
            data = fn.read_TRSdata(str(s))
            time = datetime.strptime(data['DateTime'], "%Y-%m-%d %H:%M:%S")
            # We apply an initial filter by time of day to remove the hours when there is clearly no light.
            # This speeds up the process, and then we filter by angle, between 40 and 90 degrees.
            if 10 <= time.hour <= 16:
                measurement_tmp = np.interp(wl, data['DATA'][0:-1, 0], data['DATA'][0:-1, 1])
                doy_tmp = float(time.strftime('%j'))
                hour_d = time.hour + (time.minute + time.second / 60) / 60
                angle_tmp = fn.sunposition(doy_tmp, hour_d, lat, lon)
                zenith = angle_tmp[0]
    
                if 40 <= zenith <= 90:
                    doy = np.append(doy, doy_tmp + round(hour_d / 24, 4))
                    year = np.append(year, time.year)
                    measurement = np.append(measurement, [measurement_tmp], axis=0)
                    angle = np.append(angle, [angle_tmp], axis=0)
                    count += 1
        all_data[keys[k]]=measurement
        all_doy[keys[k]]=doy
        all_angle[keys[k]]=angle
        k=k+1
        
        print("Complete sensors Variable     100%")
    
   #Finally we create the RRs variable and save it in a .dat file or an array
    Rrs                                     = np.zeros((0,len(wl)))
    doy_rrs                                 = np.zeros((0,1))
    angle_rrs                               = np.zeros((0,2))
    year_rrs                                = np.zeros((0,1))
    
    #create a variable RRs and create file document and paste the important dates
    id_min_angle                            = min(all_angle)
    if len(all_doy['lt'])!=0 and len(all_doy['es'])!=0:
        for z in np.arange(len(all_doy['lt'])):
            delta_t                         = abs(all_doy['lt'][z] - all_doy['es'])
            if min(delta_t) < 1e-5: #1./(24*60*60) # 1 sec
                index_t                     = np.where(delta_t == min(delta_t))                    
                Rrs                         = np.append(Rrs,np.divide(all_data['lt'][z],all_data['es'][index_t]),axis=0)
                doy_rrs                     = np.append(doy_rrs,all_doy['lt'][z])
                doy_str                     = [str(int(num)).zfill(3) for num in doy_rrs]
                angle_rrs                   = np.append(angle_rrs,all_angle[id_min_angle][index_t],axis=0)
                year_rrs                    = np.append(year_rrs,year[z])
                year_str                    =  [str(int(num)) for num in year_rrs]
                ID                          = [year_str[i] + doy_str[i] for i in range(len(doy_str))]
       
        #We save it in an array or .dat
        title                               =["Id","Year","Doy","Zenith","Azimuth"] 
        #We make him make his name on social media and the value of wl
        name_rrs = [f"Rrs_{r}" for r in range(400, 901, 2)]
        #We created the files because the first attempt doesn't exist; it will only happen once.
        if len(glob.glob(output_dir))==0:
            with open(output_dir, 'w') as archivo:
               # Convert column3 into a text string where each value is separated by a ;
               columna2_str = ';'.join(map(str, name_rrs))
               columna1_str = ';'.join(map(str, title))
        
               # Write the data in one row, with the values ​​from column3 as columns separated by ;
               archivo.write(columna1_str + ";"+columna2_str+"\n")
       
        for data in range(len(Rrs)):
            columna2_str = ';'.join(map(str, Rrs[data,:]))
            columna1_str = ';'.join(map(str, angle_rrs[data,:]))
            appended     =  (str(ID[data])+";"+str(int(year_rrs[data]))+";"+str(doy_rrs[data])+";"+columna1_str+";"+columna2_str+"\n")
            c_m_arch(output_dir,appended)
 
            
    else:
        print("Not Rrs: sensor fail")
        
    
        
    