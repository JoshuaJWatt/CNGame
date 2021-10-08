import time
import worlddisplay,  story

play = True

def main():
    global play
    # play = story.intro()
    while play == True:
        worlddisplay.gamemap()
    time.sleep(60)

main();

