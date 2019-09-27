# Block

This folder is about block cipher encryption methods. 

## block_cipher.py

This program implements a block cipher encryption method based on permutations.

It will take two argument as input : the file we want to encrypt and the key use for encryption. The file is usually a .txt file and the key is usually a string.

The program will split the text in blocks of the same size as the key and encrypt each block with a permutation generated from the key.

The file poem_file.txt is provided as an example.

## Usage

```python
python3 block_cipher.py poem_file.txt STUDENT
```

## More information

There are many comments inside the code, don't hesitate to look at it.
If you want to know more about the way the permutations are generated or the meaning of the rotated encryption you can send an email at guilhem.mizrahi<at>secureset.academy.


## License
[MIT](https://choosealicense.com/licenses/mit/)
