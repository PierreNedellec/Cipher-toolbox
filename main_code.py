# IMPORTS
# -*- coding: utf-8 -*-

import string
from math import sqrt

# VARIABLES



global brown_corpus
brown_corpus = open('brown_corpus_words.txt','r').read()


global english_letters
english_letters = list(string.ascii_uppercase)

# FUNCTIONS

def sortdict(mydict):
    # Will sort dictionaries according to their value, not their key
    
    sorteddict = sorted(mydict.items(),key= lambda item: item[1])
    sorteddict = dict(sorteddict[::-1])
    # Sorts the dictionary using the key: it looks at the second variable in the dictionary entry. Thats what the lambda function does.
            
    return sorteddict



def charfreq(text,lettersonly=False):
    text = text.upper()
    
    if lettersonly:
        keys = list(string.ascii_uppercase)
        letters = dict()
        for i in keys:
           letters[i] = 0
        
        for letter in text:
            if letter in letters:
                letters[letter] += 1
            else:
                continue
    
    else:
        letters = dict()
        text = text.split(' ')
        
        for letter in text:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    # Makes a dictionary with all the words with their frequencies
    
    return letters




global english_monogram_frequencies
english_monogram_frequencies = charfreq(brown_corpus,1)




def caesardecrypt(text,key):
    text = text.upper()
    
    key = key%26
    new_text = ''
    for character in text:
        if character not in english_letters:
            new_text += character
            continue
        new_character = english_letters.index(character) - key
        new_character = english_letters[new_character%26]
        new_text += new_character
    return new_text

def innerproduct_vectors(alpha,beta):
    
    if len(alpha) != len(beta):
        print('ERROR: vector lengths do not match')
        print('Vector a:',alpha)
        print('Vector b:',beta)
        return
    
    length = len(alpha)
    total = 0
    
    for item in range(length):
        product = alpha[item]*beta[item]
        total += product
    return total

def cosineangle_vectors(a,b):
    # This calcualtes the angle between two vectors
    abinner = innerproduct_vectors(a, b)
    ainner = innerproduct_vectors(a, a)
    binner = innerproduct_vectors(b, b)
    
    denominator = sqrt(ainner*binner)
    
    return abinner/denominator


def brutecaesardecrypt(text):
    key = 'not found'
    decrypt = 'not found: try decreasing the threshold'
    for k in range(26):
        if monogramfitness(text) > 0.8:
            decrypt = text
            key = k
        text = caesardecrypt(text,1)
        # Rotates the shift by 1 every time
    
    
    
    return decrypt, key

def allcaesars(text):
    for a in range(26):
        print('shift',a,end=' --> ')
        print(caesardecrypt(text,a))

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
        if character not in english_letters:
            new_text += character
            continue
        new_character = english_letters.index(character) - b
        new_character = new_character*affineinverse(a)
        new_character = english_letters[new_character%26]
        new_text += new_character
    return new_text

def charreplace(text,characters):
    # characters in format [[A,B,C,D,...][A1,B1,C1,..]] A... etc to be replaced with A1...
    for option in range(2):
        new_text = ''
        for character in text:
            if character not in english_letters:
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
        
def monoalphabeticdecrypt(text,key):
    key = list(key)
    
    new_text = ''
    for character in text:
        if character not in english_letters:
            new_text += character
            continue
        new_character = english_letters[key.index(character)]
        new_text += new_character
    print(new_text)
    
def formatcorpus(file):
    corpus = open(file,'r').read()
    
    pun = string.punctuation
    pun = list(pun)
    
    for item in pun:
        if item == '-' or item == "'":
            continue        
        corpus = corpus.replace(item,'')
        
    corpus = corpus.replace("""'s""",'')
    corpus = corpus.replace("""s'""",'s')
    corpus = corpus.replace("'",'')
    corpus = corpus.replace('\n',' ')
    corpus = corpus.replace('- ',' ')
    corpus = corpus.replace(' -',' ')
    #corpus = corpus.replace('-',' ')
    # Removing all hyphens that are not in the middle of a word
    while '  ' in corpus:
        corpus = corpus.replace('  ',' ')
    corpus = corpus.upper()
    
    return corpus

def wordfreq(text):
    words = dict()
    if type(text) == str:
        text = text.split(' ')
    
    for word in text:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    # Makes a dictionary with all the words with their frequencies
    
    return words

def dict2valuelist(mydict):
    out = []
    for keys, values in mydict.items():
        out.append(values)
        
    return out

def monogramfitness(text):
    ft = charfreq(text,1)
    fb = english_monogram_frequencies

    return (cosineangle_vectors(dict2valuelist(ft), dict2valuelist(fb)))


# CODE

cipher = open('cipher.txt','r').read()


text, ky = brutecaesardecrypt(cipher)
print(text)
print('key:',ky)



