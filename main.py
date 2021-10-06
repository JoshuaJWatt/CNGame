import time, os, sys
import colours as c
import worlddisplay, hangman, dicegame, riddles, story

def main():
    play = True
    play = story.intro()
    while play == True:
        worlddisplay.gamemap()
    os.system('cls')
    story.thanks()

main();
