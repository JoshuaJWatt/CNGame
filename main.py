import time, os, sys
import colours as c
import worlddisplay, hangman, dicegame, riddles, story

play = True

def main():
    global play
    play = story.intro()
    while play == True:
        worlddisplay.gamemap()
    time.sleep(60)

main();
