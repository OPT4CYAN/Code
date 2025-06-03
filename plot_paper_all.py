# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:42:23 2024

@author: gmart
"""

import matplotlib.pyplot as plt 
import glob
import numpy as np
import os
from datetime import datetime
from matplotlib.ticker import (MultipleLocator)
import sympy as sp
os.chdir("C:/Users/gmart/Desktop/Scripts_paper_OPT4CYAN/")
from Smoo_filter import Smoo_filter
from matplotlib.dates import MonthLocator, DateFormatter
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter, MonthLocator
from matplotlib.gridspec import GridSpec

old                     = "C:/Users/gmart/Desktop/Scripts_paper_OPT4CYAN/Santa_Olalla_index_filtered.dat" #s abre de forma solo lectura
with open(old, "r") as doc:
    lines = doc.readlines()

# Procesar las líneas y dividirlas por ';'
linelist = [line.strip().split(";") for line in lines]
linelist=np.array(linelist)


ID                      = linelist[1:,0].astype(float).astype(int).astype(str)
wl                      = list(range(400,902,2))

index                    =linelist[1:,3:].astype(float) 
doy                      = linelist[1:,0].astype(float).astype(int)
#filtramos los datos solo hasta finales de 2023
index                    = index[:,:1065]
doy                      = doy[:1065]  
day_min                  = min(doy)
    
PC_D                     = index[:,0].astype(float)
PC_D                     = PC_D[np.where(doy>=int(day_min))]
pc_d                     = PC_D
#Smoothing filter
pc_d                     =Smoo_filter(pc_d,6)

r                        = pc_d[:][~np.isnan(pc_d[:])]
pc_d_max                 = max(abs(r))
pc_d                     = ((abs(pc_d[:])-min(abs(r)))/(max(abs(r))-min(abs(r))))
                   

PC_SY                    = index[:,1].astype(float)
PC_SY                    = PC_SY[np.where(doy>=int(day_min))]
pc_sy                    = PC_SY
#Smoothing filter
pc_sy                     =Smoo_filter(pc_sy,6)
r                        = pc_sy[:][~np.isnan(pc_sy[:])]
pc_sy_max                = max(abs(r))
pc_sy                    = ((abs(pc_sy)-min(abs(r)))/(max(abs(r))-min(abs(r))))


PC_S                     = index[:,2].astype(float)
PC_S                     = PC_S[np.where(doy>=int(day_min))]
pc_s                     = PC_S
#Smoothing filter
pc_s                     =Smoo_filter(pc_s,6)
r                        = pc_s[:][~np.isnan(pc_s[:])]
pc_s_max                 = max(abs(r))
pc_s                     = ((abs(pc_s)-min(abs(r)))/(max(abs(r))-min(abs(r))))


PC_RV                   = index[:,3].astype(float)
PC_RV                   = PC_RV[np.where(doy>=int(day_min))]
pc_rv                   = PC_RV
#Smoothing filter
pc_rv                    =Smoo_filter(pc_rv,6)
r                       = pc_rv[:][~np.isnan(pc_rv[:])]
pc_rv_max               = max(abs(r))
pc_rv                   = ((abs(pc_rv)-min(abs(r)))/(max(abs(r))-min(abs(r))))
        
PC_H1b                  = index[:,5].astype(float)
PC_H1b                  = PC_H1b[np.where(doy>=int(day_min))]
pc_h1b                  = PC_H1b
#Smoothing filter
pc_h1b                     =Smoo_filter(pc_h1b,6)
r                       = pc_h1b[:][~np.isnan(pc_h1b[:])]
pc_h1b_max              = max(abs(r))
pc_h1b                  = ((abs(pc_h1b)-min(abs(r)))/(max(abs(r))-min(abs(r))))
        
PC_H3                   = index[:,6].astype(float)
PC_H3                   = PC_H3[np.where(doy>=int(day_min))]
pc_h3                   = PC_H3
#Smoothing filter
pc_h3                     =Smoo_filter(pc_h3,6)
r                       = pc_h3[:][~np.isnan(pc_h3[:])]
pc_h3_max               = max(abs(r))
pc_h3                   = ((abs(pc_h3)-min(abs(r)))/(max(abs(r))-min(abs(r))))
    

PC_L                    = index[:,8].astype(float)
PC_L                    = PC_L[np.where(doy>=int(day_min))]
pc_l                    = PC_L
#Smoothing filter
pc_l                    =Smoo_filter(pc_l,6)
r                       = pc_l[:][~np.isnan(pc_l[:])]
pc_l_max                = max(abs(r))
pc_l                    = ((abs(pc_l)-min(abs(r)))/(max(abs(r))-min(abs(r))))


Chla_NDCI               = index[:,9].astype(float)
Chla_NDCI               = Chla_NDCI[np.where(doy>=int(day_min))]
chla_ndci               = Chla_NDCI
#Smoothing filter
chla_ndci               =(Smoo_filter(chla_ndci,6))
r                       = chla_ndci[:][~np.isnan(chla_ndci[:])]
chla_ndci_max           = max(abs(r))
chla_ndci               = ((abs(chla_ndci)-min(abs(r)))/(max(abs(r))-min(abs(r))))


Chla_G08                = index[:,10].astype(float)
Chla_G08                = Chla_G08[np.where(doy>=int(day_min))]
chla_g08                = Chla_G08
#Smoothing filter
chla_g08                =Smoo_filter(chla_g08,6)
r                       = chla_g08[:][~np.isnan(chla_g08[:])]
chla_g08_max            = max(abs(r))
chla_g08                = ((abs(chla_g08)-min(abs(r)))/(max(abs(r))-min(abs(r))))


CHL_m                   = index[:,16].astype(float)
CHL_m                   = CHL_m[np.where(doy>=int(day_min))]
chl_m                   = CHL_m
#Smoothing filter
chl_m                   =Smoo_filter(chl_m,6)
r                       = chl_m[:][~np.isnan(chl_m[:])]
chl_m_max               = max(abs(r))
chl_m                   = ((abs(chl_m)-min(abs(r)))/(max(abs(r))-min(abs(r))))


CHL2D_m                 = index[:,17].astype(float)
CHL2D_m                 = CHL2D_m[np.where(doy>=int(day_min))]
chl2d_m                 = CHL2D_m
#Smoothing filter
chl2d_m                   =Smoo_filter(chl2d_m,6)
r                       = chl2d_m[:][~np.isnan(chl2d_m[:])]
chl2d_m_max             = max(abs(r))
chl2d_m                 = ((abs(chl2d_m)-min(abs(r)))/(max(abs(r))-min(abs(r))))

CHL2C_m                 = index[:,18].astype(float)
CHL2C_m                 = CHL2C_m[np.where(doy>=int(day_min))]
chl2c_m                 = CHL2C_m
#Smoothing filter
chl2c_m                   =Smoo_filter(chl2c_m,6)
r                       = chl2c_m[:][~np.isnan(chl2c_m[:])]
chl2c_m_max             = max(abs(r))
chl2c_m                 = ((abs(chl2c_m)-min(abs(r)))/(max(abs(r))-min(abs(r))))

CHL_P                   = index[:,19].astype(float)
CHL_P                   = CHL_P[np.where(doy>=int(day_min))]
chl_p                   = CHL_P
#Smoothing filter
chl_p                   =Smoo_filter(chl_p,6)
r                       = chl_p[:][~np.isnan(chl_p[:])]
chl_p_max               = max(abs(r))
chl_p                   = ((abs(chl_p)-min(abs(r)))/(max(abs(r))-min(abs(r))))

CHL2_P                  = index[:,20].astype(float)
CHL2_P                  = CHL2_P[np.where(doy>=int(day_min))]
chl2_p                  = CHL2_P 
#Smoothing filter
chl2_p                   =Smoo_filter(chl2_p,6)
r                       = chl2_p[:][~np.isnan(chl2_p[:])]
chl2_p_max              = max(abs(r))
chl2_p                  = ((abs(chl2_p)-min(abs(r)))/(max(abs(r))-min(abs(r))))


PC_BR2                  = index[:,13].astype(float)
PC_BR2                  = PC_BR2[np.where(doy>=int(day_min))]
pc_br2                  = PC_BR2
#Smoothing filter
pc_br2                    =Smoo_filter(pc_br2,6)
r                       = pc_br2[:][~np.isnan(pc_br2[:])]
pc_br2_max              = max(abs(r))
pc_br2                  =((abs(pc_br2)-min(abs(r)))/(max(abs(r))-min(abs(r))))


Chla_OC4ME              = index[:,15].astype(float)
Chla_OC4ME              = Chla_OC4ME[np.where(doy>=int(day_min))]
chla_oc4me              = Chla_OC4ME
#Smoothing filter
chla_oc4me                    =Smoo_filter(chla_oc4me,6)
r                       = chla_oc4me[:][~np.isnan(chla_oc4me[:])]
chla_oc4me_max          = max(abs(r))
chla_oc4me              = ((abs(chla_oc4me)-min(abs(r)))/(max(abs(r))-min(abs(r))))

NDCI                     = index[:,21].astype(float)
ndci                   = Smoo_filter(NDCI,3)
ndci                     = NDCI[np.where(doy>=int(day_min))]
#Smoothing filter
#ndci                    =Smoo_filter(ndci,2)
#r                       = ndci[:][~np.isnan(ndci[:])]
#ndci_max                 = np.nanmax(abs(r))
#ndci                     = ((ndci-np.nanmin(abs(ndci)))/(np.nanmax(abs(r))-np.nanmin(abs(r))))

doy                     = doy.astype(str)


#aqui cambiamos el doy a fecha normal en eje x
fech_doy = np.zeros((0,1))
i=0
while True:
    if i== len(doy):
        break
    else:
        x=datetime.strptime(str(doy[i][0:4]) + str(doy[i][4:]), "%Y%j").strftime("%d-%m-%Y")
        fech_doy=np.append(fech_doy,x)
    i=i+1
    
    
#insitu

old                     = "C:/Users/gmart/Desktop/Scripts_paper_OPT4CYAN/2020-2024 Santa_Olalla fisicoqui.csv" #s abre de forma solo lectura
with open(old, "r") as doc:
    lines = doc.readlines()

# Procesar las líneas y dividirlas por ';'
linelist_lab = [line.strip().split(";") for line in lines]
linelist_lab=np.array(linelist_lab)

doy                      = linelist_lab[1:,0]
year                     = linelist_lab[1:,13]
mes                        = linelist_lab[1:,13]
chla                     = linelist_lab[1:,12]
cyano                    = linelist_lab[1:,11]


x                        = np.where(cyano!='')[0]
cyano                    = cyano[x].astype(float)
doy                      = doy[x]
mes                    = mes[x]
year                    = year[x]

index_lab=cyano
index_lab_1= index_lab/1000
index_lab_copy=index_lab_1
index_nan=[0,1,2,3,4,5,6,7,8,9,16,17,18,19,20,28,27,29,30,31,32]
index_lab_copy[index_nan]=np.nan

fech_doy_lab = np.zeros((0,1))
fech_doy_lab=[datetime.strptime(date_str, "%d/%m/%Y").date() for date_str in doy]




index_std_lab =  np.nanstd(index_lab)
dif_n_lab =index_lab - index_std_lab
dif_p_lab = index_lab + index_std_lab
dif_n_lab[(dif_n_lab < 0)] = 0
dif_n_lab[(dif_n_lab > 1)] = 1
dif_p_lab[(dif_p_lab < 0)] = 0
dif_p_lab[(dif_p_lab > 1)] = 1
    
#mean
# mean_cy
mean_cy = np.zeros((0, 1))
std_cy = np.zeros((0, 1))
for i in range(len(pc_d)):
    m = np.mean((pc_d[i] , pc_rv[i] , pc_sy[i] , pc_h1b[i] , pc_br2[i] , pc_l[i], pc_h3[i],pc_s[i]))
    s = np.std((pc_d[i] , pc_rv[i] , pc_sy[i] , pc_h1b[i] , pc_br2[i] , pc_l[i], pc_h3[i],pc_s[i]))
    mean_cy = np.append(mean_cy, [m])
    std_cy = np.append(std_cy, [s])

dif_n =mean_cy - std_cy
dif_p = mean_cy + std_cy
dif_n[(dif_n < 0)] = 0
dif_n[(dif_n > 1)] = 1
dif_p[(dif_p < 0)] = 0
dif_p[(dif_p > 1)] = 1
#create all plots
#Plots chla
fech_doy = [datetime.strptime(date_str, "%d-%m-%Y").date() for date_str in fech_doy]





#Grafico nuevo
#######################cortes

####################################
#######################################

# Formato de fecha y rango mínimo y máximo
month_fmt = DateFormatter("%b %Y")
min_fecha = fech_doy[31]
max_fecha = np.max(fech_doy)

# Lista de límites en el eje x para cada subgráfico y su ancho proporcional
x_limits = [(fech_doy[0], fech_doy[215]), 
            (fech_doy[358], fech_doy[512]), 
            (fech_doy[682], fech_doy[830]), 
            (fech_doy[1030], fech_doy[1064])]

proporciones = [(xmax - xmin) / (max_fecha - min_fecha) for xmin, xmax in x_limits]

# Crear figura y GridSpec
fig = plt.figure(figsize=(50, 30))
gs = GridSpec(1, 4, width_ratios=proporciones, wspace=0.05)

# Crear subgráficos dentro del GridSpec
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1], sharey=ax1)
ax3 = fig.add_subplot(gs[2], sharey=ax1)
ax4 = fig.add_subplot(gs[3], sharey=ax1)
ax1.spines['right'].set_visible(False)
ax4.spines['left'].set_visible(False) 
ax4.tick_params(left=False, labelleft=False)
for ax in [ax2, ax3]:
    ax.spines['left'].set_visible(False)   # Oculta la línea del eje y
    ax.spines['right'].set_visible(False) 
    ax.tick_params(left=False, labelleft=False)  # Oculta las marcas y etiquetas del eje y

axes = [ax1, ax2, ax3, ax4]

# Graficar datos en cada subgráfico
for ax, (xmin, xmax) in zip(axes, x_limits):
    ax.plot(fech_doy, mean_cy, color="blue")
    ax.fill_between(fech_doy, dif_n, dif_p, color="lightblue")
    
    # Agregar los puntos en el eje secundario de cada gráfico
    ax_twin = ax.twinx()
    ax_twin.plot(fech_doy_lab, index_lab_copy, 'ro', markersize=20)
    ax_twin.set_ylim(-50, 317)
    
    # Ocultar las etiquetas y ticks del eje y derecho
    ax_twin.tick_params(labelcolor='none')  # Ocultar las etiquetas
    ax_twin.set_yticklabels([])  # Ocultar los ticks
    ax_twin.spines['top'].set_visible(False)
    ax_twin.spines['bottom'].set_visible(False)
    ax_twin.spines['left'].set_visible(False)
    ax_twin.spines['right'].set_visible(False)
    ax_twin.get_yaxis().set_visible(False)  

    # Ajustes de límite y formato de fecha
    ax.set_xlim(xmin, xmax)
    ax.xaxis.set_major_locator(MonthLocator(interval=1))
    ax.xaxis.set_major_formatter(month_fmt)
    
    # Rotar las etiquetas de los ticks
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)
    

# Ajustes de etiquetas y ticks
ax1.set_ylabel("PC$^μ$", fontsize=60)
ax1.tick_params(axis='both', which='major', labelsize=60)
ax2.tick_params(axis='both', which='major', labelsize=60)
ax3.tick_params(axis='both', which='major', labelsize=60)
ax4.tick_params(axis='both', which='major', labelsize=60)


ax4.text(2.30, 0.99, r'x$10^2$', transform=ax1.transAxes, fontsize=40, verticalalignment='top', color='red')

# Añadir las líneas diagonales de ruptura
d = 0.015  # Proporción de extensión de las líneas diagonales
kwargs = dict(marker=[(d, -1), (-d, 1)], markersize=40,
              linestyle="none", color='k', mec='k', mew=4, clip_on=False)
ax1.plot([1, 1], [0, 1], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 0], [0, 1], transform=ax2.transAxes, **kwargs)
ax2.plot([1, 1], [0, 1], transform=ax2.transAxes, **kwargs)
ax3.plot([0, 0], [0, 1], transform=ax3.transAxes, **kwargs)
ax3.plot([1, 1], [0, 1], transform=ax3.transAxes, **kwargs)
ax4.plot([0, 0], [0, 1], transform=ax4.transAxes, **kwargs)

# Etiqueta del eje y para el segundo eje
ax4_twin = ax4.twinx()
ax4_twin.set_ylabel("Concentration of Cyanobacteria [Cells ml$^{-1}$]", fontsize=60, color='red')
ax4_twin.set_ylim(-50, 317)
ax4_twin.tick_params(labelcolor='red', labelsize=40)
ax4_twin.spines['left'].set_visible(False)
ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()

# Guardar y mostrar el gráfico
fig.savefig("PC_index.png", dpi=300, bbox_inches='tight')
plt.show()



################################
#NDCI

##################################


#insitu

old                     = "C:/Users/gmart/Desktop/Scripts_paper_OPT4CYAN/2020-2024 Santa_Olalla fisicoqui.csv" #s abre de forma solo lectura
with open(old, "r") as doc:
    lines = doc.readlines()

# Procesar las líneas y dividirlas por ';'
linelist_lab = [line.strip().split(";") for line in lines]
linelist_lab=np.array(linelist_lab)

doy                      = linelist_lab[1:,0]
year                     = linelist_lab[1:,13]
mes                        = linelist_lab[1:,13]
chla                     = linelist_lab[1:,12]

x                        = np.where(chla!='')[0]
chla                    = chla[x].astype(float)
doy                      = doy[x]
year                     = year[x]

index_lab=chla
fech_doy_lab = np.zeros((0,1))
fech_doy_lab=[datetime.strptime(date_str, "%d/%m/%Y").date() for date_str in doy]




index_std_lab =  np.nanstd(index_lab)
dif_n_lab =index_lab - index_std_lab
dif_p_lab = index_lab + index_std_lab
dif_n_lab[(dif_n_lab < 0)] = 0
dif_n_lab[(dif_n_lab > 1)] = 1
dif_p_lab[(dif_p_lab < 0)] = 0
dif_p_lab[(dif_p_lab > 1)] = 1

fech_doy_lab=fech_doy_lab[6:]
index_lab=index_lab[6:]


#ndciiii

mean_c = np.zeros((0, 1))
std_c = np.zeros((0, 1))
for i in range(len(pc_d)):
    m = np.nanmean((chl_m[i] , chl2d_m[i] , chl2c_m[i] , chl_p[i] , chl2_p[i] , chla_oc4me[i] , chla_ndci[i] , chla_g08[i]))
    s = np.std((chl_m[i] , chl2d_m[i] , chl2c_m[i] , chl_p[i] , chl2_p[i] , chla_oc4me[i] , chla_ndci[i] , chla_g08[i]))
    mean_c = np.append(mean_c, [m])
    std_c = np.append(std_c, [s])

dif_n =mean_c - std_c
dif_p = mean_c + std_c
dif_n[(dif_n < 0)] = 0
dif_p=Smoo_filter(dif_p,1)
dif_p=Smoo_filter(dif_p,1)
dif_n[(dif_n > 1)] = 1
dif_p[(dif_p < 0)] = 0
dif_p[(dif_p > 1)] = 1
#create all plots
#Plots chla

#ndcci trios
ndci=ndci*-1
std_ndci = np.nanstd(ndci)
dif_n_ndci =(ndci) - std_ndci
dif_p_ndci = (ndci) + std_ndci



old                     = "C:/Users/gmart/Desktop/Scripts_paper_OPT4CYAN/Today_ndci.dat"

with open(old, "r") as doc:
    lines = doc.readlines()

# Procesar las líneas y dividirlas por ';'
linelist_ndci = [line.strip().split(";") for line in lines]
linelist_ndci=np.array(linelist_ndci)


doy_mean                      = linelist_ndci[1:,0].astype(float).astype(int).astype(str)
index_mean              = linelist_ndci[1:,1].astype(float)


index_mean=index_mean[92:]
doy_mean=doy_mean[92:]

#convertir la fecha
fech_doy_ndci = np.zeros((0,1))
i=0
while True:
    if i== len(doy_mean):
        break
    else:
        x=datetime.strptime(str(doy_mean[i][0:4]) + str(doy_mean[i][4:]), "%Y%j").strftime("%d-%m-%Y")
        fech_doy_ndci=np.append(fech_doy_ndci,x)
    i=i+1
  ###  
fech_doy_ndci = [datetime.strptime(date_str, "%d-%m-%Y").date() for date_str in fech_doy_ndci]




#r                       = index_mean[:][~np.isnan(index_mean[:])]
#index_mean                     = ((index_mean-np.nanmin(abs(index_mean)))/(np.nanmax(abs(r))-np.nanmin(abs(r))))



#dif_n_s[(dif_n_s < 0)] = 0
#dif_n_s[(dif_n_s > 1)] = 1
#dif_p_s[(dif_p_s < 0)] = 0
#dif_p_s[(dif_p_s > 1)] = 1


#smoo

def Smoo_filter (index:float,n:int)->float:
    import numpy as np
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

#index_mean=Smoo_filter(index_mean,1)
ndci_S=Smoo_filter(ndci,2)
std_ndci = np.nanstd(ndci_S)
dif_n_ndci =(ndci_S) - std_ndci
dif_p_ndci = (ndci_S) + std_ndci

index_nan=[0,9,10,11,12,13,20,21,22,23,24,27]
index_lab[index_nan]=np.nan
index_nan=[0,1,2,3,4,5,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,81,82,83,84,85,86,87,88,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128]
index_mean[index_nan]=np.nan
index_std =  np.nanstd(index_mean)
dif_n_s =index_mean - index_std
dif_p_s = index_mean + index_std




# Formato de fecha y rango mínimo y máximo
month_fmt = DateFormatter("%b %Y")
min_fecha = fech_doy[31]
max_fecha = np.max(fech_doy)

# Lista de límites en el eje x para cada subgráfico y su ancho proporcional
x_limits = [(fech_doy[0], fech_doy[215]), 
            (fech_doy[358], fech_doy[512]), 
            (fech_doy[682], fech_doy[830]), 
            (fech_doy[1030], fech_doy[1064])]

proporciones = [(xmax - xmin) / (max_fecha - min_fecha) for xmin, xmax in x_limits]

# Crear figura y GridSpec
fig = plt.figure(figsize=(50, 30))
gs = GridSpec(1, 4, width_ratios=proporciones, wspace=0.05)

# Crear subgráficos dentro del GridSpec
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1], sharey=ax1)
ax3 = fig.add_subplot(gs[2], sharey=ax1)
ax4 = fig.add_subplot(gs[3], sharey=ax1)
ax1.spines['right'].set_visible(False)
ax4.spines['left'].set_visible(False) 
ax4.tick_params(left=False, labelleft=False)
for ax in [ax2, ax3]:
    ax.spines['left'].set_visible(False)   # Oculta la línea del eje y
    ax.spines['right'].set_visible(False) 
    ax.tick_params(left=False, labelleft=False)  # Oculta las marcas y etiquetas del eje y

axes = [ax1, ax2, ax3, ax4]

# Graficar datos en cada subgráfico
for ax, (xmin, xmax) in zip(axes, x_limits):
    ax.plot(fech_doy, ndci_S , color="#055A02",label="In-situ Radiometry")
    ax.plot(fech_doy_ndci, index_mean, color="#35BC05",label="Satellite Radiometry")
    ax.fill_between(fech_doy_ndci, dif_n_s, dif_p_s, color="#45F906", alpha=0.5)
    ax.fill_between(fech_doy, dif_n_ndci, dif_p_ndci, color="#055A02", alpha=0.3)
    
    # Agregar los puntos en el eje secundario de cada gráfico
    ax_twin = ax.twinx()
    ax_twin.plot(fech_doy_lab, index_lab,  'ro', markersize=20, label="Water Sampling")
    ax_twin.set_ylim(-30, 160)
    
    # Ocultar las etiquetas y ticks del eje y derecho
    ax_twin.tick_params(labelcolor='none')  # Ocultar las etiquetas
    ax_twin.set_yticklabels([])  # Ocultar los ticks
    ax_twin.spines['top'].set_visible(False)
    ax_twin.spines['bottom'].set_visible(False)
    ax_twin.spines['left'].set_visible(False)
    ax_twin.spines['right'].set_visible(False)
    ax_twin.get_yaxis().set_visible(False)  

    # Ajustes de límite y formato de fecha
    ax.set_xlim(xmin, xmax)
    ax.xaxis.set_major_locator(MonthLocator(interval=1))
    ax.xaxis.set_major_formatter(month_fmt)
    
    # Rotar las etiquetas de los ticks
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)
    

# Ajustes de etiquetas y ticks
ax1.set_ylabel("NDCI", fontsize=40)
ax1.tick_params(axis='both', which='major', labelsize=60)
ax2.tick_params(axis='both', which='major', labelsize=60)
ax3.tick_params(axis='both', which='major', labelsize=60)
ax4.tick_params(axis='both', which='major', labelsize=60)


# Añadir las líneas diagonales de ruptura
d = 0.015  # Proporción de extensión de las líneas diagonales
kwargs = dict(marker=[(d, -1), (-d, 1)], markersize=40,
              linestyle="none", color='k', mec='k', mew=4, clip_on=False)
ax1.plot([1, 1], [0, 1], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 0], [0, 1], transform=ax2.transAxes, **kwargs)
ax2.plot([1, 1], [0, 1], transform=ax2.transAxes, **kwargs)
ax3.plot([0, 0], [0, 1], transform=ax3.transAxes, **kwargs)
ax3.plot([1, 1], [0, 1], transform=ax3.transAxes, **kwargs)
ax4.plot([0, 0], [0, 1], transform=ax4.transAxes, **kwargs)

# Etiqueta del eje y para el segundo eje
ax3_twin = ax3.twinx()
ax3_twin.spines['left'].set_visible(False)
ax3_twin.spines['right'].set_visible(False)
ax3_twin.tick_params(right=False, labelright=False)
ax4_twin = ax4.twinx()
ax4_twin.set_ylabel("Concentrantion of Chlorophyll-a [µg l$^{-3}$]", fontsize=60, color='red')
ax4_twin.set_ylim(-30, 160)
ax4_twin.tick_params(labelcolor='red', labelsize=40)
ax4_twin.spines['left'].set_visible(False)
ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
ax1.legend(loc='upper left', fontsize=40)
ax_twin.legend(loc='upper right', fontsize=40)

# Guardar y mostrar el gráfico
fig.savefig("NDCI.png", dpi=300, bbox_inches='tight')
plt.show()

