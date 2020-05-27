# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:37:28 2020

@author: katha
"""
'''
These are th modules used for this experiment.
'''


from psychopy.visual import Window, TextStim, ImageStim
from psychopy.core import wait
from psychopy.event import getKeys, waitKeys
from numpy.random import shuffle
from psychopy import gui
import numpy as np
import random
from win32api import GetSystemMetrics
import ctypes

def run:
	#create window
	user32 = ctypes.windll.user32
	DISPSIZE = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
	#in case that doesn't work, use DISPSIZE = (1000,700)
	#for windows only DISPSIZE = (GetSystemMetrics(0),GetSystemMetrics(1))
	BGC = 'white'
	FGC = (-1,-1,-1) #defining colour of text shown => black
	#log file
	log = open ('logfileprisonersdilemma.txt', 'w')
	log.write(' .... ') #insert headers of what should be logged
	
	win = Window(size=DISPSIZE, units='pix', color=BGC, fullscr=False)
	backgroundimage = ImageStim(win, 'prisonwall.png')
	
	#participant information
	exp_name = 'Prisoner`s dilemma'
	exp_info = {
	            'participant': '', 
	            'gender': ('male', 'female', 'diverse'), 
	            'age':'', 
	            'left-handed':False 
	            }
	dlg = gui.DlgFromDict(dictionary=exp_info, title=exp_name)
	
	print (exp_info)
	
	
	#objects for introduction and instruction
	#introduction text
	introstr = f'''
	Welcome to the prisoner's dilemma game!
	... get part ID and part Name for connection screen later ...
	Press any key to continue. 
	'''
	
	introtxt = TextStim(win, text=introstr, font='Arial', height=20, color='black', 
						   wrapWidth=400)
	#instruction text
	inststr = f'''
	Imagine you are one of two people being questioned about the same crime. They are each talking 
	to the interrogator separately. The interrogator gives each person the same deal: 
	they can choose to vouch for the other person’s innocence (COOPERATING) or rat them out (DEFECTING). 
	And of course, there’s a twist. 
	If both people cooperate with each other, they’ll each get 3 months off their sentence, 
	but if the first person vouches for the second person, and the second person rats them out, 
	the first person will get no time off their sentence and the second person will get 5 months off their time. 
	Lastly, if they both rat each other out, they each get 1 month off their time.
	
	Press 'space' to start the game. Press 'Q' to exit early.
	'''
	
	insttxt = TextStim(win, text=inststr, font='Arial', height=20, color='black', 
						   wrapWidth=400)
	
	#objects for representing participants, images
	#telling people to choose avatar
	avatstr = f'''
	Please choose one of these avatars to represent you in the game.
	Just press the key that responds to letter next to the image.
	'''
	avattxt = TextStim(win, text=avatstr, font='Arial', height=20, color='black', 
						   wrapWidth=400, pos=(000, -300))
	
	#avatars: created with http://www.hexatar.com
	#opponent image stimuli, there are on the right of the screen
	opponent = ImageStim(win, image='opponent2.png', pos=(300, 000)) #placeholder
	participant = ImageStim(win, image='partA', pos=(-300, 000)) #placeholder
	oppcauc = ImageStim(win, image='opponent2.png', pos=(300, 000)) #opponent is caucasian ethnicity 
	oppnoncauc = ImageStim(win, image='opponent1.png', pos=(300, 000)) #opponent who's not caucasian
	oppunknown = ImageStim(win, image='anonymous.jpg', pos=(300, 000))
	
	#participant representation, they are on the left side of the screen
	partA = ImageStim(win, image='partA.png', pos=(-300, 000)) #participant female caucasian
	partB = ImageStim(win, image='partB.png', pos=(-300, 000)) #participant female non caucasian
	partC = ImageStim(win, image='partC.png', pos=(-300, 000)) #participant male caucasian
	partD = ImageStim(win, image='partD.png', pos=(-300, 000)) #participant male non caucasian
	partoverview = ImageStim(win, image='partchoice.png') #start screen from which participant chooses an avatar to represent them in the game
	
	#objects for during the game, in the loop
	sentcountp = 35 #sentence count for the participant
	sentcounto = 35 #sentence count for the opponent
	
	#info about controls/gameplay, should be displayed on the bottom left during the game
	controlinfo = TextStim(win, text='''Press the left arrow to defect 
						   and the right arrow to cooperate''',
						   font='Arial', height=20, color='black',
						    pos=(-300, -300))
	
	# txt within game
	connectstr = 'Your prison sentence is' + str(sentcountp) + 'months.\n' +
	'Your partner`s sentence is' + str(sentcounto) + 'months.\n' +
	'The authorities are still not sure what to do with the two of you. Therefore, you and your partner\n'
	'will be interrogated again by a different police officer. Again you have the choice to cooperate or defect.'
	
	connecttxt = TextStim (win, text=connectstr, font='Arial', height=20, color='black', 
						   wrapWidth=400)			               
	cooptxt = TextStim (win, text='Your opponent chose to cooperate.', font='Arial', height=20, color='black', 
						   wrapWidth=400)
	deftxt = TextStim (win, text='Your opponent chose to defect.', font='Arial', height=20, color='black', 
						   wrapWidth=400)
	
	
	#goodbye screen
	goodbyestr = f'Your final prison sentence is' + sentcountp + 'months.\n' + 'The game is now over.\n' +
	'Thank you for playing!\n'\ 
	goodbye = TextStim (win, text=goodbyestr, font='Arial', height=20, color='black', 
						   wrapWidth=400)
	
	#response keys
	resp = getKeys(keyList = ('q', 'space', 'left', 'right', 'a', 'b', 'c', 'd'))
	
	strategy = [1,2,3,4,5]  #random assignment of opponents strategy
	shuffle(strategy)
	randostrategy = [1,2] #for strategy 3
	condlist = [1,2,3] #1 is in-group, 2 is outgroup, 3 is anon
	ntrials =  7
	oppstrategy = '...' #for updating the sentence counter
	
	
	#function that determines participants sentence and adds it to the sentence counter
	#add unitest here
	'''
	During the experiment, we need to update how many months the participant has
	to spend in prison now, depending on the choice they made and the choice their
	opponent made. For doing this during the trial loop, we write the function
	sentencetracker, that checks the participants choice (either cooperating or
	defecting) as well as the opponents strategy and updates the sentence based on this.
	As a reminder: left arrow to defect and the right arrow to cooperate.
	'''				
	def sentencetracker:
			if response == 'right' & oppstrategy == 'cooperation' #both cooperate
				sentcountp -= 3
				sentcounto -= 3
			if response == 'right' & oppstrategy == 'defect': #participant wants to cooperate,  but opponent rats them out
				sentcountp -= 5
			if response == 'left' & oppstrategy == 'cooperation': #participant rats opponent out, but opponent cooperates
				sentcounto -= 5
			if response == 'left' & oppstrategy == 'defect': #both defect
				sentcountp -= 1
				sentcounto -= 1
		
	
	
	#defining strategies as functions 
	
	'''
	For making the code in the trial loop more legible, we define the possible strategies
	used by the opponent in functions. There are 5 possible strategies that are chosen
	randomly and followed through the whole trial which consists of 7 rounds as default.
	We also include the sentence tracker function and the connection screen that
	displays the current sentence in months.
	'''
	
	def cooperation:
		'''strategy in which opponent always cooperates'''
		opponent.draw()
		participant.draw()
		controlinfo.draw()
		win.flip() 
		response = waitKeys(keyList=('left', 'right'))
		cooptxt.draw
		win.flip()
		wait(4) #seconds
		oppstrategy = 'cooperation'
		sentencetracker()
		connecttxt.draw
		win.flip()
		
	def defect:
		'''opponent always defects'''
		opponent.draw()
		participant.draw()
		controlinfo.draw()
		win.flip() 
		response = waitKeys(keyList=('left', 'right'))
		deftxt.draw()
		win.flip()
		wait(4) #seconds
		sentencetracker()
		oppstrategy = 'defect'
		connecttxt.draw
		win.flip()
		
	def random:
		'''opponent cooperates or defects on a random basis'''
		shuffle(randostrategy)
		random = randostrategy[0]
			if random == 1:
				opponent.draw()
				participant.draw()
				controlinfo.draw()
				win.flip() 
				response = waitKeys(keyList=('left', 'right'))
				cooptxt.draw()
				oppstrategy = 'cooperation'
				win.flip() 
				wait(4)#seconds
				sentencetracker()
				connecttxt.draw
				win.flip()
			else: 
				opponent.draw()
				participant.draw()
				controlinfo.draw()
				win.flip() 
				response = waitKeys(keyList=('left', 'right'))
				deftxt.draw()
				oppstrategy = 'defect'
				win.flip()
				wait(4) #seconds
				sentencetracker()
				connecttxt.draw
				win.flip()
				
	def nicetittat:
		'''nice tit for that: opponent cooperates in first round, then copies participants moves'''
		if ntrials[i] == 1:
				opponent.draw()
				participant.draw()
				controlinfo.draw()
				win.flip() 
				response = waitKeys(keyList=('left', 'right'))
				cooptxt.draw()
				oppstrategy = 'cooperation'
				win.flip() 
				wait(4)#seconds
				sentencetracker()
				connecttxt.draw
				#sentence draw 
				win.flip()
			else ntrials[i] > 1:
				if resp == 'right':
					opponent.draw()
					participant.draw()
					controlinfo.draw()
					win.flip() 
					response = waitKeys(keyList=('left', 'right'))
					cooptxt.draw()
					oppstrategy = 'cooperation'
					win.flip() 
					wait(4)#seconds
					sentencetracker()
					connecttxt.draw
					win.flip()
				else resp == 'left':
					opponent.draw()
					participant.draw()
					controlinfo.draw()
					win.flip() 
					response = waitKeys(keyList=('left', 'right'))
					deftxt.draw()
					oppstrategy = 'defect'
					win.flip() 
					wait(4)#seconds
					sentencetracker()
					connecttxt.draw
					win.flip()
		
	def susptittat:
		'''suspicious tit for that: opponent defects in the first round, then copies the participant's moves'''
		if ntrials[i] == 1:
				opponent.draw()
				participant.draw()
				controlinfo.draw()
				win.flip() 
				response = waitKeys(keyList=('left', 'right'))
				deftxt.draw()
				oppstrategy = 'defect'
				win.flip() 
				wait(4)#seconds
				sentencetracker()
				connecttxt.draw
				win.flip()
			else ntrials[i] > 1:
				if resp == 'right':
					opponent.draw()
					participant.draw()
					controlinfo.draw()
					win.flip() 
					response = waitKeys(keyList=('left', 'right'))
					cooptxt.draw()
					oppstrategy = 'cooperation'
					win.flip() 
					wait(4)#seconds
					sentencetracker()
					connecttxt.draw
					win.flip()
				else resp == 'left':
					opponent.draw()
					participant.draw()
					controlinfo.draw()
					win.flip() 
					response = waitKeys(keyList=('left', 'right'))
					deftxt.draw()
					oppstrategy = 'defect'
					win.flip() 
					wait(4)#seconds
					sentencetracker()
					connecttxt.draw
					win.flip()
	
	'''
	Here we assign the conditions and make sure that the right avatars are displayed, based on the participant`s avatar
	and the condition assigned. They way this is written, you should easily be able to customise which conditions
	you want to use based on which avatars. This might seem like unnecessary complicated code, but it makes transparent
	how the conditions relate to the avatars.
	'''
	def avatarassignment:
		if condition == 1: #playing with an in-group member
			if response == [a] #participant is female caucasian
				opponent.setImage("opponent2.png")
				participant.setImage("partA.png") 
			elif response == [c]: #participant is male caucasian 
				opponent.setImage("opponent2.png")
				participant.setImage("partC.png") 
			elif response == [b]: #participant is female non-caucasian
				opponent.setImage("opponent1.png") 
				participant.setImage("partB.png")
			else: #option d, participant is male non-caucasian
				opponent.setImage("opponent1.png") 
				participant.setImage("partD.png")
			print('in-group condition')
		
		if condition == 2: #playing with an out-group member
			if response == [a] #participant is female caucasian
				opponent.setImage("opponent1.png")
				participant.setImage("partA.png") 
			elif response == [c]: #participant is male caucasian 
				opponent.setImage("opponent1.png")
				participant.setImage("partC.png") 
			elif response == [b]: #participant is female non-caucasian
				opponent.setImage("opponent2.png") 
				participant.setImage("partB.png")
			else: #option d, participant is male non-caucasian
				opponent.setImage("opponent2.png") 
				participant.setImage("partD.png")
			print('out-group condition')
		
		if condition == 3: #playing with no information about opponent
			opponent.setImage("anonymous.jpg")
			if response == [a] #participant is female caucasian
				participant.setImage("partA.png") 
			elif response == [c]: #participant is male caucasian 
				participant.setImage("partC.png") 
			elif response == [b]: #participant is female non-caucasian
				participant.setImage("partB.png")
			else: #option d, participant is male non-caucasian
				participant.setImage("partD.png")
			print('anonymous condition')
	
	
	
	'''
	Time to start the experiment!
	'''
	backgroundimage.draw #background prisonwall
	introtxt.draw()
	win.flip()
	waitKeys(keyList = ('space')) #wait until participant pressed space to continue
	
	#choosing avatar that represents participant 
	avattxt.draw()
	partoverview.draw()
	win.flip()
	response = waitKeys(keyList = ('a', 'b','c','d'))
	
	shuffle(condlist) #randomly assigning condition (in group, out group, anonymous opponent)
	condition = condlist[0]
	avatarassignment()
	
		#waitkeys?
	shuffle(strategy)
	
	#explaining the game
	backgroundimage.draw()
	insttxt.draw()
	win.flip()
	waitKeys(keyList = ('space')) #wait until participant read instructions and pressed space to start the trial loop
	
	#trial loop
	background_image.draw
	for i in range(ntrials):
		
	
		#opponent always cooperates
		if strategy == 1:
			cooperation()
			
		
		#opponent always defects
		elif strategy == 2:
			defect()
	
		#random coop or defect
		elif strategy == 3:
			random()
	
		elif strategy == 4:
			nicetittat()
			
		else strategy == 5:
			susptittat()
			
			
	
	
	#exit early: 
		if resp == ['q']:
			goodbye.draw()
			win.flip()
			wait(5)
			break 
	
	goodbye.draw()
	win.flip()
	wait(5)
	win.close()
	log.close()
	
