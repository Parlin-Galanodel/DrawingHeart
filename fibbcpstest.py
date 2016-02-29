# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 08:33:39 2015

@author: Galanodel
"""

def fibb(n):
    if n==1 or n==2:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)
        
def fcps(n, k):
    if n ==1 or n==2:
        return k(1)
    else:
#        print n
        return fcps(n-1, lambda x: (x + fcps(n-2,k)))

def f(n,k):
	if n == 1 or n == 2:
		return k(1)
	else:
		return k(f(n-1,k)+f(n-2,k))
		
		
if __name__=='__main__':
	print fibb(7)
	print fcps(7,lambda x: x)
	print f(7, lambda x: x)
    