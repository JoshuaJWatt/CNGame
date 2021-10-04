import colours
import sys

worldsize = [5,5]

world = [["|",".","L","=","=","¬"],
		 ["|",".",".",".",".","|"],
		 ["|","=","=",".","/","="],
		 ["|",".",".",".","|","+"],
		 ["|",".","|",".","L","¬"],
		 ["|",".","|","x",".","|"],
		 ["L","=","┴","=","=","/"]]

viewsize = 2

playersprite = "x"

floortile = "."

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

def moveplayer(x = 0, y = 0):
	for i in range(len(world)):
		try:
			loc = [world[i].index(playersprite)]
			loc.append(i)
			# loc.reverse()
			print(world[(loc[1])+y][(loc[0])+x])
		except ValueError:
			continue
		except IndexError:
			print("Can't move that far, you'd fall off the world")
			return(False)
	if world[(loc[1])+y][(loc[0])+x] != floortile and world[(loc[1])+y][(loc[0])+x] != playersprite:
		print("You can't walk through walls, sadly")
	else:
		world[loc[1]][loc[0]] = floortile
		loc[0] += x
		loc[1] += y
		world[loc[1]][loc[0]] = playersprite

# printview(viewwindow((4,4)))

moveplayer(0, -3)
printview(world)