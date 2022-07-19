#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 13:39:19 2022

@author: student
"""
__author__ = 'Hsiang-Chi Yeh'
__email__ = 'chi90125@gmail.com'

from math import factorial
from math import pi
import numpy as np
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description = \
                                   'homework')
    parser.add_argument('-npts', \
                    help = 'number of points', type = int, default = 10)
    parser.add_argument('-x', \
                    help = 'angle', type = float, default = 3.1415)
    args = parser.parse_args()
    return args

def cos_approx(x, accuracy=10):
    def coeff(n):
        """Returns Taylor series coefficient of cosine"""
        return (-1)**n / factorial(2*n)

    series = [coeff(n) * x**(2*n) for n in range(accuracy)]
    return sum(series)

if __name__ == '__main__':  

    args = parse_args()
    x = args.x
    print('angle = ', x)
    npts = args.npts
    print("number of points = ", npts)

    def is_close(value, close_to, eta=1.e-2):
        """Returns True if the value is close to eta, or false otherwise"""
        return value > close_to-eta and value < close_to+eta
    
    approx = cos_approx(x, npts)
    actual = np.cos(x)
    print("approximate cos(x) = ", approx)
    print("actual cos(x) = ", actual)
    assert is_close(actual, approx), "They are not close!!!"
    
