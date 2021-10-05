import time, os, sys
import colours as c
import worlddisplay, hangman, dicegame, riddles

def typewriter(message):
    for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            
            if char != "\n":
                time.sleep(0.1)
            else:
                time.sleep(1)


def main():
    while True:
        worlddisplay.gamemap()

main();
