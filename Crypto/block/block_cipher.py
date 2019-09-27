#!/usr/bin/python3

# William 09/2019
# this program will take a textfile and a key as input, encrypt the text using a block permutation cipher.
# The permutation is derived from the key as described in the lab
# it will also perform this encryption vertically as described in the lab. (read the text vertically once it has been split in blocks)
# it also has functions to decrypt both the standard way and vertically.
# this program takes 2 arguments, a file name and a key string

import sys

def file_to_text(file_name):
    text_file=open(file_name, 'r')
    return(text_file.read().replace("\n",""))

def text_string_to_array(text_string, block_size):
    ''' This function will take a string and return an array of strings of length block_size. If needed, the last block will be padded will "Z"'''
#    text_file=open(file_name, 'r') # we opend the file in read mode
    sliced_text=[] # we initialize the resulting array as empty
    current_block="" # we initialize the current block as empty
#    for line in text_file.readlines():
#        line=line.replace('\n', '') # we remove the \n character from the string
    for letter in text_string:
        if len(current_block)==block_size: # if the block is already full we have to add it to the array of blocks before storing the current letter in the new block
            sliced_text.append(current_block) # we append the full block to the result
            current_block=letter # We both empty the current block and store the current letter inside it
        else: # if the block is not empty then we append the current letter to it
            current_block+=letter
    current_block+="Z"*(block_size-len(current_block)) # This will pad the last block with the necessary number of "Z"
    sliced_text.append(current_block) # we add the last bock to the result
    return(sliced_text)

def generate_permutation(key):
    '''
    This function will take a key string as input, generate a dictionary of key:value pairs where the keys are the letters in the ordered key string and the values are arrays containing the list
    '''
    ordered_key=sorted(key) # we sort the key string alphabetically in order to retrieve the indexes
    index_map={} # initially we don't have any index stored
    for i in range(len(key)): # we look at every letter in the key
        if ordered_key[i] in index_map.keys(): # if we already have encountered the letter then we can just append the current index of the letter to the list of indexes of ots occurences
            index_map[ordered_key[i]].append(i)
        else:
            index_map[ordered_key[i]]=[i] # otherwise we have to initilize the list of indexes with the current index
    index_array=[] # we want to put the indexes in correct order so we need an array
    for letter in key:
        index_array.append(index_map[letter].pop()) # this takes the last index in the list of indexes associated to the letter and puts it in the correct place in the permutation array
    return(index_array)

def encrypt(text_array, permutation_table):
    '''
    This function will take the list of blocks and perform the encryption on each block, be careful that this function will not work if the length of the blocks is different from that of the permutation
    '''
    encrypted_text_array=[] # initially we haven't encrypted anything
    for line in text_array: # We treat each block individually
        encrypted_block=[0]*len(line) # we need to be able to fill the block in non-linear order so we need to initialize a non-empty block
        for i in range(len(line)): # we look at each letter in the plaintext block
            encrypted_block[permutation_table[i]]=line[i] # we put this letter at the index specified by the permutation table
        encrypted_text_array.append("".join(encrypted_block)) # in the end we want the block to be a string
    return(encrypted_text_array)

def decrypt(encrypted_text_array, permutation_table):
    '''
    This function takes an array of encrypted blocks and will perform the decryption process on each block using the permutation table provided
    '''
    text_array=[] # at first we haven't decrypted anything, this array will store the decrypted blocks
    for line in encrypted_text_array: # again we treat each block separately
        decrypted_block="" # we initialize the block as empty
        for i in range(len(permutation_table)): # for every index in the encrypted block 
            decrypted_block+=line[permutation_table[i]] # we pull the letter at this index and add it to the plain text block
        text_array.append(decrypted_block)
    return(text_array)

def rotate_array(array, anti=False):
    '''
    This function will take an array of n blocks on size m. It will return a new string of size n*m as if reading the first array vertically.
    example : ["abc", "def"] will be transformed in "adbecf"
    to make it into an array we can just use the function text_string_to_array
    It can also perform the reverse operation if the parameter anti is set to true
    '''
    if not anti: # if we want to rotate the array
        rotated_string=[0]*(len(array)*len(array[0])) # we initialize the result to a big string of 0
        for i in range(len(array)*len(array[0])): # then we put the characters in order so that it will read the first column, then the second etc...
            rotated_string[i]=array[i%len(array)][i//len(array)]
    else: # if we want to do the reverse operation
        complete_string="".join(array) # we start by turning the array into a big string from wich we will extract the letters using arithmetics
        rotated_string="" # initialy the result is empty
        for i in range(len(array)): # we want to recreate as many blocks as before
            for j in range(len(array[0])): # and each block will read the characters separated by len(array)
                rotated_string+=complete_string[i+j*len(array)]
    return(rotated_string)

def main(file_name, key):
    '''
    This function just takes the input and makes the calls to the other functions to display the results to the screen
    '''

    block_size=len(key)    
    text_string=file_to_text(file_name)
    sliced_text=text_string_to_array(text_string, block_size)
    print("Starting the program on", file_name, "using key", key)
    print("\n"+"#"*30+"\n")

    print("Sliced plain text\n")
    print('\n'.join(sliced_text))

    print("\n"+"#"*30+"\n")
    permutation_table=generate_permutation(key)
    print("The permutation table derived from", key, "is \n", permutation_table)
    print("\n"+"#"*30+"\n")

    encrypted_text_array=encrypt(sliced_text, permutation_table)
    print("Encrypted text\n")
    print("\n".join(encrypted_text_array))
    print("\n"+"#"*30+"\n")

    decrypted_text_array=decrypt(encrypted_text_array, permutation_table)
    print("Decrypted text\n")
    print("\n".join(decrypted_text_array))

    rotated_string=rotate_array(sliced_text)
    print("\n"+"#"*30+"\n")
    print("Rotated plain text\n")
    rotated_array=text_string_to_array(rotated_string, block_size)
    print("\n".join(rotated_array))

    print("\n"+"#"*30+"\n")
    print("Encrypted rotated text\n")
    encrypted_rotated=encrypt(rotated_array, permutation_table)
    print("\n".join(encrypted_rotated))

    print("\n"+"#"*30+"\n")
    print("Decrypted rotated text\n")
    decrypted_rotated=decrypt(encrypted_rotated, permutation_table)
    print("\n".join(decrypted_rotated))

    print("\n"+"#"*30+"\n")
    print("Rotated decrypted rotated text\n")
    decrypted_anti_rotated=rotate_array(decrypted_rotated, True)
    decrypted_anti_rotated_array=text_string_to_array(decrypted_anti_rotated, block_size)
    print("\n".join(decrypted_anti_rotated_array))

if __name__=="__main__":
    file_name=sys.argv[1]
    key=sys.argv[2]
    main(file_name, key)
