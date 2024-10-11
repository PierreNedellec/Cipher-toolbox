# IMPORTS
# -*- coding: utf-8 -*-

import string
import analysis
import random
import cProfile

# VARIABLES


# Previously calculated

global brown_corpus
brown_corpus = open('brown_corpus_words.txt','r').read()

global english_letters
english_letters = list(string.ascii_uppercase)

# FUNCTIONS

def ciphertext():
    return open('cipher.txt','r', encoding='utf8').read()


def formatcorpus(text):
    text = text.upper()
    eletters = list(string.ascii_uppercase + ' ')
    
    new = ''
    for j in text:
        if j in eletters:
            new += j
    
    while '  ' in new:
        new = new.replace('  ',' ')
    # This checks if a character is in the alphabet, if it isnt, it deletes it. The try statements is because replacement results in an IndexError at the end (because the text is shorter that what it started as.)
            
    return new


def sortdict(mydict):
    # Will sort dictionaries according to their value, not their key
    
    sorteddict = sorted(mydict.items(),key= lambda item: item[1])
    sorteddict = dict(sorteddict[::-1])
    # Sorts the dictionary using the key: it looks at the second variable in the dictionary entry. Thats what the lambda function does.
            
    return sorteddict



def dict2valuelist(mydict):
    out = []
    for keys, values in mydict.items():
        out.append(values)
    return out

def dict2keylist(mydict):
    out = []
    for keys, values in mydict.items():
        out.append(keys)
    return out



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


def brutecaesardecrypt(text):
    key = 'not found'
    decrypt = 'not found'
    for k in range(26):
        if analysis.quadragramfitness(text,0) > -10:
            decrypt = text
            key = k
        text = caesardecrypt(text,1)
        # Rotates the shift by 1 every time
    return  key,decrypt


def affineinverse(alpha):
    # a*d = 1 mod 26. We want to find d
    d = 0
    while (alpha*d)%26 != 1:
        d += 1
    return d


def affinedecrypt(text,a,b):
    text = text.upper()
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


def autoaffinedecrypt(text):
    key = 'not found'
    decrypt = 'not found'
    t = sortdict(analysis.trigramfreq(text,1))
    crib_the = dict2keylist(t)[0]
    # Most common trigram identified.
    # Must also check this crib w/ monogram frequency
    
    # x denotes plaintext letter. y denotes encrypted letter. alpha and beta are the keys. y = alphax + beta
    xone = english_letters.index('T')
    xtwo = english_letters.index('E')
    yone = english_letters.index(crib_the[0])
    ytwo = english_letters.index(crib_the[2])
    # alpha(xtwo-xone) = ytwo-yone
    diffx = (xtwo - xone)%26
    diffy = (ytwo - yone)%26
    alpha = (diffy * affineinverse(diffx))%26
    # Instead of dividing, which we can't do in modular arithmetic, both sides are multiplied by a number, which gives the same practical result as dividing in normal arithmetic.
    beta = ((ytwo - (alpha*xtwo)%26))%26
    key = [alpha,beta]
    decrypt = affinedecrypt(text,key[0],key[1])
    
    return key, decrypt
    


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
    new_text = ''
    for character in text:
        if character not in english_letters:
            new_text += character
            continue
        new_character = english_letters[key.index(character)]
        new_text += new_character
    return new_text
    
    
def hill_climb_monoalphabetic(text):
    quads = analysis.englishquadragrams(0,1)
    text = formatcorpus(text)
    text = text.replace(' ','')
    parent = list(string.ascii_uppercase)
    parent_plaintext = monoalphabeticdecrypt(text, parent)
    parent_fitness = analysis.quadragramfitness(parent_plaintext,quads, 0)
    counter = 0
    while counter<5000:
       # if counter%20 == 0:
        #    print('working...')
         #   print('counter:',counter)
          #  print('current fitness:',parent_fitness)
        counter+=1
        child = parent
        x = random.randint(0,25)
        y = random.randint(0,25)
        if x == y:
            continue
        # Swap letters
        temp = child[x]
        child[x] = child[y]
        child[y] = temp
        # Calculate new fitness
        child_plaintext = monoalphabeticdecrypt(text, child)
        child_fitness = analysis.quadragramfitness(child_plaintext,quads, 0)
        # Compare parent and child keys
        if child_fitness > parent_fitness:
            counter = 0
            parent = child
            parent_plaintext = child_plaintext
            parent_fitness = child_fitness
    return parent_plaintext, parent, parent_fitness
        
#GUIs


def GUI():
    option = input('''
Welcome to your cipher toolbox.
Select an option:
    (1) Decryption
    (2) Encryption
    (3) Text analysis
    ''')
              
    if option == '1':
        GUI_decrypt()
    elif option == '2':
        GUI_encrypt()
    elif option == '3':
        GUI_analysis()
    else:
        GUI()
    
def GUI_decrypt():
    option = input('''
Select an option:
    (1) Caesar decrypt
    (2) Affine decrypt
    (3) Keyword cipher help
    (4) Back to main menu
    ''')
                   
    if option == '1':
        solved = brutecaesardecrypt(ciphertext())
        print(solved[1])
        print('key:',solved[0])
    elif option == '2':
        solved = autoaffinedecrypt(ciphertext())
        print(solved[1])
        print('key:',solved[0])
    elif option == '3':
        monoalphabetickeyword_help()
    elif option == '4':
        GUI()
    else:
        GUI_decrypt()
        
def GUI_encrypt():
    print('Feature coming soon.')
    GUI()
    
    
def GUI_analysis():
    # variable s is 1/True to include spaces, 0/False to exclude them
    s = input('''Include spaces?
    (0) No
    (1) Yes''')
    if s == '1':
        s = True
    if s == '0':
        s = False 
    mf = analysis.monogramfitness(ciphertext(),s)
    qf = analysis.quadragramfitness(ciphertext(),s)
    ioc = analysis.ioc(ciphertext(),s)
    mf = round(mf,3)
    qf = round(qf,2)
    ioc = round(ioc,3)
    print('''Performing analysis...
    Monogram fitness:''',str(mf),'Eng: 0.996, Rand: 0.76' + '''
    Quadragram fitness:''',str(qf),'Eng: -9.6, Rand: -18.3'+'''
    Index of coincidence:''',str(ioc),'''Eng: 1.7, Rand: 1.0
    (Reference values assume spaces are excluded)''')
    

def monoalphabetickeyword_help():
    print('Feature coming soon')
    GUI()

# CODE

cProfile.run('print(hill_climb_monoalphabetic(ciphertext()))')


