# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 22:46:19 2015

@author: Galanodel
"""

import random

class Deck(object):
    '''
    this class is simulation of deck.
    '''
    
    def __init__(self):
        '''
        initial method, the deck is hidden and so no one could cheat,
        i guess
        '''
        self.__deck = Deck.deckgenerator()


    @staticmethod
    def deckgenerator():
        '''
        static method used to generate a brandnew deck of playing cards
        '''
        suits = ['diamond', 'club', 'spade', 'heart']

        points = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                  'J', 'Q', 'K']

        deck=[]

        for i in points:
            for j in suits:
                k = j + ' ' + i
                deck.append(k)

        return deck
        
        
    def shuffle(self):      # shuffle the brand new deck 
        random.shuffle(self.__deck)
        
        
    def deal_card(self):
        return self.__deck.pop()
        
    
    def amount(self):       # an interface to get the number of cards 
                            # left in this deck
        return len(self.__deck)
        
        
        
def primefunc():        #prime function used to get 4 cards
    x = []
    for i in xrange(4):
        x.append(deck.deal_card())
    return x
    
    
# def a dictionary to look up points a card represents
points = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
          'J', 'Q', 'K']
d={}
for i,j in enumerate(points, 1):
    d[j] = int(i)
    
def question():         # throw the question out
    num = primefunc()   # a list of 4 cards
    print num
    num = [i[-1] for i in num]
    if '0' in num:
        num.remove('0')
        num.append('10')
    i, j, k, l = [d[i] for i in num]    # the points indicate the
                                            # the number it represents
    print 'corresponding numbers are', i, j, k, l
    print 'please give an answer or press enter to see answers'
    return i, j, k, l
    
    
def solve(i, j, k, l):
    '''
    this function solves a problem and could return solutions
    this code borrowed from http://v5b7.com/python/python_24.html#sec-1
    '''
    arr=[i, j, k, l]

    def perm(items, n=None):
        if n is None:
            n = len(items)
        for i in range(len(items)):
            v = items[i:i+1]
            if n == 1:
                yield v
            else:
                rest = items[:i] + items[i+1:]
                for p in perm(rest, n-1):
                    yield v + p
    
    def F(a,b):
        arr={}
        for i in a:
            for j in b:
                va=a[i]
                vb=b[j]
                arr.update({"("+i+"+"+j+")":va+vb})
                arr.update({"("+i+"-"+j+")":va-vb})
                arr.update({"("+j+"-"+i+")":vb-va})
                arr.update({"("+i+"*"+j+")":va*vb})
                vb>0 and arr.update({"("+i+"/"+j+")":va/vb})
                va>0 and arr.update({"("+j+"/"+i+")":vb/va})
        return arr
    
    for i in perm(arr):
        dic=[{"a":i[0]},{"b":i[1]},{"c":i[2]},{"d":i[3]}]
        alist=F(F(F(dic[0],dic[1]),dic[2]),dic[3])
        blist=F(F(dic[0],dic[1]),F(dic[2],dic[3]))
        for i in alist:
            if alist[i]==24.0:
                print i.replace('a',str(dic[0]['a'])).\
                replace('b',str(dic[1]['b'])).replace\
                ('c',str(dic[2]['c'])).replace('d',str(dic[3]['d']))
        for i in blist:
            if blist[i]==24.0:
                print i.replace('a',str(dic[0]['a'])).\
                replace('b',str(dic[1]['b'])).replace\
                ('c',str(dic[2]['c'])).replace('d',str(dic[3]['d']))

    
    
    
    
def answer(i, j, k, l):           # ask users for an answer 
    ans = raw_input()
    try:
        x = eval(ans)
        return x
    except NameError:
        print 'invalid input, please enter a formula'
        return answer(i, j, k, l)
    except SyntaxError:
        solve(i, j, k, l)  # answer would be called after question,
                            # i,j,k,l would be defined 
        return game()
    
    
def game():
    i, j, k, l = question()
    x = answer(i, j, k, l)
    
    while x != 24 and ((type(x) is int) or (type(x) is float)):
        print 'wrong answer %d, please try again' % x
        x = answer(i, j, k, l)
        
    if x == 24:
        print 'continue chanlange(y/n)'
        
        def tempfunc():
            response = raw_input()
            if response in ('yes', 'Yes', 'YES', 'y', 'Y'):
                return game()
                    
            elif response in ('no', 'NO', 'No', 'n', 'N'):
                return
                
            else:
                print 'not valid option, please try again.'
                return tempfunc()
                
        return tempfunc()


    
if __name__ == '__main__':
    '''
    the input is valid to be either a formula or a number and this results
    in a buggy situation since 24 would be always seen as correct answer.
    I keep this for debugging in case the problem is too hard    
    '''
    deck = Deck()
    deck.shuffle()
    amount = deck.amount()

    try:
        game()
    except IndexError:
        print 'CONGRATULATIONS! you have finished this deck!'