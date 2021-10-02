import colours

worldsize = [5,5]

world = [[0,0,0,0,0],
		 [0,1,0,1,0],
		 [0,0,0,0,0],
		 [0,1,0,1,0],
		 [0,0,0,0,0]]

viewsize = 2


def viewwindow(centre = (0,0)):
	view = []
	for i in range(viewsize):
		row = []
		for j in range(viewsize):
			# If we're too close to the edge, we'll get an index error, so we want to catch that
			try world[centre[0]-i]:
			except IndexError:
				break

