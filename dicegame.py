import random as r
import time
import os
from asciiimages import smallspoopyman
from typewriter import typewriter

def dicepreamble():
	typewriter('''You enter a study, a small desk is lit by an even smaller lamp.
Walls and walls of bookcases, stacked with books hundreds of meters high stretch on for what seems like forever.
And yet you feel constricted, crushed, as if trapped in a box half your size, crushed by the pressure of the 
millions of books that surround you.''')
	time.sleep(4)
	print("\033c")
	smallspoopyman()
	typewriter('''
A flickering figure appears by the desk and you feel yourself moving to join him. 
As much as you try, you can't seem to see his face, or perhaps you just can't remember it, even as you look at it. His features lost before they make it from you eyes to your mind.He doesn't speak. You know, somehow, that he never speaks. 
He produces a pair of dice, you immediately know he is challenging you to a game.
You really don't have much choice in accepting the challenge, even if you thought otherwise . \n
The rules come to you, as if you always knew them:
Roll your die to get the highest number, without exceeding 21. Draw is decided on fewest rolls \n\n''', speed = 100)

def roll(skew = None):
	if skew == None:
		out = r.randint(1,6)
	else:
		out = r.triangular(1,6,skew)
	return(out)

# The game is 21, with 1 die.
def dicegame(cpcheat = 0, skew = None, debug = 0):
	'''Runs a single round of 1 die 21 vs a basic AI'''
	win = -1 # Use this to tell if we've won (1) or lost (0). -1 if undecided
	playerscore = 0
	cpscore = 0
	playerpass = 0
	cppass = 0
	pcnt = 0
	cpcnt = 0
	while win < 0:
		playerpass = 0
		cppass = 0
		playerscore = 0
		cpscore = 0
		if debug == 1:
			playerscore = int(input("pscore: "))
			pcnt = int(input("pcnt: "))
			cpscore = int(input("cpscore: "))
			cpcnt = int(input("cpcnt: "))
		while playerpass == 0: 
			proll = 0
			pcnt += 1
			# print("You are on ", playerscore)
			in_ = input("Would you like to roll? (y/n): ")
			if "y" in in_:
				print("you roll your die")
				time.sleep(1)
				print("and it lands on....")
				time.sleep(1)
				proll = roll()
				print(proll)
				time.sleep(1)
				playerscore += proll
			else:
				playerpass = 1
			print("\033c")
			print("You are on ", playerscore)
			if playerscore > 21:
				win = 0
				print("You went bust. You can feel the man's amusement, a quiet laughing bouncing around inside your mind")
				return(win)
		while cppass == 0:
			cproll = 0
			cpcnt += 1
			# (cpscore <= 17 and cpcheat == 0) or 
			if ((cpscore < playerscore or (cpscore == playerscore and cpcnt > pcnt)) and cpscore < 21) and skew == None:
				print("The man rolls his die, though you're not sure he touched it.")
				time.sleep(1)
				print("and it lands on...")
				time.sleep(4)
				cproll = roll()
				print(cproll)
				cpscore += cproll
			elif skew != None:
				if (cpscore <= 21 - skew) or cpscore < playerscore:
					print("Your opponent rolls their die")
					time.sleep(1)
					print("and it lands on...")
					time.sleep(4)
					cproll = roll(skew)
					print(cproll)
					cpscore += cproll
				else:
					cppass = 1
			else:
				cppass = 1
			print("\033c")
			print("You are on ", playerscore, "in ", pcnt)
			print("your opponent is on ", cpscore, "in ", cpcnt)
			if cpscore > 21:
				win = 1
				print("The house went bust, you win. You can feel the man's annoyance, a hot, red pressure in your mind")
				return(win)
		if playerscore > cpscore or (playerscore == cpscore and cpcnt > pcnt):
			win = 1
			print("You won")
		elif playerscore == cpscore and pcnt == cpcnt:
			print("A complete draw. A rarity.")
			continue
		else:
			print("You lost. Laughter bounces around inside your head, drowning out all other thought.")
			win = 0
	return(win)

def adjustbias(wins, games):
	'''adjusts the bias of the cp depending on the ratio of player wins. WIP'''
	ratio = wins/(games-wins) # the ratio of wins to losses, the cp wants to tend this to 1.


def bestof(n = 3, debug = 0):
	'''Runs a best of n of our dice game'''
	
	print("\033c")
	dicepreamble()
	gamecnt = 0
	wincnt = 0
	while wincnt < int(n/2) + 1 and gamecnt < n:
		wincnt += dicegame(debug = debug)
		gamecnt += 1
		print("You have won {} out of {} games".format(wincnt,gamecnt))
	if wincnt >= int(n/2) + 1:
		print("You won the best of ", n)
		win = 1
		print("Sleep envelopes you. But you do not fall... ")
		time.sleep(3)
	else:
		print("You lost the best of ", n)
		win = 0
		print('''The laughter won't stop now, it is constant, and deafening. 
		You cover your ears, but that doesn't help, in fact it appears to amuse the man even more as his laughter somehow gets louder. You're head is on the verge of exploding''')
		time.sleep(3)
	return(win)


# dicegame(debug=1)
# bestof()