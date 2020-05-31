# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:37:28 2020

@author: katha
"""
'''
These are the modules used for this experiment.
'''


from psychopy.visual import Window, TextStim, ImageStim
from psychopy.core import wait
from psychopy.event import getKeys, waitKeys, clearEvents
from numpy.random import shuffle
from psychopy import gui
import numpy as np
import random


#create window
DISPSIZE = (1000,700)
#in case that doesn't work, use DISPSIZE = (1000,700)
#for windows only DISPSIZE = (GetSystemMetrics(0),GetSystemMetrics(1))
BGC = 'white'

#log file
log = open ('logfileprisonersdilemma.txt', 'w')
log.write('trial round\topponent strategy\participant strategy\n') #insert headers of what should be logged

win = Window(size=DISPSIZE, units='pix', color=BGC, fullscr=False)
backgroundimage = ImageStim(win, 'prisonwall.png', size=(1000, 1000))

#objects for introduction and instruction
#introduction text
subject_name = 'Kathi'

introstr = f'''
Welcome to the prisoner's dilemma game, {subject_name}!
This game will take about 10 minutes. 
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

insttxt = TextStim(win, text=inststr, font='Arial', height=25, color='white', 
					   wrapWidth=900, pos=(000,-70))

#objects for representing participants, images
#telling people to choose avatar
avatstr = '''
Please choose one of these avatars to represent you in the game.
Just press the key that responds to the letter next to the image.
'''
avattxt = TextStim(win, text=avatstr, font='Arial', height=20, color='black', 
					   wrapWidth=900, pos=(000, -300))

#avatars: created with http://www.hexatar.com
partoverview = ImageStim(win, image='partchoice.png', size=(500,500)) #start screen from which participant chooses an avatar to represent them in the game

#objects for during the game, in the loop
sentcountp = 35
sentcounto = 35

#info about controls/gameplay, should be displayed on the bottom left during the game
controlinfo = TextStim(win, text='''Press the left arrow to defect and the right arrow to cooperate''',
					   font='Arial', height=20, color='white', wrapWidth=900,
					    pos=(000, -300))

# txt within game
connectstr = f'Your prison sentence is {sentcountp} months.\n' 
'Your partner`s sentence is {sentcounto} months.\n'
'The authorities are still not sure what to do with the two of you. Therefore, you and your partner\n'
'will be interrogated again by a different police officer. Again you have the choice to cooperate or defect.'

connecttxt = TextStim (win, text=connectstr, font='Arial', height=20, color='black', 
					   wrapWidth=400)			               
cooptxt = TextStim (win, text='Your opponent chose to cooperate.', font='Arial', height=20, color='black', 
					   wrapWidth=400)
deftxt = TextStim (win, text='Your opponent chose to defect.', font='Arial', height=20, color='black', 
					   wrapWidth=400)


#goodbye screen
goodbyestr = ('The game is now over.\n' +
'Thank you for playing!\n')
goodbye = TextStim (win, text=goodbyestr, font='Arial', height=40, color='black', 
					   wrapWidth=500)


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
def sentencetracker(sentcounto, sentcountp, response, oppstrategy):
    if response == 'right' and oppstrategy == 'cooperation': #both cooperate
        sentcounto -= 3
        sentcountp -= 3
    elif response == 'right' and oppstrategy == 'defect': #participant wants to cooperate,  but opponent rats them out
        sentcountp -= 5
    elif response == 'left' and oppstrategy == 'cooperation': #participant rats opponent out, but opponent cooperates
       sentcounto -= 5
    else: #response == 'left' & oppstrategy == 'defect': #both defect
        sentcountp -= 1
        sentcounto -= 1
    return sentcounto, sentcountp
	





'''
Here we assign the conditions and make sure that the right avatars are displayed, based on the participant`s avatar
and the condition assigned. They way this is written, you should easily be able to customise which conditions
you want to use based on which avatars. This might seem like unnecessary complicated code, but it makes transparent
how the conditions relate to the avatars.
'''




'''
Time to start the experiment!
'''
backgroundimage.draw() #background prisonwall
introtxt.draw()
win.flip()
waitKeys(keyList = ['space']) #wait until participant pressed space to continue
clearEvents()

''' that part worked but couldn't figure out avatar assignment :()
#choosing avatar that represents participant 
avattxt.draw()
partoverview.draw()
win.flip()
aresponse = waitKeys(keyList = ['a','b','c','d'])

shuffle(condlist) #randomly assigning condition (in group, out group, anonymous opponent)
#condition = condlist[1]
'''

opponent = ImageStim(win, image="opponent1.png", pos=(300,000))
participant = ImageStim(win, image='partA.png', pos=(-300, 000))


	
	

''' was supposed to assign condition and set the right avatars, but doesn't work
condition = np.random.randint(1,3)
if condition == 1: #playing with an in-group member
	print('in-group condition')
	if aresponse == 'a': #participant is female caucasian
		opponent = ImageStim(win, image="opponent2.png", pos=(300,000))
		participant = ImageStim(win, image='partA.png', pos=(-300, 000))
	elif aresponse == 'c': #participant is male caucasian 
		opponent = ImageStim(win, image="opponent2.png", pos=(300,000))
		participant = ImageStim(win, image='partC.png', pos=(-300, 000))
	elif aresponse == 'b': #participant is female non-caucasian
		opponent = ImageStim(win, image="opponent1.png", pos=(300,000))
		participant = ImageStim(win, image='partB.png', pos=(-300, 000))
	elif aresponse == 'd': #option d, participant is male non-caucasian
		opponent = ImageStim(win, image="opponent1.png", pos=(300,000))
		participant = ImageStim(win, image='partD.png', pos=(-300, 000))
	
	
	
	
elif condition == 2: #playing with an out-group member
	print('out-group condition')
	if aresponse == 'a': #participant is female caucasian
		opponent = ImageStim(win, image="opponent1.png", pos=(300,000))
		participant = ImageStim(win, image='partA.png', pos=(-300, 000))
		
	elif aresponse == 'c': #participant is male caucasian 
		opponent = ImageStim(win, image="opponent1.png", pos=(300,000))
		participant = ImageStim(win, image='partC.png', pos=(-300, 000))
		
	elif aresponse == 'b': #participant is female non-caucasian
		opponent = ImageStim(win, image="opponent2.png", pos=(300,000))
		participant = ImageStim(win, image='partB.png', pos=(-300, 000))
		
	elif aresponse == 'd': #option d, participant is male non-caucasian
		opponent = ImageStim(win, image="opponent2.png", pos=(300,000))
		participant = ImageStim(win, image='partD.png', pos=(-300, 000))
		
	
	

elif condition == 3: #playing with no information about opponent
	print('anonymous condition')
	opponent = ImageStim(win, image="anonymous.jpg", pos=(300,000))
	if aresponse == 'a': #participant is female caucasian
		participant = ImageStim(win, image='partA.png', pos=(-300, 000))
		 
	elif aresponse == 'c': #participant is male caucasian 
		participant = ImageStim(win, image='partC.png', pos=(-300, 000))
		
	elif aresponse == 'b': #participant is female non-caucasian
		participant = ImageStim(win, image='partB.png', pos=(-300, 000))
		
	elif aresponse == 'd': #option d, participant is male non-caucasian
		participant = ImageStim(win, image='partD.png', pos=(-300, 000))
		
	

clearEvents()
'''


#explaining the game
backgroundimage.draw()
insttxt.draw()
win.flip()
waitKeys(keyList = ['space']) #wait until participant read instructions and pressed space to start the trial loop
strategy = np.random.randint(1,5)
'''Sentence count for the participant and the opponent. You can change this according to your needs, 
however please note that it's 35 because we defined 7 trial rounds and the maximum the 
sentence can change during each round is 5. 7 x 5 is 35, so this is set to prevent the sentence count
from going below 0.
'''
sentcounto = 35
sentcountp = 35
#trial loop



i = 0


for i in range(ntrials):
	backgroundimage.draw()
	i += 1
	log.write(str(i))
	log.write('\t')

	#opponent always cooperates
	if strategy == 1:
		opponent.draw()
		participant.draw()
		controlinfo.draw()
		win.flip() 
		log.write('strategy cooperation\t')
		response = waitKeys(keyList=['left', 'right'])
		if response == 'left':
			log.write('defect\n')
		elif response == 'right':
			log.write('cooperate\n')
		cooptxt.draw()
		win.flip()
		wait(4) #seconds
		oppstrategy = 'cooperation'
		print('strategy cooperation')
		
		sentcounto, sentcountp = sentencetracker(sentcounto, sentcountp, response, oppstrategy) 
		print(sentcounto, sentcountp)
		connectstr = f'''Your prison sentence is {sentcountp} months.
Your partner`s sentence is {sentcounto} months.
The authorities are still not sure what to do with the two of you. 
Therefore, you and your partner will be interrogated again by a different police officer. 
Again you have the choice to cooperate or defect.'''
		connecttxt = TextStim (win, text=connectstr, font='Arial', height=20, color='black', 
					   wrapWidth=400)			               
		connecttxt.draw()
		win.flip()
		wait(7)
		
	
	#opponent always defects
	elif strategy == 2:
		opponent.draw()
		participant.draw()
		controlinfo.draw()
		win.flip() 
		log.write('strategy defect\t')
		response = waitKeys(keyList=['left', 'right'])
		if response == 'left':
			log.write('defect\n')
		elif response == 'right':
			log.write('cooperate\n')
		deftxt.draw()
		win.flip()
		wait(4) #seconds
		oppstrategy = 'defect'
		print('strategy defect')
		sentcounto, sentcountp = sentencetracker(sentcounto, sentcountp, response, oppstrategy) 
		print(sentcounto, sentcountp)
		connectstr = f'''Your prison sentence is {sentcountp} months.
Your partner`s sentence is {sentcounto} months.
The authorities are still not sure what to do with the two of you. 
Therefore, you and your partner will be interrogated again by a different police officer. 
Again you have the choice to cooperate or defect.'''
		connecttxt = TextStim (win, text=connectstr, font='Arial', height=20, color='black', 
					   wrapWidth=400)	
		connecttxt.draw()
		win.flip()
		wait(7)
		

	#random coop or defect
	elif strategy == 3:
		shuffle(randostrategy)
		rando = randostrategy[0]
		print('rando')
		if rando == 1:
			opponent.draw()
			participant.draw()
			controlinfo.draw()
			win.flip() 
			log.write('strategy random cooperation\t')
			response = waitKeys(keyList=['left', 'right'])
			if response == 'left':
				log.write('defect\n')
			elif response == 'right':
				log.write('cooperate\n')
			cooptxt.draw()
			win.flip()
			wait(4)
			oppstrategy = 'cooperation'
			print('rando coop')
			sentcounto, sentcountp = sentencetracker(sentcounto, sentcountp, response, oppstrategy) 
			print(sentcounto, sentcountp)
			connectstr = f'''Your prison sentence is {sentcountp} months.
Your partner`s sentence is {sentcounto} months.
The authorities are still not sure what to do with the two of you. 
Therefore, you and your partner will be interrogated again by a different police officer. 
Again you have the choice to cooperate or defect.'''
			connecttxt = TextStim (win, text=connectstr, font='Arial', height=20, color='black', 
						   wrapWidth=400)	
			connecttxt.draw()
			win.flip()
			wait(7)
		else: 
			opponent.draw()
			participant.draw()
			controlinfo.draw()
			win.flip()
			log.write('strategy random defect\t')
			wait(4) 
			response = waitKeys(keyList=['left', 'right'])
			if response == 'left':
				log.write('defect\n')
			elif response == 'right':
				log.write('cooperate\n')
			deftxt.draw()
			win.flip()
			wait(4) #seconds
			oppstrategy = 'defect'
			print('rando defect')
			sentcounto, sentcountp = sentencetracker(sentcounto, sentcountp, response, oppstrategy)
			print(sentcounto, sentcountp)
			connectstr = f'''Your prison sentence is {sentcountp} months.
Your partner`s sentence is {sentcounto} months.
The authorities are still not sure what to do with the two of you. 
Therefore, you and your partner will be interrogated again by a different police officer. 
Again you have the choice to cooperate or defect.'''
			connecttxt = TextStim (win, text=connectstr, font='Arial', height=20, color='black', 
						   wrapWidth=400)	
			connecttxt.draw()
			win.flip()
			wait(7)

	elif strategy == 4:
		print('nice tit for tat')
		log.write('strategy nice tit for tat\t')
		if i == 1:
			opponent.draw()
			participant.draw()
			controlinfo.draw()
			win.flip() 
			response = waitKeys(keyList=['left', 'right'])
			if response == 'left':
				log.write('defect\n')
			elif response == 'right':
				log.write('cooperate\n')
			cooptxt.draw()
			win.flip()
			wait(4)
			oppstrategy = 'cooperation'
			print('cooperation')
			sentcounto, sentcountp = sentencetracker(sentcounto, sentcountp, response, oppstrategy) 
			print(sentcounto, sentcountp)
			connectstr = f'''Your prison sentence is {sentcountp} months.
Your partner`s sentence is {sentcounto} months.
The authorities are still not sure what to do with the two of you. 
Therefore, you and your partner will be interrogated again by a different police officer. 
Again you have the choice to cooperate or defect.'''
			connecttxt = TextStim (win, text=connectstr, font='Arial', height=20, color='black', 
						   wrapWidth=400)	
			connecttxt.draw()
			win.flip() 
			wait(7)#seconds
		
		elif i > 1:
			if response == 'right':
				opponent.draw()
				participant.draw()
				controlinfo.draw()
				win.flip() 
				response = waitKeys(keyList=['left', 'right'])
				if response == 'left':
					log.write('defect\n')
				elif response == 'right':
					log.write('cooperate\n')
				cooptxt.draw()
				win.flip()
				wait(4)
				oppstrategy = 'cooperation'
				print('cooperation')
				sentcounto, sentcountp = sentencetracker(sentcounto, sentcountp, response, oppstrategy) 
				print(sentcounto, sentcountp)
				connectstr = f'''Your prison sentence is {sentcountp} months.
Your partner`s sentence is {sentcounto} months.
The authorities are still not sure what to do with the two of you. 
Therefore, you and your partner will be interrogated again by a different police officer. 
Again you have the choice to cooperate or defect.'''
				connecttxt = TextStim (win, text=connectstr, font='Arial', height=20, color='black', 
							   wrapWidth=400)			   
				connecttxt.draw()
				win.flip() 
				wait(7)#seconds
				
			elif response == 'left':
				opponent.draw()
				participant.draw()
				controlinfo.draw()
				win.flip() 
				response = waitKeys(keyList=['left', 'right'])
				if response == 'left':
					log.write('defect\n')
				elif response == 'right':
					log.write('cooperate\n')
				deftxt.draw()
				win.flip()
				wait(4)
				oppstrategy = 'defect'
				print('defect')
				sentcounto, sentcountp = sentencetracker(sentcounto, sentcountp, response, oppstrategy) 
				print(sentcounto, sentcountp)
				connectstr = f'''Your prison sentence is {sentcountp} months.
Your partner`s sentence is {sentcounto} months.
The authorities are still not sure what to do with the two of you. 
Therefore, you and your partner will be interrogated again by a different police officer. 
Again you have the choice to cooperate or defect.'''
				connecttxt = TextStim (win, text=connectstr, font='Arial', height=20, color='black', 
							   wrapWidth=400)	
				connecttxt.draw()
				win.flip() 
				wait(7)#seconds
				
		
	elif strategy == 5:
		print('suspicious tit for tat')
		log.write('strategy suspicious tit for tat\t')
		if i == 1:
			opponent.draw()
			participant.draw()
			controlinfo.draw()
			win.flip() 
			response = waitKeys(keyList=['left', 'right'])
			if response == 'left':
				log.write('defect\n')
			elif response == 'right':
				log.write('cooperate\n')
			deftxt.draw()
			win.flip()
			wait(4)
			oppstrategy = 'defect'
			print('defect')
			sentcounto, sentcountp = sentencetracker(sentcounto, sentcountp, response, oppstrategy) 
			print(sentcounto, sentcountp)
			connectstr = f'''Your prison sentence is {sentcountp} months.
	Your partner`s sentence is {sentcounto} months.
	The authorities are still not sure what to do with the two of you. 
	Therefore, you and your partner will be interrogated again by a different police officer. 
	Again you have the choice to cooperate or defect.'''
			connecttxt = TextStim (win, text=connectstr, font='Arial', height=20, color='black', 
						   wrapWidth=400)	
			connecttxt.draw()
			win.flip() 
			wait(7)#seconds
		
		elif i > 1:
			if response == 'right':
				opponent.draw()
				participant.draw()
				controlinfo.draw()
				win.flip() 
				response = waitKeys(keyList=['left', 'right'])
				if response == 'left':
					log.write('defect\n')
				elif response == 'right':
					log.write('cooperate\n')
				cooptxt.draw()
				win.flip()
				wait(4)
				oppstrategy = 'cooperation'
				print('cooperation')
				sentcounto, sentcountp = sentencetracker(sentcounto, sentcountp, response, oppstrategy) 
				print(sentcounto, sentcountp)
				connectstr = f'''Your prison sentence is {sentcountp} months.
	Your partner`s sentence is {sentcounto} months.
	The authorities are still not sure what to do with the two of you. 
	Therefore, you and your partner will be interrogated again by a different police officer. 
	Again you have the choice to cooperate or defect.'''
				connecttxt = TextStim (win, text=connectstr, font='Arial', height=20, color='black', 
							   wrapWidth=400)			   
				connecttxt.draw()
				win.flip() 
				wait(7)#seconds
				
			elif response == 'left':
				opponent.draw()
				participant.draw()
				controlinfo.draw()
				win.flip() 
				response = waitKeys(keyList=['left', 'right'])
				if response == 'left':
					log.write('defect\n')
				elif response == 'right':
					log.write('cooperate\n')
				deftxt.draw()
				win.flip()
				wait(4)
				oppstrategy = 'defect'
				print('defect')
				sentcounto, sentcountp = sentencetracker(sentcounto, sentcountp, response, oppstrategy) 
				print(sentcounto, sentcountp)
				connectstr = f'''Your prison sentence is {sentcountp} months.
	Your partner`s sentence is {sentcounto} months.
	The authorities are still not sure what to do with the two of you. 
	Therefore, you and your partner will be interrogated again by a different police officer. 
	Again you have the choice to cooperate or defect.'''
				connecttxt = TextStim (win, text=connectstr, font='Arial', height=20, color='black', 
							   wrapWidth=400)	
				connecttxt.draw()
				win.flip() 
				wait(7)#seconds
		
	
		
		
	
	
	#exit early: 
	quitt = getKeys(keyList='q')
	if len(quitt) > 0:
		break

goodbye.draw()
win.flip()
wait(3)
	

win.close()
log.close()

