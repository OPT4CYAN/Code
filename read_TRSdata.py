
"""
Created on Wed May 17 11:36:29 2023
@author: Gonzalo Martínez Fornos
gmail:gmartinez@icm.csic.es
"""
import numpy as np
#separa y formatea los datos brutos del trios
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
     
    
