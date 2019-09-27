# MD5 Brute Force

This folder is about brute force decryption methods. 

## brute_force_md5.py

This program implements a brute force method to crack hashes from a list of hashes.

It will take three arguments as input : the file containing the list of hashes, the name of the ouput file to store the cracked hashes and the alphabet (the list of characters the program is going to use to generate the possible passwords).

In the case of this program it is assumed that the passwords are 5 charachters long.

The files hashes.txt and alphabet.txt are provided as an example.
The list of cracked hashes is in cracked_hashes.txt. To get this output it took 74 minutes on a Intel i5 1.8GHz CPU.

## Usage

```bash
python3 brute_force_md5.py hashes.txt cracked_hashes.txt alphabet.txt
```

## More information

There are not too many comments in this code for now but hopefully they will be added soon.

## License
[MIT](https://choosealicense.com/licenses/mit/)
