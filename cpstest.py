# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 08:07:07 2015

@author: Galanodel
"""
# cps test

from time import clock

def timeit(func):
    def t(*argus):
        start = clock()
        func(*argus)
        end = clock()
        return end - start
    return t
    
@timeit
def fact(x):
    if x == 0:
        return 1
    else:
        return x*fact(x-1)
        
@timeit
def fact_cps(x,k):
    if x==0:
        return k(1)
    else:
        return fact_cps(x-1, lambda n: k(n*x))
        
if __name__ == '__main__':
    for i in xrange(10, 110, 10):
        print fact(i), '\n',
        print fact_cps(i,lambda x:x), '\n',
        print '\n'