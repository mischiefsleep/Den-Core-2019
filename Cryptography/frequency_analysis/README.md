# Frequency analysis

This folder is about deryption methods using frequency analysis.

## frequency_analysis.py

This program implements a frequency analysis decryption method.

It will take one argument as input : the file we want to decrypt.

The program will perform a frequency analysis on the file, map the frequencies to those of letters in the English language and try to decrypt the file.

The file text_file.txt is provided as an example, it has been encrypted with a susbtitution cipher so it is vulnerable to frequency analysis attacks.

## Usage

```bash
python3 frequency_analysis.py text_file.txt
```

## doubles.py

This program will search for the number of occurences of a specific string in a file. This is useful to fine tune the decryption because the frequency analysis is not very precise (it is based on statistics and is subject to bias if the text file is not perfectly representative of the English language).

## More information

There are many comments inside the code, don't hesitate to look at it.

## License
[MIT](https://choosealicense.com/licenses/mit/)
