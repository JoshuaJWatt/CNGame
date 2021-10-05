import time, os, sys


def intro():
	print("Welcome to the haunted house game, would you like to play?")

	message_1 = ("You are driving down a country lane, its very dark and stormy so visibility is poor. All of a sudden your car stars to tremble and comes to a stop. \n\
	You leave the car to investigate, it appears you have a flat tyre and cannot continue with your journey home. \n\
	You have no signal... \n\
	There is nobody in sight... \n\
	You continue to look around and spot a light coming from the top of a hill. You make your way towards the light seeking help. \n\
	\n\
	\n\
	")
	message_2 = ("You come to a large house covered in Ivy, with stone gargoyles which seem to stare and follow your every move. \n\
	The door seems to be ajar...you call hello, but no-one answers. \n\
	Do you enter? \n\
	")
	message_3= ("You go in the hallway, which suddenly becomes dark. The door slams shut behind you. \n\
	You hear a noise. \n\
	It is the ringing of an old telephone. You pick up the receiver and a strange voice speaks: \n\
	")
	message_4= ("In order to get out of the house alive you must pass everything ahead. For each challenge you complete you will receive a number, when used together the numbers provide a code to the exit door and you are free to leave. \n\
	But nobody ever leaves...")

	def typewriter(message_1):
		for character in message_1:
			sys.stdout.write(character)
			sys.stdout.flush()
			if character != "\n":
				time.sleep(0.1)
			else:
				time.sleep(1)
	typewriter(message_1)

	def typewriter2(message_4):
		for character in message_4:
			sys.stdout.write(character)
			sys.stdout.flush()
			if character != "\n":
				time.sleep(0.1)
			else:
				time.sleep(3)

	typewriter(message_2)
	#Yes or no?
	# No == Game over - something eats you.
	#Yes == message_3
	typewriter(message_3)
	#riddle
	typewriter2(message_4)
