import random as r
import time
import os
from typewriter import typewriter
from colours import cprint, resetpointer, rgbprint, setforegroundrgb, setpointercolour

dollcolourr = 255
dollcolourg = 192
dollcolourb = 203

metd = 0

def riddlepreamble():
	typewriter("You find yourself in complete darkness. \n")
	time.sleep(5)
	typewriter("A spotlight flickers on, with it's dull light, throught the dust it highlights a small porcelain doll slumped in a dusty old armchair. \n")
	time.sleep(3)
	typewriter("Slowly, the dolls head turns to look at you. You see a little spark of joy in it's otherwise lifeless glass eyes, though you know that joy is only at your own distress.")
	setforegroundrgb(dollcolourr, dollcolourg, dollcolourb)
	print("Hey there!")
	typewriter('''Are you enjoying yourself?
I know I am!
Watching you try to escape my house has been really fun! \n''', 100)
	resetpointer()
	typewriter("You can tell that if the doll could move, she's be bouncing up and down with excitement.")
	setforegroundrgb(dollcolourr, dollcolourg, dollcolourb)
	typewriter("And, seeing as we've finally met, I want to introduce you to my favourite thing to do with visitors! \n", 10)
	time.sleep(3)
	print("\n RIDDLES! YAAAY!\n")
	typewriter("The best bit about my riddles is that if you get them wrong, you have to start the house all over again!\n",)
	typewriter("I know we're going to have so much fun, you can stay forever!\n", 100)
	resetpointer()

def riddlepreamble_met():
	typewriter("You find yourself back in the dark room, the doll highlighted by a flickering spotlight")
	setforegroundrgb(dollcolourr, dollcolourg, dollcolourb)
	print("Welcome back! I'm glad you enjoyed last time so much you came back!")

def randriddle(prev = None):
	'''selects and asks a random riddle, returns a bool of whether the answer was correct'''
	questions = [
		"When is it bad luck to see a cat? ",
		"What do you get if you cross a Snowman with a witch? ",
		"What is a ghost's favourite desert ",
		"I am wrapped, but I am not a gift, I am kept neatly in a chamber ",
		"A zombie and a mummy have a new house and it has all rooms except for one, what room is it? ",
		"The person who built it sold it. The person who bought it never used it. The person who used it never saw it. What is it?",
		"What is the main subject taught at witchcraft school?",
		"Where do ghosts, zombies and mummies love to go swimming? ",
		"You’ll find me in the quietest, creepiest place in town, yet people are dying to get in. What am I?"
		]
	answers = ["mouse","coldspell","icecream","mummy","livingroom","coffin","spelling", "deadsea", "cemetary"]
	print("\033c")
	global metd
	if metd == 0:
		riddlepreamble()
		metd = 1
	else:
		riddlepreamble_met()

	rgbprint("Sooooooo... \n", dollcolourr, dollcolourg, dollcolourb)
	int_ = r.randint(0, len(questions) - 1)

	setforegroundrgb(dollcolourr, dollcolourg, dollcolourb)
	in_ = input(questions[int_])
	resetpointer()

	for i in in_:
		in_ = in_.replace(" ","")
	
	if in_.find(answers[int_]) != -1:
		rgbprint("That's right! You're so smart! I'll let you go back to what you were doing, see you later!", dollcolourr, dollcolourg, dollcolourb)
		time.sleep(2)
		return(1)
	else:
		rgbprint("No, silly!", dollcolourr, dollcolourg, dollcolourb)
		# time.sleep(0.5)
		# rgbprint("See you again later, though you won't remember me! BYYYYEEEEE!", dollcolourr, dollcolourg, dollcolourb)
		# time.sleep(2)
		return(0)

# riddlepreamble()
# randriddle()

# rgbprint("test test", dollcolourr, dollcolourg, dollcolourb)