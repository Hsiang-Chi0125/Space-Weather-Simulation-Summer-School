#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:52:26 2022

@author: student
"""

f = open("/Users/student/Documents/Space-Weather-Simulation-Summer-School/day_5/omni_min_def_CiPTLs5DUH.lst")
f.close()

import numpy as np
import datetime as dt
import argparse
import matplotlib.pyplot as plt

def read_ascii_file(filename, index = -1):
    with open(filename) as f:

        data_dic = {"time":[], "year":[], "day":[], "hour":[], "minute":[], "symh":[]}
        
        for line in f:
            tmp = line.split()
            
            time0 = dt.datetime(int(tmp[0]),1,1,int(tmp[2]),int(tmp[3]),0)\
                                      + dt.timedelta(days=int(tmp[1])-1)     
            data_dic["time"].append(time0)
            data_dic["year"].append(int(tmp[0]))
            data_dic["day"].append(int(tmp[1]))
            data_dic["hour"].append(int(tmp[2]))
            data_dic["minute"].append(int(tmp[3]))
            data_dic["symh"].append(int(tmp[4]))
                    
    return data_dic

def parse_args():
    parser = argparse.ArgumentParser(description = 'homework')
    parser.add_argument('-filename', \
                    help = 'filename', type = str, default = "output")
    parser.add_argument('-output_filename',\
                    help = 'output_filename', type = str, default = "output")
    args = parser.parse_args()
    return args

args = parse_args()
filename = args.filename
output_filename = args.output_filename
print('filename = ', filename)
print('output_filename = ', output_filename)

time1 = dt.datetime(2002, 5, 1, 15, 30)
print(time1.date())
  
#filename='/Users/student/Documents/Space-Weather-Simulation-Summer-School/day_2/omni_min_def_20130316.lst'
index = 4
data = read_ascii_file(filename, index)
time = np.array(data["time"])
data1 = np.array(data["symh"])

fig,ax = plt.subplots()
ax.plot(time,data1,marker='.',c='gray',
        label='All Events',alpha=0.5)

print(time)
lp = data1 < -100
print(lp)
ax.plot(time[lp], data1[lp],marker='+',
        linestyle='', c='tab:orange',
        label='<-100 nT',alpha=0.6)

ax.set_xlabel('Year of 2002')
ax.set_ylabel('SYMH (nT)')
ax.grid(True)
ax.legend()
        
#outfile ='plot20130316.png'
plt.savefig(output_filename)
plt.close()
