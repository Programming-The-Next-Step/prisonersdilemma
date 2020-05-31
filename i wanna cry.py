# -*- coding: utf-8 -*-
"""
Created on Sun May 31 12:09:11 2020

@author: katha
"""

from psychopy.visual import Window, TextStim, ImageStim
from psychopy.core import wait
from psychopy.event import getKeys, waitKeys
from numpy.random import shuffle
from psychopy import gui
import numpy as np
import random
from win32api import GetSystemMetrics
import ctypes

#create window
user32 = ctypes.windll.user32
DISPSIZE = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
#in case that doesn't work, use DISPSIZE = (1000,700)
#for windows only DISPSIZE = (GetSystemMetrics(0),GetSystemMetrics(1))
BGC = 'white'

#log file
log = open ('logfileprisonersdilemma.txt', 'w')
log.write(' .... ') #insert headers of what should be logged

win = Window(size=DISPSIZE, units='pix', color=BGC, fullscr=False)
backgroundimage = ImageStim(win, 'prisonwall.png', size=(1000, 1000))

#objects for introduction and instruction
#introduction text
introstr = '''
Welcome to the prisoner's dilemma game!
This game will take about 15 minutes. 
Please wait for further instructions after you've finished.
Press 'space' to continue. 
'''

introtxt = TextStim(win, text=introstr, font='Arial', height=30, color='white', 
					   wrapWidth=400)
#instruction text
inststr = '''
Imagine you are one of two people being questioned about the same crime. They are each talking to the interrogator separately. The interrogator gives each person the same deal: 
they can choose to vouch for the other person’s innocence (COOPERATING) or rat them out (DEFECTING). 
And of course, there’s a twist. If both people cooperate with each other, they’ll each get 3 months off their sentence, 
but if the first person vouches for the second person, and the second person rats them out, 
the first person will get no time off their sentence and the second person will get 5 months off their time. 
Lastly, if they both rat each other out, they each get 1 month off their time.

Press 'space' to start the game.
'''

insttxt = TextStim(win, text=inststr, font='Arial', height=25, color='red', 
					   wrapWidth=900)


#avatars: created with http://www.hexatar.com
partoverview = ImageStim(win, image='partchoice.png', size=(500,500)) #start screen from which participant chooses an avatar to represent them in the game



#info about controls/gameplay, should be displayed on the bottom left during the game
controlinfo = TextStim(win, text='''Press the left arrow to defect and the right arrow to cooperate''',
					   font='Arial', height=20, color='black', wrapWidth=900,
					    pos=(-150, -250))
#objects for during the game, in the loop
sentcountp = 35
sentcounto = 35

# txt within game
connectstr = 'Your prison sentence is' + str(int(sentcountp)) + ' months.\n' \
'Your partner`s sentence is' + str(int(sentcounto)) + ' months.\n' \
'The authorities are still not sure what to do with the two of you. Therefore, you and your partner\n'\
'will be interrogated again by a different police officer. Again you have the choice to cooperate or defect.'

connecttxt = TextStim (win, text=connectstr, font='Arial', height=20, color='black', 
					   wrapWidth=400)			               
cooptxt = TextStim (win, text='Your opponent chose to cooperate.', font='Arial', height=40, color='black', 
					   wrapWidth=400)
deftxt = TextStim (win, text='Your opponent chose to defect.', font='Arial', height=40, color='black', 
					   wrapWidth=400)

response = getKeys(keyList = ['q', 'space', 'enter', 'left', 'right', 'a', 'b', 'c', 'd'])

#goodbye screen
goodbyestr = ('Your final prison sentence is ' + str(sentcountp) + ' months.\n' + 'The game is now over.\n' +
'Thank you for playing!\n')
goodbye = TextStim (win, text=goodbyestr, font='Arial', height=40, color='white', 
						   wrapWidth=500)

strategy = np.random.randint(1, 2)
randostrategy = np.random.randint(1, 2)
ntrials =  7
oppstrategy = '...'







'''
During the experiment, we need to update how many months the participant has
to spend in prison now, depending on the choice they made and the choice their
opponent made. For doing this during the trial loop, we write the function
sentencetracker, that checks the participants choice (either cooperating or
defecting) as well as the opponents strategy and updates the sentence based on this.
As a reminder: left arrow to defect and the right arrow to cooperate.
'''

'''
Time to start the experiment!
'''

backgroundimage.draw() #background prisonwall
introtxt.draw()
win.flip()
waitKeys(keyList = ['space']) #wait until participant pressed space to continue






backgroundimage.draw()
insttxt.draw()
win.flip()
waitKeys(keyList = ['space']) #wait until participant read instructions and pressed space to start the trial loop


strategy = [1,2]
shuffle(strategy)
for i in range(ntrials):
	condition = np.random.randint(1,3)
	opponent = ImageStim(win, image="opponent1.png", pos=(300,000))
	participant = ImageStim(win, image='partD.png', pos=(-300, 000))	
	if strategy[1] == 1:
		oppstrategy = 1
		opponent.draw()
		participant.draw()
		controlinfo.draw()
		win.flip() 
		response = waitKeys(keyList=['left', 'right'])
		
		if response[-1] == 'right':
		 #both cooperate
			sentcountp = sentcountp - 3
			sentcounto = sentcounto - 3
		
		if response[-1] == 'left': #participant rats opponent out, but opponent cooperates
			sentcounto = sentcounto - 5
		
		
		cooptxt.draw()
		win.flip()
		wait(4) #seconds
		
		connecttxt.draw()
		win.flip()
		wait(7)
	elif strategy[1] == 2:
		oppstrategy = 'defect'
		opponent.draw()
		participant.draw()
		controlinfo.draw()
		win.flip() 
		response = waitKeys(keyList=['left', 'right'])
		
	
		if response[-1] == 'right':
		 #both cooperate
			sentcountp = sentcountp - 3
			sentcounto = sentcounto - 3
			print(sentcountp)
			print(sentcounto)
		
		if response[-1] == 'left': #participant rats opponent out, but opponent cooperates
			sentcounto = sentcounto - 5
			print(sentcountp)
			print(sentcounto)
		
		
		
		deftxt.draw()
		win.flip()
		wait(4) #seconds
		
		connecttxt.draw()
		win.flip()
		wait(7)
	
	
	 
	#exit early: 
	if response == 'q':
		goodbye.draw()
		win.flip()
		wait(5)
		break 

	
goodbye.draw()
win.flip()
wait(5)
win.close()