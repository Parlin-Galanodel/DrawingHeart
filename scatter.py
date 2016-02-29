# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 07:01:21 2016

@author: Galanodel
"""
import numpy as np
from matplotlib import pyplot as plt
from math import sin
from scipy import optimize


def sine(x, center, amplitude, angularf, phase):
    return center + amplitude * np.sin(angularf * x + phase)


para =(0.8999835458658402,
0.01815980098337701,
-0.0739594555770137,
-0.03462543991969243,
0.060077614379157485,
-0.023140522875836716,
0.003962418300656491,
-3.1979458450068535E-4,
9.92063492064156E-6)

def f(x):
    return para[0] + para[1] * x + para[2] * x**2 + para[3] * x**3 \
    + para[4] * x**4 + para[5] * x**5 + para[6]* x**6 + para[7] * x**7 \
    +para[8] * x**8
    
#for i in xrange(11):
#    print f(i)
    
data = (0.9,0.85,0.8,0.85,0.9,0.85,0.8,0.85,0.9,0.85,0.8)

fit = optimize.curve_fit
print fit(sine, range(11), data)