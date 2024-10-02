# IMPORTS
# -*- coding: utf-8 -*-

import string
from math import sqrt

# VARIABLES



global brown_corpus
brown_corpus = open('brown_corpus_words.txt','r').read()

global letters
letters = list(string.ascii_uppercase)

# FUNCTIONS

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
    
    sortedletters = sorted(letters.items(),key= lambda item: item[1])
    sortedletters = dict(sortedletters[::-1])
    # Sorts the dictionary using the key: it looks at the second variable in the dictionary entry. Thats what the lambda function does.
            
    return sortedletters

def caesardecrypt(text,key):
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
    abinner = innerproduct_vectors(a, b)
    ainner = innerproduct_vectors(a, a)
    binner = innerproduct_vectors(b, b)
    
    denominator = sqrt(ainner*binner)
    
    return abinner/denominator


def brutecaesardecrypt(text):
    return

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

def dict2valuelist(mydict):
    out = []
    for keys, values in mydict.items():
        out.append(values)
        
    return out

# CODE

cipher = """Prime Minister Sir Keir Starmer has paid back more than £6,000 worth of gifts and hospitality received since becoming prime minister, following a backlash over donations.

The prime minister is covering the cost of six Taylor Swift tickets, four tickets to the races and a clothing rental agreement with a high-end designer favoured by his wife, Lady Victoria Starmer.

It comes after Sir Keir and other cabinet ministers have faced weeks of criticism for accepting freebies from wealthy donors.

Sir Keir has committed to tightening the rules around ministerial hospitality to improve transparency.

Speaking in Brussels on Wednesday, the prime minister said his government would bring forward new principles for donations "as until now politicians have used their best individual judgement to decide".

"I took the decision that until those principles were in place it was right to repay these particular payments,” he said.

Earlier, a Downing Street spokesperson confirmed that the ministerial code will be updated and will include “a new set of principles on gifts and hospitality” commissioned by Sir Keir.

"Ahead of the publication of the new code, the prime minister has paid for several entries on his own register.

"This will appear in the next register of members' interests."

The gifts Starmer has paid for include four Taylor Swift tickets from Universal Music Group worth £2,800, two from the Football Association at a cost of £598, and four to Doncaster Races from Arena Racing Corporation at £1,939.

An £839 clothing rental agreement with Edeline Lee, the designer recently worn by his wife to London Fashion Week, along with one hour of hair and makeup, was also covered by the prime minister.

Sir Keir has also accepted a further £6,134 in "clothing and personal support" for Lady Starmer in June, from Labour donor Lord Alli.

The details of the donations have been published, external in the latest register of interests for MPs on Wednesday.

It comes as Parliament's standards watchdog said Lord Alli was being investigated over allegedly failing to register interests.

A complaint was made during the last week about the Labour donor, who has been at the centre of a row over his donations to Sir Keir and other MPs.

Sir Keir has said he will not accept donations of clothing as prime minister.

When asked about the Lord Alli probe, he said: "I'm not going to comment on Lord Alli. The investigation will run its course."

Last month, Sir Keir told the BBC he had accepted the donation for clothing in opposition, during a "busy election campaign".

The latest register of interest also shows Deputy Prime Minister Angela Rayner declared £836 in hospitality as a "visit to (a) DJ booth".

The registration relates to a trip to a nightclub where Rayner was filmed dancing and being cheered on by the crowd over summer.

The name of the donor listed on the latest register of interests is Ayita LLC."""


ft = charfreq(cipher,1)
fb = charfreq(brown_corpus,1)

print(cosineangle_vectors(dict2valuelist(ft), dict2valuelist(fb)))




