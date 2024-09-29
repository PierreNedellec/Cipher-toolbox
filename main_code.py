# IMPORTS

import string

# VARIABLES

global alphabet
alphabet = {}

keys = [a for a in list(string.printable)]

for key in keys:
    alphabet[key] = 0
# Creates dictionary with (all printable characters) : 0
# The 0 represents the frequency

# FUNCTIONS

def char_freq(text):
    count = [0 for a in alphabet]

    for character in text:
        count[alphabet.index(character)] += 1

    for place in range(len(alphabet)):
        print(alphabet[place],count[place])

# CODE

#char_freq('hello world')
print(alphabet)
