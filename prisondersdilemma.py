# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:37:28 2020

@author: katha
"""

from psychopy.visual import Window, TextStim, Circle, ImageStim, Rect, ShapeStim
from psychopy.core import wait, Clock
from psychopy.event import getKeys, clearEvents, waitKeys, Mouse
from numpy.random import shuffle
import numpy as np
import random
from win32api import GetSystemMetrics

#these are all just building blocks for now, not functioning code! it won't run yet

#create window

DISPSIZE = (GetSystemMetrics(0),GetSystemMetrics(1))
BGC = 'white'
FGC = (-1,-1,-1) #defining colour of text shown => black
#log file
log = open ('logfileprisonersdilemma.txt', 'w')
log.write(' .... ') #insert headers of what should be logged

win = Window(size=DISPSIZE, units='pix', color = BGC, fullscr=False)
background_image = ImageStim(win, 'prisonwall.png')


#objects for introduction and instruction
#introduction text
intro_str = f'''
Welcome to the prisoner's dilemma game!
... get part ID and part Name for connection screen later ...
Press any key to continue. 
'''

intro_txt = TextStim(win, text=intro_str, font="Arial", height=20, color='black', 
					   wrapWidth=400)
#instruction text
inst_str = f'''
Imagine you are one of two people being questioned about the same crime. They are each talking 
to the interrogator separately. The interrogator gives each person the same deal: 
they can choose to vouch for the other person’s innocence (COOPERATING) or rat them out (DEFECTING). 
And of course, there’s a twist. 
If both people vouch for each other, they’ll each get 3 months off their sentence, 
but if the first person vouches for the second person, and the second person rats them out, 
the first person will get no time off their sentence and the second person will get 5 months off their time. 
Lastly, if they both rat each other out, they each get 1 month off their time.

Press 'space' to start the game. Press 'Q' to exit early.
'''

inst_txt = TextStim(win, text=inst_str, font="Arial", height=20, color='black', 
					   wrapWidth=400)

#objects for representing participants, images
#telling people to choose avatar
avat_str = f'''
Please choose one of these avatars to represent you in the game.
Just press the key that responds to the image.
Press 'space'to continue.
'''
avat_txt = TextStim(win, text=avat_str, font="Arial", height=20, color='black', 
					   wrapWidth=400, pos = (000, -300))

#avatars: created with http://www.hexatar.com
#opponent image stimuli, there are on the right of the screen
opponent = ImageStim(win, image="opponent2.png", pos=(300, 000)) #placeholder
participant = ImageStim(win, image="partA", pos=(-300, 000)) #placeholder
oppcauc = ImageStim(win, image="opponent2.png", pos=(300, 000)) #opponent is caucasian ethnicity 
oppnoncauc = ImageStim(win, image="opponent1.png", pos=(300, 000)) #opponent who's not caucasian
oppunknown = ImageStim(win, image="anonymous.jpg", pos=(300, 000))

#participant representation, they are on the left side of the screen
partA = ImageStim(win, image="partA.png", pos=(-300, 000)) #participant female caucasian
partB = ImageStim(win, image="partB.png", pos=(-300, 000)) #participant female non caucasian
partC = ImageStim(win, image="partC.png", pos=(-300, 000)) #participant male caucasian
partD = ImageStim(win, image="partD.png", pos=(-300, 000)) #participant male non caucasian
partOverview = ImageStim(win, image="partchoice.png"#start screen from which participant chooses an avatar to represent them in the game

#objects for during the game, in the loop
#textstim counting the participants sentence; should be displayed at the bottom right during the game
sentCounter = TextStim(win, text='0 months', font="Arial",
					    height=20, color='black',
					    pos = (300, -300)) #counter stating amount of sentence

#info about controls/gameplay, should be displayed on the bottom left during the game
controlinfo = TextStim(win, text = '''Press the left arrow to defect 
					   and the right arrow to cooperate''',
					   font="Arial", height=20, color='black',
					    pos = (-300, -300))

# txt within game
connect_str = f''' 
				text	
'''
connecttxt = TextStim (win, text=connectstr + , font="Arial", height=20, color='black', 
					   wrapWidth=400)			               
cooptxt = TextStim ()
deftxt = TextStim ()

#for later in the loop: 
sentCount = 0
sentCounter.setText(str(sentCount)+'months')


#response keys
resp = getKeys(keyList = ('q', 'space', 'left', 'right', 'a', 'b', 'c', 'd'))
strategy = [1,2,3,4,5]  #random assignment of opponents strategy
shuffle(strategy)
randostrategy = [1,2] #for strategy 3
condlist = [1,2,3] #1 is in-group, 2 is outgroup, 3 is anon
n_trials =  #need to set that

#defining strategies as functions 
def cooperation:
	'''strategy in which opponent always cooperates'''
	opponent.draw()
	participant.draw()
	cooptxt.draw
	win.flip()
	wait(4) #seconds
	connecttxt.draw
	#sentence draw 
	win.flip()
	
def defect:
	'''opponent always defects'''
	opponent.draw()
	participant.draw()
	deftxt.draw()
	win.flip()
	wait(4) #seconds
	connecttxt.draw
	#sentence draw 
	win.flip()
	
def random:
	'''opponent cooperates or defects on a random basis'''
	shuffle(randostrategy)
		if randostrategy == 1:
			opponent.draw()
			participant.draw()
			cooptxt.draw()
			win.flip() 
			wait(4)#seconds
			#sentence draw 
			win.flip()
		else: 
			opponent.draw()
			participant.draw()
			deftxt.draw()
			win.flip()
			wait(4) #seconds
			connecttxt.draw
			#sentence draw 
			win.flip()
			
def nicetittat:
	'''nice tit for that: opponent cooperates in first round, then copies participants moves'''
	if condlist[i] == 1:
			opponent.draw()
			participant.draw()
			cooptxt.draw()
			win.flip() 
			wait(4)#seconds
			connecttxt.draw
			#sentence draw 
			win.flip()
		else condlist[i] > 1:
			if resp == 'right':
				opponent.draw()
				participant.draw()
				cooptxt.draw()
				win.flip() 
				wait(4)#seconds
				connecttxt.draw
				#sentence draw 
				win.flip()
			else resp == 'left':
				opponent.draw()
				participant.draw()
				deftxt.draw()
				win.flip() 
				wait(4)#seconds
				connecttxt.draw
				#sentence draw 
				win.flip()
	
def susptittat:
	'''suspicious tit for that: opponent defects in the first round, then copies the participant's moves'''
	if condlist[i] == 1:
			opponent.draw()
			participant.draw()
			deftxt.draw()
			win.flip() 
			wait(4)#seconds
			connecttxt.draw
			#sentence draw 
			win.flip()
		else condlist[i] > 1:
			if resp == 'right':
				opponent.draw()
				participant.draw()
				cooptxt.draw()
				win.flip() 
				wait(4)#seconds
				connecttxt.draw
				#sentence draw 
				win.flip()
			else resp == 'left':
				opponent.draw()
				participant.draw()
				deftxt.draw()
				win.flip() 
				wait(4)#seconds
				connecttxt.draw
				#sentence draw 
				win.flip()
	

#starting the game
background_image.draw #background prisonwall
intro_txt.draw()
win.flip()
waitKeys(keyList = ('space'))

#choosing avatar that represents participant 
avat_txt.draw()
partOverview.draw()
win.flip()
response = waitKeys(keyList = ('a', 'b','c','d'))

shuffle(condlist) #randomly assigning condition (in group, out group, anonymous opponent)

if condlist == 1 & response ==[a]:#participant is female caucasian and plays with in-group member
	opponent.setImage("opponent2.png")
	participant.setImage("partA") 
	#tipps and example on how to do this for every condition on possible choice of participant avatar in a function, my 2 weeks of python experience didn't get me too far on this
	

#trial loop
background_image.draw
for i in range(n_trials):
	
	shuffle(strategy)
	

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
				
		
			






#exit: 
if resp == ['q']:
	break 

