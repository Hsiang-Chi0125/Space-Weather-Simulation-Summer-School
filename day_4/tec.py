#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 12:38:29 2022

@author: student
"""
__author__ = 'Hsiang-Chi Yeh'
__email__ = 'chi90125@gmail.com'

import netCDF4 as nc
import matplotlib.pyplot as plt
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description = 'homework')
    parser.add_argument('-infilename', nargs = "+", help = 'infilename', type = str, default = "output")
    args = parser.parse_args()
    return args

def plot_tec(lons, lats, tec, figsize=(12,6)):
    fig, ax = plt.subplots(1, figsize=(12, 6))
    ax1=ax.pcolormesh(lons, lats, tec)
    ax.set_xlabel('Lontitude')
    ax.set_ylabel('Latitude')
    ax.set_title('20220721 TEC')
    plt.colorbar(ax1, ax=ax)
    return fig, ax

dataset = nc.Dataset('/Users/student/Documents/ionosphere forecast data/wfs.t12z.ipe05.20220721_000000.nc')

tec = dataset['tec'][:]  # How you get the numpy array of the data
lons = dataset['lon'][:] 
lats = dataset['lat'][:] 
dataset['tec'].units  # How you get the units of data

print(dataset)

fig, ax = plot_tec(lons, lats, tec)

if __name__ == '__main__':  
    args = parse_args()
    infilename = args.infilename
    output_filename = infilename + '.png'
    plt.savefig(output_filename)
    plt.close()
    
    print('inputfile = ', infilename)
    print('outputfile = ', output_filename)
    