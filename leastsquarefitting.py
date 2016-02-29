# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:31:32 2016

Trying to fit some data to a sine wave using least square method

@author: Galanodel
"""

from numpy import sin
from scipy import optimize
from math import pi
from matplotlib import pyplot as plt
from numpy import linspace
import math



# Data:
x = linspace(0, 10, 51)
y = (0.9,0.89755,0.89045,0.87939,0.86545,0.85,0.83455,0.82061,0.80955,0.80245,
     0.8,0.80245,0.80955,0.82061,0.83455,0.85,0.86545,0.87939,0.89045,0.89755,
     0.9,0.89755,0.89045,0.87939,0.86545,0.85,0.83455,0.82061,0.80955,0.80245,
     0.8,0.80245,0.80955,0.82061,0.83455,0.85,0.86545,0.87939,0.89045,0.89755,
     0.9,0.89755,0.89045,0.87939,0.86545,0.85,0.83455,0.82061,0.80955,0.80245,
     0.8)
new_x = linspace(0, 10, 1000)

# Locate the fit function:
fit = optimize.curve_fit

# Fit function:
def func(x, c, A, w, p):
    '''
    The function to be fitted with data.
        x ---  x value of the data;
        c ---  center of the sine function;
        A ---  amplitude of the sine func;
        w ---  angular frequency;
        p ---  phase shit;
    '''
    return c + A * sin(w * x + p)

# Do fitting without guess:
popt, pcov = fit(func, x, y)

# Do fitting with guess:
#maxdata = max(y)
#mindata = min(y)
#c_guess = (maxdata + mindata)/2
#A_guess = (maxdata - mindata)/2
#w_guess = 
guess = (1.5, 1, pi*5, pi/4)
popt2, pcov2 = fit(func,x, y, guess)

# get parameters:
c, A, w, p = popt
c2, A2, w2, p2 =popt2

#plot the origin graph:
#plt.subplot(2,1,1)

# Func closure used to generate function fitted to:
def sine(c, A, w, p):
    def f(x):
        return c + A * math.sin(w*x +p)
    return f
    
# plot the first fitting:
plt.subplot(2,1,1)
plt.plot(x, y, 'g-')
new_y = map(sine(c, A, w, p), new_x)
plt.plot(new_x, new_y, 'r.')

# plot the second fitting:
plt.subplot(2,1,2)
plt.plot(x, y, 'g-')
new_y = map(sine(c2, A2, w2, p2), new_x)
plt.plot(new_x, new_y, 'b.')

plt.show()


