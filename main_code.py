# IMPORTS

import string

# VARIABLES

global alphabet
alphabet = list(string.printable)


# FUNCTIONS

def char_freq(text):
    count = [0 for a in alphabet]

    for character in text:
        count[alphabet.index(character)] += 1

    for place in range(len(alphabet)):
        print(alphabet[place],count[place])

# CODE

char_freq('hello world')
