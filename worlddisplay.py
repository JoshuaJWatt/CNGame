from math import trunc
import colours, hangman, dicegame, riddles
import rockpaperscissors as rps
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
exit = [0,6]

playersprite = "x"
floortile = " "
doortile = "D"

def reset():
	global world
	global viewsize
	global playerscore
	global usabledoors
	global gamelist
	global exit

	world = [["|","x","L","=","D","¬"],
		 ["|",".",".",".",".","D"],
		 ["|","=","=",".","/","="],
		 ["|",".",".",".","D","+"],
		 ["D",".","|",".","L","¬"],
		 ["|",".","D",".",".","D"],
		 ["L","=","┴","D","=","/"]]
	viewsize = 2
	playerpos = (0,1)
	playerscore = 0
	usabledoors = [[5,1],[0,4],[5,5],[3,6]]
	gamelist = [0, 1, 2, 3]
	exit = [0,1]

def viewwindow(centre = (0,0)):
	# This will do the columns
	lowerbound = (centre[1]-viewsize)
	upperbound = (centre[1]+viewsize+1)

	if lowerbound < 0:
		view = world[:upperbound]
	elif upperbound > len(world[0]) + 1:
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
	if [x,y] in usabledoors:
		currentdoor = [x,y]
		return(1)
	if[x,y] == exit:
		if playerscore == 4:
			print("You type the code in and find the door will now open")
			print("You get away and live a happy life or something, idk")
		else:
			print("The door won't budge, and you don't know the code yet")
	else:
		return(0)

def choosegame():
	global gamelist
	game = random.choice(gamelist)
	gamelist.pop(game)
	return(game)

def gamefuncer(n):
	if n == 0:
		out = hangman.hangman()
	elif n == 1:
		out = dicegame.bestof()
	elif n == 2:
		out = riddles.randriddle()
	elif n == 3:
		out = rps.rockpaperscissors()
	else:
		return
	return(out)

def moveplayer(x = 0, y = 0):
	global playerpos
	global world
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
			print("You found a door")
			if doorcheck(loc[0]+x,loc[1]+y) == 0:
				print("The door is locked")
			else:
				print("It's unlocked")
				doorin = input("Do you want to go in? ")
				doorin = doorin.lower()
				if "y" in doorin:
					print("chooses a game to start")
					# out = gamefuncer(choosegame())
					room()
					# return out
		else:
			print("You can't walk through walls, sadly")
	else:
		world[loc[1]][loc[0]] = floortile
		loc[0] += x
		loc[1] += y
		world[loc[1]][loc[0]] = playersprite
		playerpos = (loc[0],loc[1])

def gamemap():
	os.system('cls')
	moveplayer(0,0)
	while True:
		printview(viewwindow(playerpos))
		input_ = input("where to? (n/s/e/w) ")
		input_ = input_.lower()
		os.system('cls')
		if input_ == "n":
			moveplayer(0,-1)
		elif input_ == "s":
			moveplayer(0,1)
		elif input_ == "e":
			moveplayer(1,0)
		elif input_ == "w":	
			moveplayer(-1,0)

def room():
	global playerscore
	global usabledoors
	global currentdoor
	os.system('cls')
	print("You enter the room")
	time.sleep(2)
	game = choosegame()
	loop = True

	while loop == True:
		roomres = gamefuncer(game)
		if roomres == 1:
			time.sleep(2)
			os.system('cls')
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
				os.system('cls')
				print("Looks like you're goin back to the start")
				time.sleep(2)
				reset()
				loop = False
				break
