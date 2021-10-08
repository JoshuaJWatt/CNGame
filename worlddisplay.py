import colours, hangman, dicegame, riddles, story
import rockpaperscissors as rps
from typewriter import typewriter
import sys, os
import random
import time

worldsize = [5,5]

# world = [["|","x","L","=","D","¬"],
# 		 ["|",".",".",".",".","D"],
# 		 ["|","=","=",".","/","="],
# 		 ["|",".",".",".","D","+"],
# 		 ["D",".","|",".","L","¬"],
# 		 ["|",".","D",".",".","D"],
# 		 ["L","=","┴","D","=","/"]]

world =[["=","=","=","=","=","=","D","=","=","=","="],
		["=","=","="," ","=","=","x","=","=","=","="],
		["="," "," "," "," "," "," ","=","D","=","="],
		["="," ","=","=","=","=","=","="," "," ","="],
		["="," ","D","=","=","=","=","D"," ","=","="],
		["="," ","=","=","=","=","=","="," ","=","="],
		["="," "," "," "," "," "," "," "," ","=","="],
		["=","=","=","="," ","=","=","=","=","=","="],
		["=","=","=","="," ","=","=","=","=","=","="],
		["=","=","=","="," ","=","=","=","=","=","="],
		["=","=","=","D"," ","D","=","=","=","D","="],
		["=","=","=","="," ","=","=","=","="," ","="],
		["=","=","=","="," ","=","=","=","="," ","="],
		["=","D","=","="," ","=","=","=","="," ","="],
		["="," "," "," "," "," "," "," "," "," ","="],
		["=","=","=","=","=","=","=","="," ","=","="],
		["=","=","=","=","=","=","=","=","D","=","="]]

viewsize = 1

playerpos = (0,6)
playerscore = 0

usabledoors = [[7,4],[1,13],[5,10],[9,10]]
currentdoor = []
gamelist = [0, 1, 2, 3]
playedlist = []
exit = [6,0]

playersprite = "x"
floortile = " "
doortile = "D"

play = True
metd = 0



def reset():
	global world
	global viewsize
	global playerpos
	global playerscore
	global usabledoors
	global playedlist
	global exit
	global metd

	world = [["=","=","=","=","=","=","D","=","=","=","="],
		["=","=","="," ","=","=","x","=","=","=","="],
		["="," "," "," "," "," "," ","=","D","=","="],
		["="," ","=","=","=","=","=","="," "," ","="],
		["="," ","D","=","=","=","=","D"," ","=","="],
		["="," ","=","=","=","=","=","="," ","=","="],
		["="," "," "," "," "," "," "," "," ","=","="],
		["=","=","=","="," ","=","=","=","=","=","="],
		["=","=","=","="," ","=","=","=","=","=","="],
		["=","=","=","="," ","=","=","=","=","=","="],
		["=","=","=","D"," ","D","=","=","=","D","="],
		["=","=","=","="," ","=","=","=","="," ","="],
		["=","=","=","="," ","=","=","=","="," ","="],
		["=","D","=","="," ","=","=","=","="," ","="],
		["="," "," "," "," "," "," "," "," "," ","="],
		["=","=","=","=","=","=","=","="," ","=","="],
		["=","=","=","=","=","=","=","=","D","=","="]]
	viewsize = 1
	playerpos = (0,6)
	playerscore = 0
	usabledoors = [[7,4],[1,13],[5,10],[9,10]]
	playedlist = []
	exit = [0,6]
	metd = 0

def viewwindow(centre = (0,0)):
	# This will do the columns
	lowerbound = (centre[1]-viewsize)
	upperbound = (centre[1]+viewsize+1)

	if lowerbound < 0:
		view = world[:upperbound]
	elif upperbound > len(world) + 1:
		view = world[lowerbound:]
	else:
		view = world[lowerbound:upperbound]
	
	# This will do rows
	lowerbound = (centre[0]-viewsize)
	upperbound = (centre[0]+viewsize+1)

	if lowerbound < 0:
		lowerbound = 0
	if upperbound > len(world[0]) + 1:
		upperbound = len(world[0])

	for i in range(len(view)):
		view[i] = view[i][lowerbound:upperbound]

	return(view)

def printview(view):
	for i in view:
		for j in i:
			sys.stdout.write(j)
		sys.stdout.write("\n")

def setplayerloc(x, y):
	'''PLACEHOLDER Use this to teleport the player. Usually to the start of the map. PLACEHOLDER'''

def doorcheck(x, y):
	global currentdoor
	global play
	print("You found a door")
	if[x,y] == exit:
		if playerscore == 4:
			story.escape()
			# play = False
			return(-1)
		else:
			print("The door won't budge, and you don't know the code yet")
			return(0)
	if [x,y] in usabledoors:
		currentdoor = [x,y]
		return(1)
	else:
		return(0)

def choosegame():
	global gamelist
	global playedlist
	chosen = 0
	while chosen == 0:
		game = random.choice(gamelist)
		if game in playedlist:
			continue
		else:
			playedlist.append(game)
			chosen = 1
	return(game)

def gamefuncer(n):
	if n == 0:
		out = hangman.hangman()
	elif n == 1:
		out = dicegame.bestof()
	elif n == 2:
		out = riddles.randriddle()
	elif n == 3:
		out = rps.bestof()
	else:
		return
	return(out)

def moveplayer(x = 0, y = 0):
	# The code here is self documenting. Enjoy,
	global playerpos
	global world
	global play
	loc = [playerpos[0],playerpos[1]]
	for i in range(len(world)):
		#locate the player sprite in the world, we probably don't need to do this anymore
		try:
			loc = [world[i].index(playersprite)]
			loc.append(i)
			# loc.reverse()
			# print(world[(loc[1])+y][(loc[0])+x])
		except UnboundLocalError:
			[playerpos[0],playerpos[1]]
		except ValueError:
			continue
		except IndexError:
			print("Can't move that far, you'd fall off the world")
			return(False)
	if world[(loc[1])+y][(loc[0])+x] != floortile and world[(loc[1])+y][(loc[0])+x] != playersprite:
		if world[(loc[1])+y][(loc[0])+x] == doortile:
			doorch = doorcheck(loc[0]+x,loc[1]+y)
			if doorch == 0:
				print("The door is locked")
			elif doorch == -1:
				play = False
			else:
				print("It's unlocked")
				doorin = input("Do you want to go in? ")
				doorin = doorin.lower()
				if "y" in doorin:
					# Puts the player in a 'room' starting a random game
					room()
		else:
			print("You can't walk through walls, sadly")
	else:
		world[loc[1]][loc[0]] = floortile
		loc[0] += x
		loc[1] += y
		world[loc[1]][loc[0]] = playersprite
		playerpos = (loc[0],loc[1])

def gamemap():
	print("\033c")
	moveplayer(0,0)
	global play
	while play == True:
		colours.setforegroundrgb(252,76,2)
		moveplayer(0,0)
		if playerscore == 4:
			print("You've got all 4 numbers, you should try getting out of the front door")
		printview(viewwindow(playerpos))
		input_ = input("where to? (n/s/e/w) ")
		input_ = input_.lower()
		colours.resetpointer()
		print("\033c")
		if input_ == "n":
			moveplayer(0,-1)
		elif input_ == "s":
			moveplayer(0,1)
		elif input_ == "e":
			moveplayer(1,0)
		elif input_ == "w":	
			moveplayer(-1,0)
	play = False

def room():
	global playerscore
	global usabledoors
	global currentdoor
	print("\033c")
	print("You enter the room")
	time.sleep(2)
	game = choosegame()
	loop = True

	while loop == True:
		roomres = gamefuncer(game)
		if roomres == 1:
			time.sleep(2)
			print("\033c")
			print("You won the room, you find yourself back outside the door with a new number written on your hand")
			time.sleep(2)
			playerscore += 1
			usabledoors.remove(currentdoor)
			loop = False
			
		else:
			print("You lost the room")
			time.sleep(2)
			rid = riddles.randriddle()
			if rid == 1:
				continue

			else:
				colours.setforegroundrgb(255,192,203)
				print("\033c")
				print("Looks like you get to start again.")
				print("See you again later, though you won't remember me! BYYYYEEEEE!")
				time.sleep(2)
				colours.resetpointer()
				reset()
				loop = False
				break

# escape()