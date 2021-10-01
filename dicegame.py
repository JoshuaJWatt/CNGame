import random as r
import time

def roll(skew = None):
	if skew == None:
		out = r.randint(1,6)
	else:
		out = r.triangular(1,6,skew)
	return(out)

# The game is 21.
def dicegame():
	win = -1 # Use this to tell if we've won (1) or lost (0). -1 if undecided
	playerscore = 0
	cpscore = 0
	playerpass = 0
	cppass = 0
	cpcheat = 0
	while win < 0:
		if playerpass == 0: 
			proll = 0
			print("You are on ", playerscore)
			in_ = input("Would you like to roll? (y/n): ")
			if in_ == "y":
				print("you roll your die")
				time.sleep(1)
				print("and it lands on....")
				time.sleep(4)
				proll = roll()
				print(proll)
				playerscore += proll
			else:
				playerpass = 1
			print("You are on ", playerscore)
			if playerscore > 21:
				win = 0
				print("You went bust")
				return(win)
		if cppass == 0:
			cproll = 0
			if cpscore <= 
			print("Your opponent rolls their die")