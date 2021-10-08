from random import randint
import os
import time
from colours import cprint, resetpointer, setforegroundrgb
from typewriter import typewriter

from asciiimages import medfullwitch, witchface
# from worlddisplay import reset

def rpspreamble():
	typewriter('''You enter the room and stumble as a black cat runs between your legs. It must have been waiting outside the door, but you don't remember having seen it.
Your eyes follow the cat as it makes it's way across the surprisingly messy room, climbing it's way through dead plants; over open, strewn books and around half-mixed potions.
You notice, now, that there are messily drawn pentagrams all over, obviously redrawn in the same spots hundredes of times over. \n''')
	cprint("MR SCRATCHY EARS! WHERE HAVE YOU BEEN?!?!?!", "red")
	setforegroundrgb(72,161,11)
	typewriter("While you were distracted, the cat had evidently made it to it's destination... \n\n")

	time.sleep(2)

	cprint(medfullwitch(),"red")
	time.sleep(2)

	cprint(''' \n "YOU!!!!" ''', "red")
	setforegroundrgb(72,161,11)
	print("She doesn't appear happy")

	cprint("YOU STOLE MY BABY! I'VE BEEN SEARCHING FOR MY MR SCRATCHY EARS ALL OVER", "red")
	setforegroundrgb(72,161,11)
	typewriter("You start to open your mouth to explain the situation, but the witch waves her hand and a cloud of purple smoke hits you. You find yourself unable to speak, or even move. (oh no) \n")

	cprint("I DON'T WANT TO HEAR IT.", "red")
	setforegroundrgb(72,161,11) 
	time.sleep(1)
	typewriter('''Appearing to calm a little, she sits for a moment, in thought. \n''')
	time.sleep(5)

	cprint('''"What ever will we do with this horrid person that took you from me, Mr Scratchy Ears?" ''', "red")
	setforegroundrgb(72,161,11)
	time.sleep(1)
	typewriter("The cat looks at her, then you, then back to her, and gives a single meow \n")
	cprint("That doesn't seem like a harsh enough punishment Mr Scratchy Ears, I was thinking we use their eyes for one of my potions, or grow some herbs from their head", "red")
	setforegroundrgb(72,161,11)
	time.sleep(2)
	cprint("MEOW", "black", "red")
	setforegroundrgb(72,161,11)
	time.sleep(1)
	cprint("Yes, I suppose you were the one that got kidnapped","red")
	setforegroundrgb(72,161,11)
	time.sleep(1)
	cprint("meow", "black", "red")
	setforegroundrgb(72,161,11)
	time.sleep(1)
	cprint("Very well, we'll do that then. But I'm choosing next time", "red")
	setforegroundrgb(72,161,11)
	time.sleep(1)
	cprint("Doubtful.", "black", "red") 
	setforegroundrgb(72,161,11)
	time.sleep(0.5)
	print("did that cat just speak?")
	typewriter('''The witch approaches you, getting a little too close for comfort''')

	witchface()

	cprint('''Mr Scratchy Ears has passed judgement.''', "red")
	setforegroundrgb(72,161,11)
	time.sleep(1)
	typewriter("You find your arms lifting up to face eachother. \n") 
	cprint("By ruling of Mr Scratchy Ears, you are sentenced to", "red")
	setforegroundrgb(72,161,11)
	time.sleep(5)
	cprint('''the dreaded paper, rock, scissors \n
You'll play against your right hand, you'll not get me playing that game''', "red")
	setforegroundrgb(72,161,11)
	typewriter("you can see your right hand is raring to go, already preparing to make it's decision, obviously excited about it's new-found independence \n")
	cprint("go on, I've not got all day", "red")
	setforegroundrgb(72,161,11)
	typewriter("she returns to her cat, almost immediately forgetting you exist.")

def rockpaperscissors():
	win = -1
	list = ["Rock","Paper","Scissors",]
	# print("\033c")
	# rpspreamble()
	while win < 0:
		Black_cat = list[randint(0,2)]
		player = input("Rock, Paper, Scissors?\nEnter your move\n")
		player = player.capitalize()
		if player == Black_cat:
			print("Your right hand chooses {}".format(Black_cat))
			print("Draw")
			print("Looks like you need to give it another go" )
		elif player == "Rock":
			if Black_cat == "Paper":
				print("You lost! Your right hand gives you a thumbs up. ", Black_cat, "covers", player)
				win = 0
				
			else:
				print("You won! Your right hand shakes with rage", player, "smashes", Black_cat)
				win = 1
				
		elif player == "Paper":
			if  Black_cat == "Scissors":
				print("You lost! Your right hand gives you a thumbs up. ", Black_cat,"cut", player)
				win = 0
				
			else:
				print("You won! Your right hand shakes with rage", player,"covers", Black_cat)
				win = 1
				
		elif player == "Scissors":
			if Black_cat == "Rock":
				print("You lost! Your right hand gives you a thumbs up. ", Black_cat, "smashes", player)
				win = 0
				
			else:
				print("You won! Your right hand shakes with rage", player, "cut", Black_cat)
				win = 1
				
		else:
			print("It's rock, paper, scissors, bud.")
	return(win)

def bestof(n = 3, debug = 0):
	'''Runs a best of n of our dice game'''
	print("\033c")
	setforegroundrgb(72,161,11)
	# rpspreamble()
	gamecnt = 0
	wincnt = 0
	while (wincnt < int(n/2) + 1) or (gamecnt < n):
		wincnt += rockpaperscissors()
		time.sleep(2)
		print("\033c")
		setforegroundrgb(72,161,11)
		gamecnt += 1
		print("You have won {} out of {} games".format(wincnt,gamecnt))
		if (n - gamecnt) < (int(n/2) + 1 - wincnt):
			print("You have lost the best of ", n)
			win = 0
	if wincnt >= (int(n/2) + 1):
		print("You won the best of ", n)
		win = 1
		print("Sleep envelopes you. But you do not fall... ")
	else:
		print("You lost the best of ", n)
		win = 0
		print('''A cloud of purple smoke envelops you...''')
	resetpointer()
	return(win)

# rpspreamble()
# rockpaperscissors()
# bestof()
