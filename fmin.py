# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:26:22 2016

sine fitting with downhill simplex mehod

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
sigma = map(lambda x: 0.05*x, y)

# Locate the fit method:
## "fmin" is not a sensible name for an optimisation package.
### Rename fmin to "fit" (this fitting used downhill simplex method)
fit = optimize.fmin

# Powell's method
fit_powell = optimize.fmin_powell

# Fit function:
def func(params, x, y, Err):
    '''
    Define the objective function to be minimised by Simplex.
    x      ... array holding x-positions of observed data.
    y      ... array holding y-values of observed data.
    Err    ... array holding errors of observed data.
    '''
    # extract current values of fit parameters from input array
    c = params[0]
    A = params[1]
    w = params[2]
    p = params[3]
    # compute chi-square
    chi2 = 0.0
    for n in range(len(x)):
        x_sample = x[n]
        # The function y(x)=a+b*x+c*x^2 is a polynomial
        # in this example.
        y_esti = c + A * sin(w * x_sample + p)
        chi2 = chi2 + (y[n] - y_esti) * (y[n] - y_esti) / (Err[n] * Err[n])
    return chi2

initial_guess = (1, 1, 1, 1)
initial_guess2 = (1, 1, 1, 1)
c, A, w, p = fit(func, initial_guess, args=(x, y, sigma))
c2, A2, w2, p2 = fit_powell(func, initial_guess2, args=(x, y, sigma))

##plot the origin graph:
#plt.plot(x, y, 'g-')

# Func closure used to generate function fitted to:
def sine(c, A, w, p):
    def f(x):
        return c + A * math.sin(w*x +p)
    return f
    
# plot the first fitting:
new_y = map(sine(c, A, w, p), new_x)
new_y2 = map(sine(c2, A2, w2, p2), new_x)
plt.subplot(2,1,1)
plt.plot(x, y, 'g-')
plt.plot(new_x, new_y, 'r.')
plt.subplot(2,1,2)
plt.plot(x, y, 'g-')
plt.plot(new_x, new_y2, 'b.')

plt.show()