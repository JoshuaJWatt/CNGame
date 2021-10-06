from random import choice
import os
import time
from colours import setpointercolour, resetpointer
from typewriter import typewriter

def hangmanpreamble():
    typewriter('''You enter a room covered with mist. It's vast, and feels very eerie. \n\
You can't make out much of the surroundings but feel the breeze of nearby movement on your skin. With your sight compromised you listen closely to discover sounds of fluttering and flapping. You feel a slight tingling in your hands. As you hold them in front of you to inspect, a large leather-bound book floats perfectly into your palms. The pages flick rapidly and stop all of a sudden. The pages display a hangman challenge and a voice from within the mist whispers... \n\n'''
, speed = 100)

def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def hangman():
    os.system('cls')
    setpointercolour("magenta")
    hangmanpreamble()
    time.sleep(2)
    words = choice(["halloween", "pumpkin", "ghosts", "zombie", "vampire", "blood", "monster", "magical",
        "goblin", "haunted", "spirits", "paranormal", "phantom", "poltergeist", "possessed",
        "bones", "demon", "cemetery", "cursed", "skeleton", "frankenstein", "spider", "coffin", 
        "skull", "trick", "cackle", "ghastly", "tombstone", "witch"])
    guessed = []
    wrong = []
    win = -1
    tries = 7

    
    typewriter("You wont be able to beat me! Give it your best shot, lets play hangman.", speed = 5)
    while tries > 0 and win < 0:
        out = ""
        for letter in words:
            if letter in guessed:
                out = out + letter
            else:
                out = out + "_"

        if out == words:
            break
        print(display_hangman(tries))
        print("\n")
        print("What's your guess?:", out)
        print("You have",tries, " chances left")

        guess = input()

        if guess == words:
            win = 1
        else:
            if guess in guessed or guess in wrong:
                print("You have already tried this letter.", guess)
                time.sleep(1)
            elif guess in words:
                print("Oh no! You got one >:(")
                guessed.append(guess)
                time.sleep(1)
            else:
                if tries == 0:
                    print("Haha, no, you lose")
                    time.sleep(2)
                else:
                    print("NOPE! Haha, try again...")
                    tries -= 1
                    wrong.append(guess)
                    time.sleep(1)

        os.system('cls')

    if tries:
        print("You guessed correctly:", words)
        time.sleep(2)
        resetpointer()
        return(1)
    else:
        print("The word was", words, "better luck next time.")
        time.sleep(2)
        resetpointer()
        return(0)

hangman()