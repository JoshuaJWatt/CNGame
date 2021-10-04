import colours

worldsize = [5,5]

world = [[0,0,0,0,0],
		 [0,1,0,1,0],
		 [0,0,0,0,0],
		 [0,1,0,1,0],
		 [0,0,0,0,0]]

viewsize = 1

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


print(viewwindow((3,2)))