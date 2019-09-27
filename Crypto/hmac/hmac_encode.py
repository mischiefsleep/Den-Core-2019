#!/usr/bin/python3
# William

# This program takes a text file with the formating <sentence>:<hash> and a .key file that contains the key used to compute the hashes
# It will compute the hash of the sentence and compare it to the associateed hash in the file
# The aim of this program is to be able to detect if a sentence has been altered or not
# If a sentence hash a hash that doesn't match the provided hash, it is safe to assume that this sentence has been altered in some way.
# This program is made up of 3 functions.
#       split_text takes a file_name as input and parses it assuming the format of the file is <sentence>:<hash> and returns a dictionary of key:value pair where the key is the sentence and the value is the hash
#       gen_tag takes a key and a string as input and encodes the message using the key provided as input to the program
#       main will make the calls to the other functions in order to perform the desired task

import hmac # This package is used to compute the hashes
import sys # This package is used to parse the command line arguments so the file names are not hard coded

def split_text(text_file): # This function takes a file name as input with the syntax <sentence>:<hash> and returns a dictionary "sentence":"hash"
    out_file=open(text_file, 'r')
    list_of_lines=out_file.readlines() # make a list of lines, each line contains a <sentence>:<hash> string
    out_dict={} # initially the dictionary is empty
    for i in range(len(list_of_lines)): # For every line we split the line and populate the dictionary
        text_tag=list_of_lines[i].split(':')
        out_dict[text_tag[0]]=text_tag[1].replace('\n', '') # be careful to remove the end of line in the string
    return(out_dict)

def gen_tag(key, message): # This function will encrypt the message using the key
    encoded_hmac=hmac.new(key.encode()) # Creating a new hmac object from the hmac package
    encoded_hmac.update(message.encode()) # We update the object with a message
    return(encoded_hmac) # Be aware that encoded_hmac is not a hash string but a hmac object. The main function will call the appropriate method to compare actual hashes
    

def main(text_file, key):
    # Parse the file using the split_text function
    text_dict=split_text(text_file)
    # Initialize the not matching sentences to empty list
    not_matching_text=[]
    # For each sentence in the list 
    for message in text_dict.keys():
        calculated_hash=gen_tag(key, message).hexdigest() # Compute the hash
        if not hmac.compare_digest(calculated_hash, text_dict[message]): # if the hashes don't match
            not_matching_text.append(message) # append the sentence to the list on not matching sentences
    print("Texts not matching the hash\n") # print the output to the screen
    print('\n'.join(not_matching_text))


if __name__=="__main__":
    key=open(sys.argv[2], 'r').read() # The key file name is the second argument
    text_file=sys.argv[1] # The text file with sentences is the first argument
    main(text_file, key)
