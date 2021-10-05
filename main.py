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
    c.setforegroundrgb(245, 23, 124)
    c.setbackgrounfrgb(23, 45, 152)
    print("hello world")
    return(1)

main();
