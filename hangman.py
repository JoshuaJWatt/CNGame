from random import choice
import os
import time

def hangmanpreamble():
    print("The preamble and art for the hangman game")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
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
    hangmanpreamble()
    words = choice(["halloween", "pumpkin", "ghosts", "zombie", "vampire", "blood", "monster", "magical",
        "goblin", "haunted", "spirits", "paranormal", "phantom", "poltergeist", "possessed",
        "bones", "demon", "cemetery", "cursed", "skeleton", "frankenstein", "spider", "coffin", 
        "skull", "trick", "cackle", "ghastly", "tombstone", "witch"])
    guessed = []
    wrong = []
    win = -1
    tries = 6

    while tries > 0 and win < 0:
        out = ""
        for letter in words:
            if letter in guessed:
                out = out + letter
            else:
                out = out + "_"

        if out == words:
            break
        print("You wont be able to beat me! Give it your best shot, lets play hangman.")
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
                print("NOPE! Haha, try again...")
                tries -= 1
                wrong.append(guess)
                time.sleep(1)

        print()
        os.system('cls')

    if tries:
        print("You guessed correctly:", words)
        time.sleep(2)
        return(1)
    else:
        print("The word was", words, "better luck next time.")
        time.sleep(2)
        return(0)

