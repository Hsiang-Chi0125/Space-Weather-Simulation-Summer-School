#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 13:57:28 2022

@author: student
"""

import numpy as np
import h5py
import matplotlib.pyplot as plt

import numpy as np
from scipy.io import loadmat

dir_density_Jb2008 = '/Users/student/Documents/data/JB2008/2002_JB2008_density.mat'

# Load Density Data
try:
    loaded_data = loadmat(dir_density_Jb2008)
    print (loaded_data)
except:
    print("File not found. Please check your directory")

# Uses key to extract our data of interest
JB2008_dens = loaded_data['densityData']

# The shape command now works
print(JB2008_dens.shape)

#%%
"""
Data visualization I
Let's visualize the density field for 400 KM at different time.
"""
# Import required packages
import matplotlib.pyplot as plt

# Before we can visualize our density data, we first need to generate the discretization grid of the density data in 3D space. We will be using np.linspace to create evenly sapce data between the limits.

localSolarTimes_JB2008 = np.linspace(0,24,24)
latitudes_JB2008 = np.linspace(-87.5,87.5,20)
altitudes_JB2008 = np.linspace(100,800,36)
nofAlt_JB2008 = altitudes_JB2008.shape[0] #36
nofLst_JB2008 = localSolarTimes_JB2008.shape[0] #24
nofLat_JB2008 = latitudes_JB2008.shape[0] #20

# We can also impose additional constratints such as forcing the values to be integers.
time_array_JB2008 = np.linspace(0,8760,20, dtype = int)
print(time_array_JB2008)
# For the dataset that we will be working with today, you will need to reshape them to be lst x lat x altitude
JB2008_dens_reshaped = np.reshape(JB2008_dens,(nofLst_JB2008,nofLat_JB2008,nofAlt_JB2008,8760), order='F') # Fortra-like index order
data_arr = np.random.randn(2,5)
print(data_arr)

print('The mean of all elements is: ',np.mean(data_arr))
print('The mean along the 0 axis is: ',np.mean(data_arr, axis = 0))

alt = 400
hi = np.where(altitudes_JB2008==alt)

fig, axs = plt.subplots(10, figsize=(15, 10*5), sharex = True)

for ik in range (10):
    cs = axs[ik].contourf(localSolarTimes_JB2008, latitudes_JB2008, JB2008_dens_reshaped[:,:,hi,time_array_JB2008[ik]].squeeze().T)
    axs[ik].set_title('JB2008 density at 400 km, t = {} hrs'.format(time_array_JB2008[ik]), fontsize=18)
    axs[ik].set_ylabel("Latitudes", fontsize = 18)
    axs[ik].tick_params(axis = 'both', which = 'major', labelsize = 16)
    
    cbar = fig.colorbar(cs, ax=axs[ik])
    cbar.ax.set_ylabel('Density')

axs[ik].set_xlabel("Local Solar Time", fontsize=18)    

#%%
"""
Assignment 1
Can you plot the mean density for each altitude at February 1st, 2002?
"""

# First identidy the time index that corresponds to  February 1st, 2002. Note the data is generated at an hourly interval from 00:00 January 1st, 2002
time_index = 251*24
dens_data_sep7 = JB2008_dens_reshaped[:,:,:,time_index]
JB2008_dens_sep7_alt=np.mean(np.mean(dens_data_sep7, axis=0), axis=0)
altitudes_JB2008

fig,ax = plt.subplots()
ax.plot(altitudes_JB2008, JB2008_dens_sep7_alt,c='Blue')
ax.set_xlabel('Altitude')
ax.set_ylabel('Density')
ax.set_title('Mean Density vs Altitude')
ax.grid(True)
plt.yscale('log')

#%%
"""
Data Visualization II
Now, let's us work with density data from TIE-GCM instead, and plot the density field at 310km
"""
# Import required packages
import h5py

loaded_data = h5py.File('/Users/student/Documents/data/TIEGCM/2002_TIEGCM_density.mat')

print('Key within database:',list(loaded_data.keys()))

tiegcm_dens = (10**np.array(loaded_data['density'])*1000).T
altitudes_tiegcm = np.array(loaded_data['altitudes']).flatten()
latitudes_tiegcm = np.array(loaded_data['latitudes']).flatten()
localSolarTimes_tiegcm = np.array(loaded_data['localSolarTimes']).flatten()
nofAlt_tiegcm = altitudes_tiegcm.shape[0]
nofLst_tiegcm = localSolarTimes_tiegcm.shape[0]
nofLat_tiegcm = latitudes_tiegcm.shape[0]

time_array_tiegcm = np.linspace(0,8760,20, dtype = int)
tiegcm_dens_reshaped = np.reshape(tiegcm_dens,(nofLst_tiegcm,nofLat_tiegcm,nofAlt_tiegcm,8760), order='F')

i = 100
alt = 310
hi = np.where(altitudes_tiegcm==alt)
fig, axs = plt.subplots(5, figsize=(15, 10*2), sharex=True)

for ik in range (5):
    cs = axs[ik].contourf(localSolarTimes_tiegcm, latitudes_tiegcm, tiegcm_dens_reshaped[:,:,hi,time_array_tiegcm[ik]].reshape(nofLst_tiegcm,nofLat_tiegcm).T)
    axs[ik].set_title('TIE-GCM density at 310 km, t = {} hrs'.format(time_array_tiegcm[ik]), fontsize=18)
    axs[ik].set_ylabel("Latitudes", fontsize=18)
    axs[ik].tick_params(axis = 'both', which = 'major', labelsize = 16)
    cbar = fig.colorbar(cs,ax=axs[ik])
    cbar.ax.set_ylabel('Density')

axs[ik].set_xlabel("Local Solar Time", fontsize=18) 

#%%
time_index = 31*24
dens_data_feb1 = JB2008_dens_reshaped[:,:,:,time_index]
JB2008_dens_feb1_alt=np.mean(np.mean(dens_data_feb1, axis=0), axis=0)
altitudes_JB2008

fig,ax = plt.subplots()
ax.plot(altitudes_JB2008, JB2008_dens_feb1_alt,c='Blue')
ax.set_xlabel('Altitude')
ax.set_ylabel('Density')
ax.set_title('Mean Density vs Altitude')
ax.grid(True)
plt.yscale('log')

loaded_data = h5py.File('/Users/student/Documents/data/TIEGCM/2002_TIEGCM_density.mat')

print('Key within database:',list(loaded_data.keys()))

tiegcm_dens = (10**np.array(loaded_data['density'])*1000).T
altitudes_tiegcm = np.array(loaded_data['altitudes']).flatten()
latitudes_tiegcm = np.array(loaded_data['latitudes']).flatten()
localSolarTimes_tiegcm = np.array(loaded_data['localSolarTimes']).flatten()
nofAlt_tiegcm = altitudes_tiegcm.shape[0]
nofLst_tiegcm = localSolarTimes_tiegcm.shape[0]
nofLat_tiegcm = latitudes_tiegcm.shape[0]

time_array_tiegcm = np.linspace(0,8760,20, dtype = int)
tiegcm_dens_reshaped = np.reshape(tiegcm_dens,(nofLst_tiegcm,nofLat_tiegcm,nofAlt_tiegcm,8760), order='F')

i = 100
alt = 310
hi = np.where(altitudes_tiegcm==alt)
fig, axs = plt.subplots(5, figsize=(15, 10*2), sharex=True)

for ik in range (5):
    cs = axs[ik].contourf(localSolarTimes_tiegcm, latitudes_tiegcm, tiegcm_dens_reshaped[:,:,hi,time_array_tiegcm[ik]].reshape(nofLst_tiegcm,nofLat_tiegcm).T)
    axs[ik].set_title('TIE-GCM density at 310 km, t = {} hrs'.format(time_array_tiegcm[ik]), fontsize=18)
    axs[ik].set_ylabel("Latitudes", fontsize=18)
    axs[ik].tick_params(axis = 'both', which = 'major', labelsize = 16)
    cbar = fig.colorbar(cs,ax=axs[ik])
    cbar.ax.set_ylabel('Density')

axs[ik].set_xlabel("Local Solar Time", fontsize=18) 

#%%
time_index = 31*24
tiegcm_dens_feb1 = tiegcm_dens_reshaped[:,:,:,time_index]
tiegcm_dens_feb1_alt = np.mean(np.mean(tiegcm_dens_feb1, axis=0), axis=0)
JB2008_dens_data_feb1 = JB2008_dens_reshaped[:,:,:,time_index]
JB2008_dens_feb1_alt=np.mean(np.mean(dens_data_feb1, axis=0), axis=0)

fig,ax = plt.subplots()
plt.subplots(1, figsize=(10, 6))
plt.semilogy(altitudes_tiegcm,tiegcm_dens_feb1_alt,linewidth = 2,label='TIE-GCM')
plt.semilogy(altitudes_JB2008,JB2008_dens_feb1_alt,'-.',linewidth = 2,label='JB2008')
plt.xlabel('Altitude', fontsize=18)
plt.ylabel('Density', fontsize=18)
plt.title('Mean Density vs Altitude', fontsize=18)
plt.grid()
plt.legend(fontsize=16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)



#%%
"""
Data Interpolation (1D)
Now, let's us look at how to do data interpolation with scipy
"""
# Import required packages
from scipy import interpolate

# Let's first create some data for interpolation
x = np.arange(0, 10)
y = np.exp(-x/3.0)
interp_func_1D = interpolate.interp1d(x, y)

xnew = np.arange(0, 9, 0.1)
ynew = interp_func_1D(xnew)   # use interpolation function returned by `interp1d`
plt.subplots(1, figsize=(10, 6))
plt.plot(x, y, 'o', xnew, ynew, '-',linewidth = 2)
plt.legend(['Inital Points','Interpolated line'], fontsize = 16)
plt.xlabel('x', fontsize=18)
plt.ylabel('y', fontsize=18)
plt.title('1D interpolation', fontsize=18)
plt.grid()
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

#%%