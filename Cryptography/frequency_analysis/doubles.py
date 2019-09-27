#!/usr/bin/python3

# Guilhem Mizrahi 09/2019

# This program will take a text file as input and a string and will return the number of times this string appeared in the file.
# This program was useful in assessing if common words like "the", "that", "with" were present in our decrypted text (the absence of these words suggesting an incomplete decryption)

import sys

def doubles_frequency(file_name, term):
    plain_text=open(file_name, "r") # open the file 
    count=0 # initialize the number of occurences of the string to 0
    for line in plain_text.readlines(): # for all the lines in the file
        temp=True # we start by assuming that the string is present in the first characters
        for i in range(len(line)-len(term)+1): # then for each starting index in the line we have to check if the letters match the string (we don't need to check for all values of i as when we reach the end of the line there simply isn't enough space to hold the searched term
            for j in range(len(term)): # we want to check if a string of the same length as the searched term is found at the index i
                if(line[i+j]!=term[j]):
                    temp=False # if a charachter that doesn't match the search term is found then the search term is not found at rank i
            if temp:
                count+=1 # if all the letters match then we can increment the counter for the searched term as we have found one occurence
            temp=True
    print(count)

def main():
    doubles_frequency(sys.argv[1], sys.argv[2]) # the main program will simply execute the search function on the arguments provided by the user

if __name__ == '__main__':
    main()
