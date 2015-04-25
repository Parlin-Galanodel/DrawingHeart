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

        points = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J',
                  'Q', 'K']

        deck=[]

        for i in points:
            for j in suits:
                k = j + ' ' + i
                deck.append(k)

        return deck
        
        
    def shuffle(self):
        random.shuffle(self.__deck)
        
        
    def deal_card(self):
        return self.__deck.pop()
        
    
    def amount(self):
        return len(self.__deck)
        
    
    
if __name__ == '__main__':
    
    deck = Deck()
    deck.shuffle()
    
    def primefunc():
            x = []
            for i in xrange(4):
                x.append(deck.deal_card())
            return x
    
    
    def question():
        print primefunc()
        print 'please give an answer'
        
    def answer():
        ans = raw_input()
        x = eval(ans)
        return x
        
        
    def game():
        question()
        x = answer()
        
        while x != 24:
            print 'wrong answer %d, please try again' % x
            x = answer()
            
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
            
    while deck.amount() >=4:
        x = game()
        if x is None:
            break