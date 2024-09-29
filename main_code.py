# IMPORTS

import string

# VARIABLES
global letters
letters = list(string.ascii_uppercase)

global alphabet
alphabet = {}

keys = [a for a in list(string.printable)]

for key in keys:
    alphabet[key] = 0
# Creates dictionary with (all printable characters) : 0
# The 0 represents the frequency

# FUNCTIONS

def char_freq(text):

    for character in text:
        alphabet[character] += 1

    for freq in range(max(alphabet.values()),0,-1):
        for place in list(string.printable):
            if alphabet[place] == freq:
                print(place, freq)
    # This for loop prints the items in order of frequency, rather than in alphabetical order.

def cshift(text,key):
    key = key%26
    new_text = ''
    for character in text:
        if character not in letters:
            new_text += character
            continue
        new_character = letters.index(character) - key
        new_character = letters[new_character%26]
        new_text += new_character
    return new_text

def allcshifts(text):
    for a in range(26):
        print('shift',a,end=' --> ')
        print(cshift(text,a))

def affineinverse(alpha):
    # a*d = 1 mod 26. We want to find d
    d = 0
    while (alpha*d)%26 != 1:
        d += 1
    return d

def affinedecrypt(text,a,b):
    # y = ax + b
    new_text = ''
    for character in text:
        if character not in letters:
            new_text += character
            continue
        new_character = letters.index(character) - b
        new_character = new_character*affineinverse(a)
        new_character = letters[new_character%26]
        new_text += new_character
    return new_text

def charreplace(text,characters):
    # characters in format [[A,B,C,D,...][A1,B1,C1,..]] A... etc to be replaced with A1...
    for option in range(2):
        new_text = ''
        for character in text:
            if character not in letters:
                new_text += character
                continue
            if character in characters[0]:
                new_character = characters[1][characters[0].index(character)]
                new_text += new_character
            else:
                new_character = character.lower()
                if option == 0:  
                    new_text += new_character
                if option == 1:
                    new_text += '_'
        print(new_text)
        print('')
        print('----------------------------------------------')
        print('')

# CODE

cipher = """HTRTCK TMTCKJ WFMT BFST XK RATFHTH KWFC TMTH KD BT KWFK X FB XC BDHKFA SFCVTH.

TORTEK KWT WFAA XJ WFLCKTS DH X FB VDXCV BFS KWTC X BLJK IT KWT MXRKXB DU F RHLTA WDFO; X UTFH UDH BP JFCXKP FCS BP AXUT.

SLHXCV KWT CXVWK X WTFH JDLCSJ DU ETDEAT NWXJETHXCV, ILK NWTC X JTFHRW, X UXCS CD-DCT.

HDVTHJ KTAAJ BT KWFK X FB XBFVXCXCV XK FAA FCS KWFK X CTTS KD RFAB SDNC, ILK X RFCCDK.

LCATJJ BP ETHJTRLKDH RFC IT UDLCS FCS JKDEETS X NXAA TXKWTH VD BFS DH IT ZXAATS.

BFXJXT XJ KWT DCAP DCT X RFC KHLJK, ILK SD X SFHT JWFHT BP UTFHJ NXKW WTH: NDLAS JWT ITAXTMT BT, FCS NDLAS SDXCV JD ELK WTH XC FJ BLRW SFCVTH FJ X FEETFH KD IT XC?"""


#char_freq(cipher)
#allcshifts(cipher)
#print(affinedecrypt(cipher,3,7))
#print(affineinverse(-15))
chartobereplaced = [['T','U','V','W','K','F','X','A'],['E','F','G','H','T','A','I','L']]
charreplace(cipher,chartobereplaced)


