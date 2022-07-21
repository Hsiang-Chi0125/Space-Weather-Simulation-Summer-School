#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 17:19:41 2022

@author: student
"""

__author__ = 'Hsiang-Chi Yeh'
__email__ = 'chi90125@gmail.com'


import matplotlib.pyplot as plt
import numpy as np

def spherical_cartesian(radius, azimuth, zentith):
    """Convert spherical coordinates to cartesian"""
    x = radius*np.sin(zentith)*np.cos(azimuth)
    y = radius*np.sin(zentith)*np.cos(azimuth)
    z = radius*np.cos(zentith)
    return {'x':x, 'y':y, 'z':z}
   
fig = plt.figure()
axes = fig.gca(projection='3d')
r = np.linspace(0, 1)
theta = np.linspace(0, 2*np.pi)
phi = np.linspace(0, 2*np.pi)
coords = spherical_cartesian(r, theta, phi)
axes.plot(coords['x'], coords['y'], coords['z'])
