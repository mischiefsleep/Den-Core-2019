#!/usr/bin/python3

# william
# This program will randomly generate a story based on a given template by randomly choosing terms to fill the gaps in the story
# The different terms the program can choose from are hardcoded as "global" variables.
# The function elem(tuple) will return a random choice from the tuple given as a parameter.
# The main function will insert the random choices inside the story template and print the result to the screen.
# This program does not require any input from the user

import random # Import the random library that will be used to randomly choose the terms

noun=("car","bus","ball","plane","cup") # These lines store the possible values inside "global" variables
verb=("jump","sit","run","think","smile")
superhero=("Superman","Wonder Woman","Batgirl","Batman")
animal=("dog","cat","octopus","wolverine","snail","monkey")
people=("Abe","Jim","Gary","Michelle","Kimberly","Megan","Omar")
places=("the Citadel Mall","Denver","North Pole","downtown")
season=("spring","winter","fall","summer")

def elem(tuple): # This function will simply return an element from the tuple given as a variable using the random.choice function
    return(random.choice(tuple))

def main():
    # This function will choose an element by calling elem(tuple) each time it has to fill a gap in the story
    print("Every " + elem(season) + ", " + elem(superhero) + \ # and print it to the screen
" is joined by The " + elem(animal) + \
", who's secret identity is " + elem(people) + \
". They attempt to " + elem(verb) +\
", which rarely succeeds. So instead they chase down a " + \
"villain in " + elem(places) + " who was trying to steal a " + \
elem(noun) + ".")

if __name__ == '__main__':
    main() # Call to main() as usual
