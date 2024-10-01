# IMPORTS
# -*- coding: utf-8 -*-

import string

# VARIABLES



global brown_corpus
brown_corpus = open('brown_corpus_words.txt','r').read()
brown_corpus = brown_corpus.split(' ')

global letters
letters = list(string.ascii_uppercase)

# FUNCTIONS

def charfreq(text):
    letters = dict()
    text = text.split(' ')
    
    for letter in text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    # Makes a dictionary with all the words with their frequencies
    
    sortedletters = sorted(letters.items(),key= lambda item: item[1])
    sortedletters = dict(sortedletters[::-1])
    # Sorts the dictionary using the key: it looks at the second variable in the dictionary entry. Thats what the lambda function does.
            
    return sortedletters

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
        
def monoalphabeticdecrypt(text,key):
    key = list(key)
    
    new_text = ''
    for character in text:
        if character not in letters:
            new_text += character
            continue
        new_character = letters[key.index(character)]
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
    
    sortedwords = sorted(words.items(),key= lambda item: item[1])
    sortedwords = dict(sortedwords[::-1])
    # Sorts the dictionary using the key: it looks at the second variable in the dictionary entry. Thats what the lambda function does.
            
    return sortedwords

# CODE

cipher = """text"""



g = open('english_words_frequencies.txt','w')
f = wordfreq(brown_corpus)
f = f.keys()
n = ''

for a in f:
    a += ' '
    n += a

g.write(n)






