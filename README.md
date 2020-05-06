# prisonersdilemma
The goal of this project is implementing the single-trial prisoner’s dilemma, however manipulating the second prisoner a participant would have to deal with by randomly depicting an in-group or out-group member or giving no information. This software is meant for use in experiments; for example, investigating whether people behave differently depending on playing with an ethnic in-group or out-group member. Will a Caucasian player be more like to cooperate with another Caucasian player than with an Asian player, even if the Caucasian player betrays them? Or are players more likely to cooperate if they have any information at all about their fellow prisoner, thus making them more trustworthy, than if they have no information at all? The result of this project should not only be a ready-to-use experimental software, but should also include options for customisation. Therefore, a range of different conditions and possible strategies will be included, but one doesn’t not necessarily have to use all of them in a project but should be able to pick and choose.

Implementing the prisoner's dilemma game will consist of the following steps and components:

* Introduction, explaining to participants what the story is what they are supposed to do. This could look something like this:
> Imagine you are one of two people being questioned about the same crime. >They are each talking to the interrogator separately. The interrogator gives each person the same deal: they can choose to vouch for the other person’s innocence or rat them out. And of course, there’s a twist. If both people vouch for each other, they’ll each get 3 months off their sentence, but if the first person vouches for the second person, and the second person rats them out, the first person will get no time off their sentence and the second person will get 5 months off their time. Lastly, if they both rat each other out, they each get 1 month off their time.

* Graphical user interface: the participant will see his/her avatar on the left and their opponents on the right, separated by a brick wall. The background should look like a prison wall. The controls can be seen on the bottom part of the screen. Additionally, there will be a counter, indicating both prisoner’s sentences in months. It starts with a sentence of 35 months and will be updated after each round.

* Keys: how do participants operate the game? A possibility would be to use the left arrow for defecting and the right arrow for cooperating.

* Log file: recording which strategy the participant follows.

* The “gameplay”: 
	* Participants choose an avatar (e.g. emojis taken from the [openmoji project](https://openmoji.org) or an avatar from [Pick a Face](https://pickaface.net) to represent them in the game.
	* Then they are confronted with their opponent: an ethnic in-group member; an ethnic out-group member; an opponent without information on ethnic group membership serving as a control condition (you can imagine this like the picture shown on facebook when people don't have a profile picture). They will play seven rounds (called one trial; that is the default setting) with the same opponent. The opponent will be randomly assigned as default, but this can be changed as required.
	* The number of trials each participant goes through can be changed but will be set to 1 as default.
	* 5 different strategies will be implemented; the respective researcher using the software in his or her project can choose which ones to use or use all of them.
	* The strategies which relate to one trial are the following:
	1. Opponent always cooperates
	2. Opponent always defects (betrays the participant)
	3. Opponent cooperates or defects on a random basis
	4. Nice tit for tat: opponent cooperates in the first round, then copies the participant's moves
	5. Suspicious tit for tat: opponent defects in the first round, then copies the participant's moves
	(peers: if you have ideas for other strategies that could be interesting, please tell me in the feedback!)
	* There will be connecting screens between the rounds, telling participants the lenght of their sentence at that point. Following the narrative of a prisoner's dilemma, it will also say that the interrogating officers have not made a definite choice yet and will keep on interrogating. Therefore, they have again the choice of cooperating or defecting. (Peers: if you have better ideas on the narrative, I'd like to hear that out)

* The goodbye screen: 
A screen stating the lenght of the final sentence and thanking the participant for taking part.

I will use Python PsychoPy for implementing the experiment. I will not write my own functions since PsychoPy offers a quite extensive library.
* For the background, the avatars, displayed text and the like I will use objects (Window, TextStim, ImageStim)
* The assignment to a condition (in-group/out-group/anonymous) will be implemented through if statements (if avatar chose Caucasian avatar, randomly assign them to a Caucasian opponent, an African opponent or an anonymous opponent). The random part will be done by creating a condition list and shuffling it. The same principle applies when creating the random assignment of strategies the opponent uses. 
* 1 trial, consisting of 7 rounds, will be implemented using a for-loop.

The most important parts for the whole software to function are the strategies opponents are confronted with and the controls, thus this will be implemented first. If I'm short on time, I might cut the opportunity to choose an avatar and represent all participants by the same avatar. In case I have extra time, I would implement the factor gender; right now, the avatars are supposed to look gender-neutral, but I could make gender more explicit by including a female and male avatar for every group membership. Another option would be to use gender as the group identity that is manipulated instead of ethnicity and add this to the code.
