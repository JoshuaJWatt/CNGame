import time, os, sys
import colours as c

def typewriter(message):
    for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            
            if char != "\n":
                time.sleep(0.1)
            else:
                time.sleep(1)


def main():
    c.cprint("hello world", "red", "green")
    c.cprint("hello world")
    print("hello world")

    c.tileprint()
    c.tileprint(n = 5)
    c.tileprint("green")
    return(1)

main();
