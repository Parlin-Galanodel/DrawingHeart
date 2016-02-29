# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 19:48:38 2016

@author: Galanodel
"""
i = lambda x: x

def f(x):
	if x == 0:
		return 1
	else:
		return f(x-1)*x
		
		
		
def fact(x, c):
	if x == 0:
		return c(1)
	else:
		return c(fact(x-1, c)*x)
		
def factCPS(n):
    def f(n, k):
        if n == 0:
            return k(1)
        else:
            return f(n - 1, lambda x: k(n * x))
    return f(n, i)
	
if __name__ == '__main__':
	print f(4)
	print fact(4, id)
	print factCPS(4)
	print
	print f(7)
	print fact(7, id)
	print factCPS(7)
	
	