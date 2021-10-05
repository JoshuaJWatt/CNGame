import random as r
import time
import os

def dicepreamble():
	print("The preamble and art for the dice game")

def roll(skew = None):
	if skew == None:
		out = r.randint(1,6)
	else:
		out = r.triangular(1,6,skew)
	return(out)

# The game is 21, with 1 die.
def dicegame(cpcheat = 0, skew = None):
	'''Runs a single round of 1 die 21 vs a basic AI'''
	win = -1 # Use this to tell if we've won (1) or lost (0). -1 if undecided
	playerscore = 0
	cpscore = 0
	playerpass = 0
	cppass = 0
	pcnt = 0
	cpcnt = 0
	while win < 0:
		while playerpass == 0: 
			proll = 0
			pcnt += 1
			os.system('cls')
			print("You are on ", playerscore)
			# print("You are on ", playerscore)
			in_ = input("Would you like to roll? (y/n): ")
			if in_ == "y":
				print("you roll your die")
				time.sleep(1)
				print("and it lands on....")
				time.sleep(4)
				proll = roll()
				print(proll)
				time.sleep(1)
				playerscore += proll
			else:
				playerpass = 1
			
			if playerscore > 21:
				win = 0
				print("You went bust")
				return(win)
		while cppass == 0:
			cproll = 0
			cpcnt += 1
			if ((cpscore <= 17 and cpcheat == 0) or cpscore < playerscore or (cpscore == playerscore and cpcnt > pcnt)) and skew == None:
				print("Your opponent rolls their die")
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
			print("your opponent is on ", cpscore)
			if cpscore > 21:
				win = 1
				print("The house went bust, you win")
				return(win)
		if playerscore > cpscore or cpcnt > pcnt:
			win = 1
			print("You won")
		else:
			print("You lost")
			win = 0
		return(win)

def adjustbias(wins, games):
	'''adjusts the bias of the cp depending on the ratio of player wins. WIP'''
	ratio = wins/(games-wins) # the ratio of wins to losses, the cp wants to tend this to 1.


def bestof(n = 3):
	'''Runs a best of n of our dice game'''
	os.system('cls')
	dicepreamble()
	gamecnt = 0
	wincnt = 0
	while wincnt < n/2 + 1 and gamecnt < n:
		wincnt += dicegame()
		gamecnt += 1
		print("You have won {} out of {} games".format(wincnt,gamecnt))
	if wincnt >= n/2 + 1:
		print("You won the best of ", n)
		win = 1
	else:
		print("You lost the best of ", n)
		win = 0
	return(win)
