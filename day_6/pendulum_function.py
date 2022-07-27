#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 17:08:12 2022
@author: student
"""
__author__ = 'Hsiang-Chi Yeh'
__email__ = 'chi90125@gmail.com'

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def pendulum_free(x, t):
    l = 3
    g = 9.81
    x_dot = np.zeros(2)
    x_dot[0] = x[1]
    x_dot[1] = -g/l * np.sin(x[0])
    return x_dot

def pendulum_damped(x, t):
    l = 3
    g = 9.81
    damp = 0.3
    x_dot = np.zeros(2)
    x_dot[0] = x[1]
    x_dot[1] = -g/l * np.sin(x[0]) - damp*x[1]
    return x_dot

t0 = 0.0
tf = 15.5
n_point = 1000
x0 = np.array([np.pi/3, 0])
t = np.linspace(t0, tf, n_point)

solution_free = odeint(pendulum_free, x0, t)
solution_damp = odeint(pendulum_damped, x0, t)
fig, axs = plt.subplots(2, 1)
axs[0].plot(t, solution_free, '-', linewidth = 2)
axs[1].plot(t, solution_damp, '-', linewidth = 2)


#%%

def Lorenz63(x, t, o, p, B):
    xdot = np.zeros(3)
    xdot[0] = o*(x[1]-x[0])
    xdot[1] = x[0]*(p-x[2])-x[1]
    xdot[2] = x[0]*x[1]-B*x[2]
    return xdot

o = 10    
p = 28
B = 8/3
x0 = np.array([5, 5, 5])
t_in = 0
t_fin = 20
n_points = 1000
time = np.linspace(t_in, t_fin, n_points)

y = odeint(Lorenz63, x0, t, args=(o, p, B))
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.plot3D(y.T[0], y.T[1], y.T[2])

for ik in range (20):