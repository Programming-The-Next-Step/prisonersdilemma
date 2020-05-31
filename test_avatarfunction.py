# -*- coding: utf-8 -*-
"""
Created on Sat May 30 20:44:12 2020

@author: katha
"""


'''
Here we assign the conditions and make sure that the right avatars are displayed, based on the participant`s avatar
and the condition assigned. They way this is written, you should easily be able to customise which conditions
you want to use based on which avatars. This might seem like unnecessary complicated code, but it makes transparent
how the conditions relate to the avatars.
'''
from psychopy.visual import Window, TextStim, ImageStim
DISPSIZE = (1000,900)
#in case that doesn't work, use DISPSIZE = (1000,700)
#for windows only DISPSIZE = (GetSystemMetrics(0),GetSystemMetrics(1))
BGC = 'white'
win = Window(size=DISPSIZE, units='pix', color=BGC, fullscr=False)
opponent = ImageStim(win, image='opponent2.png', pos=(300, 000)) #placeholder
participant = ImageStim(win, image='partA.png', pos=(-300, 000)) #placeholder

def avatarassignment(opponent, participant, condition, response):
	if condition == 1: #playing with an in-group member
		if response == 'a': #participant is female caucasian
			opponent.setImage("opponent2.png")
			participant.setImage("partA.png") 
		elif response == 'c': #participant is male caucasian 
			opponent.setImage("opponent2.png")
			participant.setImage("partC.png") 
		elif response == 'b': #participant is female non-caucasian
			opponent.setImage("opponent1.png") 
			participant.setImage("partB.png")
		elif response == 'd': #option d, participant is male non-caucasian
			opponent.setImage("opponent1.png") 
			participant.setImage("partD.png")
		print('in-group condition')
	
	if condition == 2: #playing with an out-group member
		if response == 'a': #participant is female caucasian
			opponent.setImage("opponent1.png")
			participant.setImage("partA.png") 
		elif response == 'c': #participant is male caucasian 
			opponent.setImage("opponent1.png")
			participant.setImage("partC.png") 
		elif response == 'b': #participant is female non-caucasian
			opponent.setImage("opponent2.png") 
			participant.setImage("partB.png")
		elif response == 'd': #option d, participant is male non-caucasian
			opponent.setImage("opponent2.png") 
			participant.setImage("partD.png")
		print('out-group condition')
	
	if condition == 3: #playing with no information about opponent
		opponent.setImage("anonymous.jpg")
		if response == 'a': #participant is female caucasian
			participant.setImage("partA.png") 
		elif response == 'c': #participant is male caucasian 
			participant.setImage("partC.png") 
		elif response == 'b': #participant is female non-caucasian
			participant.setImage("partB.png")
		elif response == 'd': #option d, participant is male non-caucasian
			participant.setImage("partD.png")
		print('anonymous condition')
		
		return opponent, participant
	
condition = 1
response = 'a'
opponent, participant = avatarassignment(opponent, participant, condition, response)
participant.draw()
opponent.draw()