# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 18:08:48 2015

@author: Galanodel
"""

# Trying on lazy evaluation without generator

class My_xrange(object):
    ''' The first idea comes to my head is that, I could simulate a stream-like
    thing and it is merely a delayed sequence. So I decide to write a xrange
    object  or generator without using the python iterator protocal'''
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start
        
    def next(self):
        self.current += self.stop
        return self.
        
