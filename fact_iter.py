# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 10:58:18 2016

@author: Galanodel
"""

def fact(number, product = 1, counter = 1):
	if counter == number:
		return product
	else:
		counter += 1
		product *= counter
		return fact(number, product, counter)