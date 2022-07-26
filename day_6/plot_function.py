#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 11:46:53 2022

@author: student
"""

__author__ = 'Hsiang-Chi Yeh'
__email__ = 'chi90125@gmail.com'

import numpy as np
import matplotlib.pyplot as plt

def fun(x):
    return (np.cos(x) + x*np.sin(x))

def function(x):
    return x*np.cos(x)

x_in = -6
x_fin = -x_in
n_points = 1000
x = np.linspace(x_in, x_fin, n_points)

plt.plot(fun(x), '-')
plt.plot(function(x), '-')
plt.xlabel('x', fontsize=12)


#%%
h = 0.25
arr_x = np.array([])
arr_der = np.array([])

def derivation(x, h):
    return (fun(x+h)-fun(x))/h

x0 = -6
while x0 <= x_fin:
    arr_der = np.append(arr_der, derivation(x0, h))
    x0 = x0+h
    arr_x = np.append(arr_x, x0)

plt.plot(arr_x, arr_der)

#%%
h = 0.25
arr_x = np.array([])
arr_der = np.array([])

def derivation(x, h):
    return (fun(x-h)-fun(x))/h

x1 = 6
while x1 <= x_fin:
    arr_der = np.append(arr_der, derivation(x1, h))
    x1 = x1-h
    arr_x = np.append(arr_x, x1)
    
plt.plot(arr_x, arr_der)

#%%
h = 0.25
arr_x = np.array([])
arr_der = np.array([])

def derivation(x, h):
    return (fun(x+h)-fun(x-h))/(2*h)

def function(x):
    return x*np.cos(x)
    
x0 = -6
while x0 <= x_fin:
    arr_der = np.append(arr_der, derivation(x0, h))
    x0 = x0+h
    arr_x = np.append(arr_x, x0)

plt.grid()
plt.plot(arr_x, arr_der)
plt.plot(x, function(x), '-b')
plt.xlabel('x', fontsize=12)
plt.legend([r'$\dot y$ truth', r'$\dot y$ forward', r'$\dot y$ backward',r'$\dot y$ central'])