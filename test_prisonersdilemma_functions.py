# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:59:51 2020

@author: katha
"""

import unittest
from prisonersdilemma import run
'''
This is a function that tracks the sentence count in the prisoner's dilemma game.
I'm gonna test it by setting sentcounto and sentcountp to 0 and then setting response == 'right'
and oppstrategy == 'defect' to see if it calculates the sentence correctly.


Information for the person who grades this: I copied the function instead of importing it because
I wasn't 100% sure about how everything works (and it's already shortly before the deadline now) 
and decided to test the function like that,
just to be sure. I included the code from the tutorial anyways. Hope that's okay.
'''

def sentencetracker(sentcounto, sentcountp, response, oppstrategy):
    if response == 'right' and oppstrategy == 'cooperation': #both cooperate
        sentcountp -= 3
        sentcounto -= 3
    elif response == 'right' and oppstrategy == 'defect': #participant wants to cooperate,  but opponent rats them out
        sentcountp -= 5
    elif response == 'left' and oppstrategy == 'cooperation': #participant rats opponent out, but opponent cooperates
        sentcounto -= 5
    else: #response == 'left' & oppstrategy == 'defect': #both defect
        sentcountp -= 1
        sentcounto -= 1
    return sentcounto, sentcountp


response = 'right'
oppstrategy = 'defect'
sentcountp = 0
sentcounto = 0
#sentcounto should be 0 and sentcountp should be -5

sentcounto, sentcountp = sentencetracker(sentcounto, sentcountp, response, oppstrategy) 

print(sentcounto)
print(sentcountp)



class testfunctionsdilemma(unittest.TestCase):
	
	def test_sentencetracker(self):
		obj = sentencetracker(sentcounto, sentcountp, response, oppstrategy)
		response = 'right'
		oppstrategy = 'defect'

		self.assertEqual(sentcounto, 3)
		self.assertEqual(sentcountp, 3)
		
		
if __name__ == '__main__':
	unittest.main()
