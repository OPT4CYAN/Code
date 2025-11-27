# -*- coding: utf-8 -*-
"""
@author:             Gonzalo M.F. 
Gonzalo Martínez-Fornos
gmartinez@icm.csic.es
Research institute:  ICM-CSIC 
Collaboration:       EBD-CSIC 
"""


import pandas as pd
import matplotlib.pyplot as plt 
import functions as fn
import numpy as np
from matplotlib.ticker import MaxNLocator

def plot_run (output_dir, site):
    with open(output_dir +site+ "_pcu_chl_index.dat", "r") as index_doc:
        pcu_chl = index_doc.readlines()
    pcu_chl  = pd.DataFrame([line.strip().split(";") for line in pcu_chl ])
    pcu_chl.columns =  pcu_chl.iloc[0]
    pcu_chl  =  pcu_chl[1:].reset_index(drop=True)
    with open(output_dir + "sentinel_ndci.dat", "r") as index_doc:
        sen_ndci = index_doc.readlines()
    sen_ndci  = pd.DataFrame([line.strip().split(";") for line in sen_ndci ])
    sen_ndci.columns =  sen_ndci.iloc[0]
    sen_ndci  =  sen_ndci[1:].reset_index(drop=True)
    
    #day filter and fech change
    pcu_chl_array        =pcu_chl.to_numpy()[:,3:].astype(float)
    doy_unique           = np.unique(pcu_chl['ID'])
    pcu_chl_unique       = []
    pcu_chl_std          = []
    for i in doy_unique:
        tmp= np.where(i == pcu_chl['ID'])[0]
        pcu_chl_unique.append(np.nanmean(pcu_chl_array[tmp],axis=0))
        pcu_chl_std.append(np.nanstd(pcu_chl_array[tmp],axis=0))
    pcu_chl_unique           = np.array(pcu_chl_unique)
    pcu_chl_std           = np.array(pcu_chl_std)
    date_pcu_chl             = []
    for i in doy_unique:
        date_pcu_chl.append(fn.doy_to_date(int(i)))
    
    
    sen_ndci_array        =sen_ndci.to_numpy().astype(float)
    doy_unique           = np.unique(sen_ndci['Doy'])
    sen_ndci_unique       = []
    sen_ndci_std          = []
    for i in doy_unique:
        tmp= np.where(i == sen_ndci['Doy'])[0]
        sen_ndci_unique.append(np.nanmean(sen_ndci_array[tmp],axis=0))
        sen_ndci_std.append(np.nanstd(sen_ndci_array[tmp],axis=0))
    sen_ndci_unique           = np.array(sen_ndci_unique)
    sen_ndci_std           = np.array(sen_ndci_std)
    date_sen_ndci             = []
    for i in doy_unique:
        date_sen_ndci.append(fn.doy_to_date(int(i)))
    
    fig  = plt.figure(figsize=(50, 30))
    ax                      =fig.add_axes([0.1,0.1,0.8,0.8])
    ax.plot(date_pcu_chl,pcu_chl_unique[:,0],color="blue",label="Pcu insitu")
    ax.plot(date_pcu_chl,pcu_chl_unique[:,1],color="green",label="Chl insitu")
    ax.fill_between(date_pcu_chl, pcu_chl_unique[:, 0] - pcu_chl_std[:,0], pcu_chl_unique[:, 0] + pcu_chl_std[:,0], color="blue", alpha=0.7)
    ax.fill_between(date_pcu_chl,pcu_chl_unique[:, 1] - pcu_chl_std[:,1],pcu_chl_unique[:, 1] + pcu_chl_std[:,1],color="green", alpha=0.7)
    num_ticks = min(len(date_pcu_chl), 20)  
    ax.xaxis.set_major_locator(MaxNLocator(nbins=num_ticks, integer=False))
    if len(date_pcu_chl) > 10:
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    else:
        plt.setp(ax.get_xticklabels(), rotation=0, ha='center')
    ax.tick_params(axis='both', labelsize=40)
    ax.grid(True)
    plt.legend(loc='upper left', fontsize=40)
    plt.tight_layout() 
    plt.show()
    fig.savefig(output_dir+"pcu_vs_chl.jpg",dpi=300)
    plt.close(fig)
    
    fig  = plt.figure(figsize=(50, 30))
    ax                      =fig.add_axes([0.1,0.1,0.8,0.8])
    ax.plot(date_pcu_chl,pcu_chl_unique[:,2],color="red",label="ndci insitu")
    ax.plot(date_sen_ndci,sen_ndci_unique[:,1],color="black",label="ndci Sentinel",marker='o',markersize=30)
    ax.fill_between(date_pcu_chl, pcu_chl_unique[:, 2] - pcu_chl_std[:,2], pcu_chl_unique[:, 2] + pcu_chl_std[:,2], color="red", alpha=0.7)
    num_ticks = min(len(date_pcu_chl), 20)  
    ax.xaxis.set_major_locator(MaxNLocator(nbins=num_ticks, integer=False))
    if len(date_pcu_chl) > 10:
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    else:
        plt.setp(ax.get_xticklabels(), rotation=0, ha='center')
    ax.tick_params(axis='both', labelsize=40)
    ax.grid(True)
    plt.legend(loc='upper left', fontsize=40)
    plt.tight_layout() 
    plt.show()
    fig.savefig(output_dir+"ndci.jpg",dpi=300)
    plt.close(fig)
    
    
    
    