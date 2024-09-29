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

# CODE

cipher = """HTRTCK TMTCKJ WFMT BFST XK RATFHTH KWFC TMTH KD BT KWFK X FB XC BDHKFA SFCVTH.

TORTEK KWT WFAA XJ WFLCKTS DH X FB VDXCV BFS KWTC X BLJK IT KWT MXRKXB DU F RHLTA WDFO; X UTFH UDH BP JFCXKP FCS BP AXUT.

SLHXCV KWT CXVWK X WTFH JDLCSJ DU ETDEAT NWXJETHXCV, ILK NWTC X JTFHRW, X UXCS CD-DCT.

HDVTHJ KTAAJ BT KWFK X FB XBFVXCXCV XK FAA FCS KWFK X CTTS KD RFAB SDNC, ILK X RFCCDK.

LCATJJ BP ETHJTRLKDH RFC IT UDLCS FCS JKDEETS X NXAA TXKWTH VD BFS DH IT ZXAATS.

BFXJXT XJ KWT DCAP DCT X RFC KHLJK, ILK SD X SFHT JWFHT BP UTFHJ NXKW WTH: NDLAS JWT ITAXTMT BT, FCS NDLAS SDXCV JD ELK WTH XC FJ BLRW SFCVTH FJ X FEETFH KD IT XC?"""
#char_freq(cipher)
allcshifts(cipher)
