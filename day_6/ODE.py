#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 15:10:06 2022

@author: student
"""
__author__ = 'Hsiang-Chi Yeh'
__email__ = 'chi90125@gmail.com'

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def RHS(y, t):
    return -2*y

h = 0.2
y0 = 3
t0 = 0
tf = 2

time = np.linspace(t0, tf)
y_true = odeint(RHS, y0, time)

fig1 = plt.figure()
plt.plot(time, y_true, 'k-', linewidth = 2)
plt.grid()
plt.xlabel('time')
plt.ylabel('sy(t)s')
plt.legend('Truth')

#%%
timeline = np.array([t0])
sol_rk1 = np.array([y0])

while t0 < tf-h:
    slope = RHS(y0, t0)
    y1 = y0 + slope * h
    
    t1 = t0 + h
    timeline = np.append(timeline, t1)
    sol_rk1 = np.append(sol_rk1, y1)
    
    t0 = t1
    y0 = y1
    
plt.plot(timeline, sol_rk1, '-o', linewidth = 1.5)    

#%%

h = 0.2
t0 = 0
y0 = 3
tf = 2

timeline = np.array([t0])
sol_rk1 = np.array([y0])

while t0 < tf-h:
    slope1 = RHS(y0, t0)
    slope2 = RHS(y0 + (h/2) * slope1, t0 + (h/2))
    y1 = y0 + h * slope2
    
    t1 = t0 + h
    timeline = np.append(timeline, t1)
    sol_rk1 = np.append(sol_rk1, y1)
    
    t0 = t1
    y0 = y1
    
plt.plot(timeline, sol_rk1, 'b-o', linewidth = 1.5)

#%%
h = 0.2
t0 = 0
y0 = 3
tf = 2

timeline = np.array([t0])
sol_rk1 = np.array([y0])

while t0 < tf-h:
    k1 = RHS(y0, t0)
    k2 = RHS(y0 + (h/2) * k1, t0 + (h/2))
    k3 = RHS(y0 + (h/2) * k2, t0 + (h/2))
    k4 = RHS(y0 + h * k3, t0 + h)
    y1 = y0 + (k1 + 2*k2 + 2*k3 + k4) * h/6
    
    t1 = t0 + h
    timeline = np.append(timeline, t1)
    sol_rk1 = np.append(sol_rk1, y1)
    
    t0 = t1
    y0 = y1
    
plt.plot(timeline, sol_rk1, 'r-o', linewidth = 1.5)
plt.legend(['Truth', 'Runge-Kutta 1', 'Runge-Kutta 2', 'Runge-Kutta 4'])
    
