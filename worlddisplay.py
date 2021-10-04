import colours

worldsize = [5,5]

world = [[0,0,0,0,0],
		 [0,1,0,1,0],
		 [0,0,0,0,0],
		 [0,1,0,1,0],
		 [0,0,0,0,0]]

viewsize = 1

# def surrounds(self, x, y):
#         """Checks the surroundings of a cell and returns the number of lives cells around it"""
#         arr = []
#         for i in range (-1, 2):
#             for j in range (-1, 2):
#                 try:
#                     arr.append(self.world[x+i,y+j])
#                 except IndexError:
#                     arr.append(0)
#         sum_ = sum(arr) - self.world[x,y]
#         return(sum_)
		
# def viewwindow(centre = (0,0)):
# 	view = []
# 	for i in range(viewsize):
# 		view.append([])
# 	for i in range(viewsize): # The row we're on
# 		for j in range(viewsize): # the column we're on
# 			# If we're too close to the edge, we'll get an index error, so we want to catch that
# 			try: view[i].append(world[centre[0]-(viewsize - i)])
# 			except IndexError:
# 				view[i].append(' ')
# 	return(view)

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