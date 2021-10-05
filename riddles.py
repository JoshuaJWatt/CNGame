import random as r
import time
import os

def riddlepreamble():
	print("The preamble and art for the riddles")

def randriddle(prev = None):
	'''selects and asks a random riddle, returns a bool of whether the answer was correct'''
	questions = [
		"When is it bad luck to see a cat?     ",
		"What do you get if you cross a Snowman with a witch?     ",
		"What is a ghost's favourite desert ",
		"I am wrapped, but I am not a gift, I am kept neatly in a chamber     ",
		"A zombie and a mummy have a new house and it has all rooms except for one, what room is it?     "
		]
	answers = ["mouse","coldspell","icecream","mummy","livingroom"]
	os.system('cls')
	riddlepreamble()

	int_ = r.randint(0, len(questions) - 1)
	in_ = input(questions[int_])
	for i in in_:
		in_ = in_.replace(" ","")
	
	if in_.find(answers[int_]) != -1:
		print("correct")
		time.sleep(2)
		return(1)
	else:
		print("wrong")
		time.sleep(2)
		return(0)