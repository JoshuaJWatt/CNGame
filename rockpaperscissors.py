from random import randint
import os

def rpspreamble():
	print("The preamble and art for the rps game")

def rockpaperscissors():
	os.system('cls')
	rpspreamble()
	win = -1
	list = ["Rock","Paper","Scissors",]
	while win < 0:
		Black_cat = list[randint(0,2)]
		player = input("Rock, Paper, Scissors?\nEnter your move\n")
		player = player.capitalize()
		if player == Black_cat:
			print("Draw")
			print("Let's play again!" )
		elif player == "Rock":
			if Black_cat == "Paper":
				print("You lose!", Black_cat, "covers", player)
				win = 0
				
			else:
				print("You win!", player, "smashes", Black_cat)
				win = 1
				
		elif player == "Paper":
			if  Black_cat == "Scissors":
				print("You lose!", Black_cat,"cut", player)
				win = 0
				
			else:
				print("You win!", player,"covers", Black_cat)
				win = 1
				
		elif player == "Scissors":
			if Black_cat == "Rock":
				print("You lose!", Black_cat, "smashes", player)
				win = 0
				
			else:
				print("You win!", player, "cut", Black_cat)
				win = 1
				
		else:
			print("umm...That's not accepted!")
	return(win)
