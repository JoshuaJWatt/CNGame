import sys
import time

def typewriter(text, speed = 1):
		for character in text:
			sys.stdout.write(character)
			sys.stdout.flush()
			if character != "\n":
				time.sleep(0.1)
			else:
				time.sleep(1/speed)