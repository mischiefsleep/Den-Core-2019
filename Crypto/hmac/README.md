# HMAC (hash-based message authentication code)

This folder is about veryfying the integrity of data using hashes. 

## hmac_encode.py

This program will verify the integrity of sentence using hashes.

This program takes a text file with the formating <sentence>:<hash> and a key file that contains the key used to compute the hashes
It will compute the hash of the sentence and compare it to the associated hash in the file.

It will take two arguments as input : the file with sentences (keep in mind that it has to be formated using <sentence>:<hash>) and the key used for encryption.

The files sentences.txt and key.key are provided as an example. The file not_matching holds the result of the program as an example of the output.

## Usage

```bash
python3 hmac_encode.py sentences.txt key.key
```

## More information

There are many comments inside the code, don't hesitate to look at it.
If you want to know more about the way the permutations are generated or the meaning of the rotated encryption you can send an email at guilhem.mizrahi<at>secureset.academy.


## License
[MIT](https://choosealicense.com/licenses/mit/)
