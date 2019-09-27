#!/usr/bin/python3

# william
# This program takes a text file as argument. It will perform a frequency analysis of the letters of the text, create a permutation table mapping the result of the frequency analysis to the frequencies of letters in the english language. This permutation table will be used to try and decrypt the text file provided using a permutation cypher.
# The accuracy of the frenquency analysis method is not enough to perfectly decrypt the text file. In order the completely decrypt, some manual changes have been made to the table. This lead to the hardcoded table that actually matches the permutation table used for encryption.
# The result of the decryption will be written to a file called "decrypted_<file_name>.txt"
import sys

def take_second_elem(array): # This function will be used for sorting an array along the second element using the sort function
    return(array[1])

def permutation_table(dictionary, frequency_table):
    '''This function takes a dictionary (we will use this with the frequency dictionary later) and an array (we will use this with the array of letters in english sorted by frequency later) and returns a permutation table.'''
    array_dictionary=[] # we need to be able to iterate and keep the order so we need to cast our dictionary into an array
    for key in dictionary.keys():
        array_dictionary.append([key, dictionary[key]]) # we simply store every 'key':'value' pair in an array
    array_dictionary.sort(key=take_second_elem, reverse=True) # we can sort this array in descending order along the second element (to match the structure of the frequency table for english provided
    conversion_table={} # in this dictionary we wil the permutation table
    for i in range(len(array_dictionary)): # We create a dictionary of {'encrypted_letter': 'plain_letter'}
        conversion_table[array_dictionary[i][0]]=frequency_table[i] # we map the letter at rank i in the frequency table with the letter at rank i in our fequency analysis
    return(conversion_table)

def pretty(occurences, frequencies):
    '''
    This function will simply print to the screen a dictionary in a pretty way, we will use it to display the frequency table
    '''
    print("Letter".ljust(7), "Occurences".ljust(11), "Frequencies".ljust(12))
    for key in sorted(occurences.keys()):
        print(str(key).ljust(7), str(occurences[key]).ljust(11), str(round(frequencies[key], 2)).ljust(12))

def frequency_analysis(file_name):
    '''
    This function will calculate the frequency of occurence of each charachter in the text file who's name is provided as argument and return this table as a dictionary
    '''
    try:
        plain_text=open(file_name, "r") # open the file in read mode
    except:
        print("File not found") # if the file can't be opened then exit the program
        return(1)
    occurences = {} # initially the table is empty, it will hold key:value pairs where the key is a character and the value is its number of occurences
    total_letters=0 # we will need to count the total number of letters to compute the approximate of the frequency
    for line in plain_text.readlines(): # for each line of the text file
        for letter in line: # for each letter in the line
            if(letter!=' '): # we only want to process letters not spaces
                total_letters+=1 # increment the number of letters
                if letter in occurences.keys(): # if the letter has already been encountered then we just want to increment the counter
                    occurences[letter]+=1 # increment the value of the count of the letter
                else: # if the letter has never been encountered then we want to initialize the count to 1
                    occurences[letter]=1
    frequencies={} # we create a new dictionary (in case we still want to keep the one with occurences and not overwrite it)
    for letter in occurences.keys(): # for every letter encountered we want to compute the frequency
        frequencies[letter]=occurences[letter]/total_letters # the frequency is simple the number of occurences/total number of letters
    pretty(occurences, frequencies) # we want to display the result to the screen using the pretty function
    plain_text.close() # close the file
    return(frequencies)

def decrypt_file(file_name, conversion_table):
    '''
    This function takes a file name as input and a permutation table. It will open the text file, change all the letters according to the permutation table and write the result to a new file.
    '''
    try: # we try to open the text files
        encrypted_text=open(file_name, "r") # the input file
        decrypted_text=open("decrypted_"+file_name, "w+") # the output file
    except:
        print("File not found") # if the files cannot be opend then exit the program
        return(1)
    for line in encrypted_text.readlines(): # we look at the lines in the file
        for letter in line: # then at each letter in the line
            if(letter!=' '): # if it is not a space then we try to decryptthe letter
                decrypted_text.write(conversion_table[letter]) # so we write to the output the letter corresponding to the plaintext version according to the permutation table
            else:
                decrypted_text.write(' ') # otherwise we simply write the space
    encrypted_text.close() # we close the files
    decrypted_text.close()
    return(0)


def main():
#    frequency_table=['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'U', 'C', 'M', 'W', 'F', 'Y', 'G', 'P', 'B', 'V', 'K', 'X', 'J', 'Q', 'Z']
    # this table is the table of frequencies in the english language
    frequency_table=['E', 'T', 'A', 'O', 'S', 'I', 'N', 'H', 'R', 'L', 'D', 'M', 'U', 'C', 'G', 'Y', 'F', 'W', 'P', 'B', 'V', 'K', 'X', 'J', 'Q', 'Z']
    # This frequency table is the result of manually tweaking the table so it would correctly decrypt the text with the result of our frequency analysis.
    frequencies=frequency_analysis(sys.argv[1]) # we run the frequency analysis on the file provided as argument
    conversion_table=permutation_table(frequencies, frequency_table) # we create the permutation table
    print(conversion_table)
    decrypt_file(sys.argv[1], conversion_table) # we run the decryption algorithm with the permutation table produced before

if __name__ == '__main__':
    main()













