import colours
import sys, os
import random

worldsize = [5,5]

world = [["|","x","L","=","D","¬"],
		 ["|",".",".",".",".","D"],
		 ["|","=","=",".","/","="],
		 ["|",".",".",".","D","+"],
		 ["D",".","|",".","L","¬"],
		 ["|",".","D",".",".","D"],
		 ["L","=","┴","D","=","/"]]

viewsize = 2

playerpos = (0,1)

usabledoors = [[5,1],[0,4],[5,5],[3,6]]
gamelist = [0, 1, 2, 3]

playersprite = "x"
floortile = "."
doortile = "D"

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
	'''Use this to teleport the player. Usually to the start of the map'''

def doorcheck(x, y):
	if [x,y] in usabledoors:
		return(1)
	else:
		return(0)

def choosegame():
	global gamelist
	game = random.choice(gamelist)
	gamelist.pop(game)
	return(game)

def moveplayer(x = 0, y = 0):
	global playerpos
	global world
	for i in range(len(world)):
		#locate the player sprite in the world, we probably don't need to do this anymore
		try:
			loc = [world[i].index(playersprite)]
			loc.append(i)
			# loc.reverse()
			# print(world[(loc[1])+y][(loc[0])+x])
		except UnboundLocalError:
			loc = playerpos
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
					game = choosegame()
					print(game)
					return game
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
		input_ = input("where to? ")
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
		

gamemap()