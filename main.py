import time, os, sys
from colorama import Fore, Back, Style
import colours

def typewriter(message):
    for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            
            if char != "\n":
                time.sleep(0.1)
            else:
                time.sleep(1)


colours.prDark("hello world")