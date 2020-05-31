# prisonersdilemma
The goal of this project is implementing the single-trial prisoner’s dilemma, however manipulating the second prisoner a participant would have to deal with by randomly depicting an in-group or out-group member or giving no information. This software is meant for use in experiments; for example, investigating whether people behave differently depending on playing with an ethnic in-group or out-group member. Will a Caucasian player be more like to cooperate with another Caucasian player than with an Asian player, even if the Caucasian player betrays them? Or are players more likely to cooperate if they have any information at all about their fellow prisoner, thus making them more trustworthy, than if they have no information at all? The result of this project should not only be a ready-to-use experimental software, but should also include options for customisation. Therefore, a range of different conditions and possible strategies will be included, but one doesn’t not necessarily have to use all of them in a project but should be able to pick and choose.

Eventually, I didn't manage to include this in-group/out-group manipulation but programmed a "normal" prisoner's dilemma game with random assignment of 5 different opponent strategies as well as options for customisation regarding avatars. 

Implementing the prisoner's dilemma game will consist of the following steps and components:

* Introduction, explaining to participants what the story is what they are supposed to do. This could look something like this:
> Imagine you are one of two people being questioned about the same crime. >They are each talking to the interrogator separately. The interrogator gives > each person the same deal: they can choose to vouch for the other person’s innocence or rat them out. And of course, there’s a twist. If both people vouch > for each other, they’ll each get 3 months off their sentence, but if the first person vouches for the second person, and the second person rats them out, > the first person will get no time off their sentence and the second person will get 5 months off their time. Lastly, if they both rat each other out, they >each get 1 month off their time.

* Graphical user interface: the participant will see his/her avatar on the left and their opponents on the right. The background should look like a prison wall. How to operate the game can be seen on the bottom part of the screen. Additionally, there will be a counter, indicating both prisoner’s sentences in months, which is displayed after every round. It starts with a sentence of 35 months and will be updated after each round.

* Keys: Participants operate the game using the left arrow for defecting and the right arrow for cooperating.

* Log file: recording which strategy the participant follows.

* The “gameplay”: 
	* Participant and opponent both are represented by an avatar
	*They will play seven rounds (called one trial; that is the default setting) with one opponent using one strategy.
	* The number of trials each participant goes through can be changed but will be set to 1 as default.
	* 5 different strategies will be implemented; the respective researcher using the software in his or her project can choose which ones to use or use all of them.
	* The strategies which relate to one trial are the following:
	1. Opponent always cooperates
	2. Opponent always defects (betrays the participant)
	3. Opponent cooperates or defects on a random basis
	4. Nice tit for tat: opponent cooperates in the first round, then copies the participant's moves
	5. Suspicious tit for tat: opponent defects in the first round, then copies the participant's moves
	* There will be connecting screens between the rounds, telling participants the lenght of their sentence at that point. Following the narrative of a prisoner's dilemma, it will also say that the participant will no be interrogated by a different officer and that they have again the choice of cooperating or defecting. 

* The goodbye screen: 
A screen thanking the participant for taking part.

I used Python PsychoPy for implementing the experiment. I wrote one function tracking the length of the sentence both prisoners face.
* For the background, the avatars, displayed text and the like I will use objects (Window, TextStim, ImageStim)
* 1 trial, consisting of 7 rounds, is implemented using a for-loop.

