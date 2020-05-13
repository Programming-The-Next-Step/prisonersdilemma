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

#these are all just building blocks for now, not functioning code! it won't run yet

#create window

DISPSIZE = (1000, 700)
BGC = 'white'
FGC = (-1,-1,-1) #defining colour of text shown => black

win = Window(size=DISPSIZE, units='pix', color = BGC, fullscr=False)


#create objects and stimuli 

background_image = ImageStim(win, 'prisonwall.png', autoDraw=True) #maybe for works for using a background image?
welcome_str = f'Imagine you are one of two people being questioned about the same crime.\n'\
'They are each talking to the interrogator separately. The interrogator gives each'\
'person the same deal: \n'\
'they can choose to vouch for the other person’s innocence (COOPERATING) or rat them out (DEFECTING).\n '\
'And of course, there’s a twist. If both people vouch for each other, they’ll each get 3 months '\
'off their sentence, but if the first person vouches for the second person, and the second '\
'person rats them out, the first person will get no time off their sentence\n'\
'and the second person will get 5 months off their time. Lastly, if they both '\
'rat each other out, they each get 1 month off their time.\n'\
'You can exit early by pressing Q\nPress space to start'

sentCounter = TextStim(win, text='0 months', font="Arial", height=20, color='black', pos = (300, -300)) #counter stating amount of sentence
controlinfo = TextStim(win, text = 'Press the left arrow to defect and the right arrow to cooperate',
					   font="Arial", height=20, color='black', pos = (-300, -300), autoDraw = True)
#for later in the loop: 
sentCount = 0
sentCounter.setText(str(sentCount)+'months')

#welcome text
welcome_txt = TextStim(win, text=welcome_str, font="Arial", height=20, color='black', 
					   wrapWidth=400)


#avatars: NOT FINISHED YET POSSS
image_01 = ImageStim(win, image="im_01.jpg") #check if it's the right picture and name it after ethnicity
image_02 = ImageStim(win, image="im_02.jpg") 
image_03 = ImageStim(win, image="im_03.jpg") 
image_04 = ImageStim(win, image="im_04.jpg") 
image_05 = ImageStim(win, image="im_05.jpg") 
image_06 = ImageStim(win, image="im_06.jpg")
image_07 = ImageStim(win, image="im_07.jpg")
image_08 = ImageStim(win, image="im_08.jpg")
image_09 = ImageStim(win, image="im_09.jpg")
image_10 = ImageStim(win, image="im_10.jpg")


opponent = Imagetim () #for later in trial loop maybe setIm (if that exists) for randomly assigning opponent based on condition

# txt within game
connecttxt = TextStim ()
cooptxt = TextStim ()
deftxt = TextStim ()

#log file
log = open ('logfileprisonersdilemma.txt', 'w')
log.write(' .... ') #insert headers of what should be logged

#response keys
resp = getKeys(keyList = ('q', 'space', 'left', 'right'))

strategy = [1,2,3,4,5]  #random assignment of opponents strategy
shuffle(strategy)

randostrategy = [1,2] #for strategy 3


condlist = 
n_trials =  #need to set that


#starting the game
background_image.draw()
win.flip()


#trial loop
for i in range(n_trials):
	
	#strategies

	#opponent always cooperates
	if strategy == 1:
		opponent.draw()
		cooptxt.draw()
		win.flip()
		wait(4) #seconds
		connecttxt.draw
		#sentence draw 
		win.flip()
	
	#opponent always defects
	elif strategy == 2:
		opponent.draw()
		deftxt.draw()
		win.flip()
		wait(4) #seconds
		connecttxt.draw
		#sentence draw 
		win.flip()
	
	#random coop or defect
	elif strategy == 3:
		shuffle(randostrategy)
		if randostrategy == 1:
			opponent.draw()
			cooptxt.draw()
			win.flip() 
			wait(4)#seconds
			#sentence draw 
			win.flip()
		elif: 
			opponent.draw()
			deftxt.draw()
			win.flip()
			wait(4) #seconds
			connecttxt.draw
			#sentence draw 
			win.flip()
	
	elif strategy == 4:
		if condlist[i] == 1:
			opponent.draw()
			cooptxt.draw()
			win.flip() 
			wait(4)#seconds
			connecttxt.draw
			#sentence draw 
			win.flip()
		elif condlist[i] > 1:
			if resp == 'right':
				opponent.draw()
				cooptxt.draw()
				win.flip() 
				wait(4)#seconds
				connecttxt.draw
				#sentence draw 
				win.flip()
			elif resp == 'left':
				opponent.draw()
				deftxt.draw()
				win.flip() 
				wait(4)#seconds
				connecttxt.draw
				#sentence draw 
				win.flip()
	elif strategy == 5:
		if condlist[i] == 1:
			opponent.draw()
			deftxt.draw()
			win.flip() 
			wait(4)#seconds
			connecttxt.draw
			#sentence draw 
			win.flip()
		elif condlist[i] > 1:
			if resp == 'right':
				opponent.draw()
				cooptxt.draw()
				win.flip() 
				wait(4)#seconds
				connecttxt.draw
				#sentence draw 
				win.flip()
			elif resp == 'left':
				opponent.draw()
				deftxt.draw()
				win.flip() 
				wait(4)#seconds
				connecttxt.draw
				#sentence draw 
				win.flip()
				
		
			






#exit: 
if resp == ['q']:
	break 

