# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 07:38:37 2016

@author: Galanodel
"""

from numpy import linspace
from math import pi, cos, e
from matplotlib import pyplot as plt

x = linspace(0, 500, 10000)
w1 = pi / 10
w2 = pi / 11

def o1(x):
    return cos(w1*x)
    
def o2(x):
    return cos(w2*x)
    
def o(x):
    return 2*cos((w1+w2)/2.*x)*cos((w1-w2)/2.*x)

def f(A, a):
    return lambda x: A*e**(-1.* a * x)
    
#y = map(f(10, 0.02), x)
#y1 = map(f(10, 0.5), x)
#y2 = map(f(20, 0.02), x)
#
#plt.plot(x,y,'r-')
#plt.plot(x,y1,'g.')
#plt.plot(x,y2,'b.')
#plt.show()    
#    
    
y1 = map(o1, x)
y2 = map(o2, x)
y = map(o, x)

plt.subplot(3,1,1)
plt.plot(x, y1, 'r-')
plt.subplot(3,1,2)
plt.plot(x, y2, 'b-')
plt.subplot(3,1,3)
plt.plot(x, y, 'g-')
plt.show()