#!/usr/bin/python3

# Guilhem Mizrahi 09/2019

import sys
import hashlib
import itertools

def generate_and_compare(list_of_hashes, output_file, alphabet):
    count_hit=0
    total_hashes=len(list_of_hashes)
    output=open(output_file, 'a+')
    list_of_cracked_hashes=[]
    for word in itertools.product(alphabet, repeat=5):
        word=''.join(word)
        hashed_word=hashlib.md5(word.encode()).hexdigest()
        if hashed_word in list_of_hashes:
            count_hit+=1
            list_of_cracked_hashes.append(word+" : "+hashed_word)
            print(word, count_hit, total_hashes)
    output.write("\n".join(list_of_cracked_hashes))
    output.close()

def main(input_file, output_file, alphabet_file):
    list_of_hashes=set(open(input_file, 'r').read().split("\n"))
    alphabet=open(alphabet_file, 'r').read().replace("\n", "")
    generate_and_compare(list_of_hashes, output_file, alphabet)

if __name__=="__main__":
    input_file=sys.argv[1]
    output_file=sys.argv[2]
    alphabet_file=sys.argv[3]
    main(input_file, output_file, alphabet_file)
