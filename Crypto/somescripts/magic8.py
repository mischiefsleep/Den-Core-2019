#!/usr/bin/python3

# william
# This program simulates a magic 8 ball game
# There are no arguments
# The program will choose at random in a list of messages using the random module and print the message to the screen 

import random as rd

def main():
    try:
       choices=("Cannot predict now", "Ask again later", "Yes", "No", "Why do you ask me ?", "How should I know ?")
       print(choices[rd.randint(0, len(choices)-1)])
       return(0)
   except:
       print("Somehow the program has failed")
       return(1)

if __name__ == '__main__':
    main()
