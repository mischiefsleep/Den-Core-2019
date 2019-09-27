#!/usr/bin/python3

# Guilhem Mizrahi

# This program will perform a Caesar cypher on a text file and print the encypted text to a new text file
# Two user inputs are expected : a file name and an integer (the offset for the cypher)
# A typical command would be "./caesar plain_text.txt 5" and the output would be written to "encrypted_plain_text.txt"
# The main function will call two other functions :
#           rotate_text will open the files, look up the letters and invoke the other function
#           change_letter takes a letter and an offset as input and returns the new letter
# All characters that are not letter will not be encrypted
# This script can be used to both encrypt and decrypt. The decryption is simply done by providing an offset of negative the value of the offset used for encryption

import sys

def change_letter(letter, offset):
    '''
    This function takes a character and an offset. If the character is a letter it will be rotated by the the offset. If it isn't then it is not rotated.
    '''
    if(ord(letter)<92 and ord(letter)>64): # if the letter is uppercase
        return(chr(65+(ord(letter)-65+offset)%26)) # change the letter according to the offset provided
    elif(ord(letter)<123 and ord(letter)>96): # if the letter is lowercase
        return(chr(97+(ord(letter)-97+offset)%26)) # change the letter according to the offset provided
    else:
        return(letter)

def rotate_text(file_name, offset):
    '''
    This function takes a file name as argument and an offset value and will change every letter with the change_letter function
    '''
    try:
        plain_text=open(file_name, "r") # open the file with the text to encrypt
        encrypted_text=open("encrypted_"+file_name, "w+") # open the file to which the result will be written
        offset=int(offset) # make sure the offset is an integer
    except:
        print("File not found or offset invalid") # If the conditions above are not satisfied then exit the function
        return(1)
    for line in plain_text.readlines(): # We look at each line in the text file
        for letter in line: # every letter in the line
            encrypted_text.write(change_letter(letter, offset)) # write the encrypted letter to the file
    plain_text.close() # close the files
    encrypted_text.close()

def main():
    rotate_text(sys.argv[1], sys.argv[2]) # we make the user call the program specifying a file name and an offset

if __name__ == '__main__':
    main()
