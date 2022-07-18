#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 17:04:00 2022

@author: student
"""
__author__ = 'Hsiang-Chi Yeh'
__email__ = 'chi90125@gmail.com'

from datetime import datetime
from swmfpy.web import get_omni_data
import matplotlib.pyplot as plt

start_time = datetime(2001, 1, 25)
end_time = datetime(2001, 1, 25)
data = get_omni_data(start_time, end_time)  # returns a dictionary
data.keys()


AL=list(data['al'])
plt.plot(AL)
plt.show()