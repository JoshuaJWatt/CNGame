import time, os, sys
from typewriter import typewriter
from asciiimages import pumpkinout, hauntedhouse, old_telephone
import colours


def intro():

	message_1 = ("You are driving down a country lane, it's very dark and stormy so visibility is poor. All of a sudden your car starts to tremble and comes to a stop. \n\
You leave the car to investigate, it appears you have a flat tyre and cannot continue with your journey home. \n\
You have no signal... \n\
There is nobody in sight... \n\
You continue to look around and spot a light coming from the top of a hill. You make your way towards the light seeking help. \n")
	message_2 = ("You come to a large house covered in Ivy, with stone gargoyles which seem to stare and follow your every move. \n\
The door seems to be ajar...you call out, but no-one answers. \n")
	message_3= ('''You enter the hallway, which suddenly becomes dark. The door slams shut behind you. \n\
You hear a noise. \n\
It is the ringing of an old telephone.\n''')
	message_4= ("In order to get out of the house alive you must pass everything ahead. For each challenge you complete you will receive a number, when used together the numbers provide a code to the exit door and you are free to leave. \n\
But nobody ever leaves...")

	while True:
		ans = input("Welcome to the haunted house game, would you like to play? (y/n)" )
		os.system('cls')
		if "n" in ans:
			return(False)
		elif "y" in ans:
			typewriter(message_1)
			typewriter(message_2)
			typewriter(message_3)
			print(old_telephone())
			time.sleep(3)
			os.system('cls')
			typewriter("You pick up the receiver and a strange voice speaks: \n")
			typewriter(message_4, speed = 0.3)

			return(True)

def escape():
	global play
	os.system('cls')
	typewriter('''You have all 4 numbers now, so you should be allowed to leave. 
You try the handle, and it actually turns. You tentatively pull the door open, it could just be a trick after all. 
As soon as the door is opened far enough you run out of it and back down the hill. 
You jump back into your car, you'll just drive on rims, and deal with the tire issue once you're well clear of this place \n''')
	typewriter("You drive off, as quickly as one can with one wheel dragging, atleast relieved that you're finally out of that place...")
	time.sleep(3)
	colours.setpointercolour("magenta")
	os.system('cls')
	typewriter("A small porcelein doll sits on your back seat. It turns it's head.")
	time.sleep(3)
	os.system('cls')

	print('''___________.___ _______   
\_   _____/|   |\      \  
 |    __)  |   |/   |   \ 
 |     \   |   /    |    \\
 \___  /   |___\____|__  /
     \/                \/ ''')

	# play = False
	time.sleep(3)
	
	thanks()
	
	
def thanks():
	colours.setforegroundrgb(252,76,2)
	colours.setbackgrounfrgb(72,161,11)
	print(hauntedhouse())
	time.sleep(5)
	os.system('cls')
	print(pumpkinout())
	print("Thanks for playing!")
	time.sleep(20)
	colours.resetpointer()

# thanks()
