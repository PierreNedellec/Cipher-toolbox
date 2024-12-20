# IMPORTS
# -*- coding: utf-8 -*-

import string
import analysis
import random
import cProfile
import math
from itertools import product, permutations, cycle
import time

# VARIABLES


# Previously calculated

global brown_corpus
brown_corpus = open('brown_corpus_words.txt','r').read()

global english_letters
english_letters = list(string.ascii_uppercase)

# FUNCTIONS

def ciphertext():
    return open('cipher.txt','r', encoding='utf8').read()

def ciphertext_clean():
    text = open('cipher.txt','r', encoding='utf8').read()
    text = formatcorpus(text)
    text = text.replace(' ','')
    return text

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

def insert_spaces(text):
    text = formatcorpus(text).replace(' ','')
    words = open('english_words.txt','r').read()
    cell = ' '
    new_text = ''
    
    while len(text) != 0:
        cell += text[0]
        text = text[1:]
        if cell in words:
            new_text += cell
            cell = ' '
        if len(cell) > 19:
            new_text += cell
            cell = ' '
    if cell != ' ':
        new_text += cell
    
    return new_text
    

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

def THEclue(raw_text):
    text = formatcorpus(raw_text)
    letterfreq = analysis.monogramfreq(text)
    pos = letterfreq.index(max(letterfreq))
    e = english_letters[pos]
    letterfreq[pos] = 0
    pos = letterfreq.index(max(letterfreq))
    t = english_letters[pos]
    
    return '....'+e+'..............'+t+'......'

def remove_double_letters(word):
    word = list(word)
    letters = list(set(word))
    goal_length = len(letters)
    pops = []
    
    while len(word) != goal_length:
        for num,b in enumerate(word):
            if b in word[:num]:
                pops.append(b)
        
        word = word[::-1]
        for p in pops:
            word.remove(p)
        word = word[::-1]
    return word

def alphabet_keyword_mix(keyword,mode = 0):
    # Mode 0 = WORDEFG... Mode 1 = WORDABCE... Mode 2 = WORDCBAZ... Mode 3 = WORDZYX...
    alphabet = list(string.ascii_uppercase)
    keyword = remove_double_letters(keyword)
    
    if mode == 2 or mode == 3:
        alphabet = alphabet[::-1]
        mode -= 2
        
    if mode == 0:
        last_letter = alphabet.index(keyword[-1])
        mix = keyword + alphabet[last_letter:] + alphabet[:last_letter]
        return remove_double_letters(mix)
    
    if mode == 1:
        mix = keyword + alphabet
        return remove_double_letters(mix)
    
    
def simple_columnar_transposition_encrypt(text,ncolumns,pad = True):
    # Message placed in matrix like so:
    #['T', 'H', 'I', 'S', 'M', 'E', 'S', 'S']
    #['A', 'G', 'E', 'W', 'A', 'S', 'E', 'N']
    #['C', 'R', 'Y', 'P', 'T', 'E', 'D', 'W']
    #['I', 'T', 'H', 'A', 'T', 'R', 'A', 'N']
    #['S', 'P', 'O', 'S', 'I', 'T', 'I', 'O']
    #['N', 'C', 'I', 'P', 'H', 'E', 'R', 'X']
    #Then read off in columns
    
    text = text.replace(' ','')
    character = 'X'
    if not pad:
        character = ' '
    text = pad_text(text, ncolumns, padchar = character)
    nrows = len(text)/ncolumns
    nrows = int(nrows)
    if ncolumns*nrows != len(text):
        print('error in matrix transposition: number of columns, number of rows and length of text do not match')
        
    matrix = [[a for a in range(ncolumns)] for b in range(nrows)]
    for n,letter in enumerate(text):
        column = n%ncolumns
        row = n//ncolumns
        matrix[row][column] = letter
        
    print(matrix)
    newtext = []
    # how to read matrix
    for c in range(ncolumns):
        for r in range(nrows):
            newtext += matrix[r][c]
    
    return ''.join(newtext)

def simple_columnar_transposition_decrypt(text,ncolumns):
    text = text.replace(' ','')
    nrows = len(text)/ncolumns
    nrows = int(nrows)
    if ncolumns*nrows != len(text):
        print('error in matrix transposition: number of columns, number of rows and length of text do not match')
        
    matrix = [[a for a in range(ncolumns)] for b in range(nrows)]
    for n,letter in enumerate(text):
        row = n%nrows
        column = n//nrows
        matrix[row][column] = letter
        
    print(matrix)
    newtext = []
    # how to read matrix
    for c in range(nrows):
        newtext += matrix[c]
    
    return ''.join(newtext)

def generate_psquare(keyword = None,mix = 0,mode = 0, same_letter = 'i/j'):
    #       Mode 0/1              Mode 2/3              Mode 4/5
    #       Across              Vertical            Spiral
    #      0 Left-Right         2 Up-Down           4 In-Out
    #      1 Right-Left         3 Down-Up           5 Out-In
    
    square = [[a for a in range(5)] for b in range(5)]
    alphabet = list(string.ascii_uppercase)
    
    if keyword != None:
        alphabet = alphabet_keyword_mix(keyword,mode = mix)
    
    
    
    return

def double_char_to_one(text):
    translator = dict()
    alphabet = list(string.ascii_uppercase)
    
    for chars in range(0,len(text),2):
        charpair = text[chars:(chars+2)]
        if charpair not in translator.keys():
            translator[charpair] = alphabet[len(translator)]
    
    newtext = ''.join(translator.get(text[c:(c+2)], 'error') for c in range(0,len(text),2))
    # ^adapted version of monoalphabetic_decryption funciton    
    return newtext


def decrypt_psquare(text):
    return auto_monoalphabetic_decrypt(double_char_to_one(text))

def perminverse(perm):
    newperm = [-1]*len(perm)
    for l in range(len(perm)):
        newperm[perm[l]] = l
        
    return newperm

def pad_text(raw_text,block_size,padchar = 'X'):
    text = formatcorpus(raw_text)
    text = text.replace(' ','')
    length = len(text)
    add = length%block_size
    if add > 0:
        add = block_size - add
    
    return (raw_text + (padchar*add))
    

def permutationencrypt(text,key):
    # Text format
    text = formatcorpus(text)
    text = text.replace(' ','')
    # Variables
    period = len(key)
    new_text = ''
    for cellnumber in range(0,len(text),period):
        new_cell = [''] * period
        for position in range(period):
            new_cell[int(key[position])] = text[cellnumber+position]
        new_text += ''.join(new_cell) + ' '
    return new_text


def permutationdecrypt(text,key):
    return permutationencrypt(text,perminverse(key))

def autopermutationdecrypt(text,period):
    text = pad_text(text, period)
    quads = analysis.englishquadragrams(0,1)

    perms = list(permutations(range(period)))
    maxf = -20
    maxkey = []
    maxdecrypt = ''
    for perm in perms:
        decrypt = permutationdecrypt(text,perm)
        fitness = analysis.quadragramfitness(decrypt, quads)
        if fitness>maxf:
            maxf = fitness
            maxdecrypt = decrypt
            maxkey = perm
    return maxkey, maxdecrypt, maxf

def vigenere_tranches(text,block_size):
    tranches = [''] * block_size
    for i,c in enumerate(text):
        tranches[i%block_size] += c 
    return tranches

def vigenere_block_size(text,max_size = 20, threshold = 1.6):
    t = threshold
    text = formatcorpus(text).replace(' ','')
    totaliocs = [0] * max_size
    
    for block in range(2,max_size):
        sumofioc = 0
        slices = vigenere_tranches(text,block)
        for sub in slices:
            sumofioc += analysis.ioc(sub)
        avgofioc = sumofioc / block
        totaliocs[block] = avgofioc
    period = 0
    
    for b, ioc in enumerate(totaliocs):
        if ioc > threshold:
            period = b
            break
    if period == 0:
        period = vigenere_block_size(text,threshold=t-0.1)
    return period

def brute_vigenere_decrypt(text):
    period = vigenere_block_size(text,100)
    letters = string.ascii_uppercase
    maxf = -20
    maxkey = [0] * period
    maxdecrypt = 'notfound'
    combinations = list(product(letters,repeat=period))
    
    for combo in combinations:
        print(combo)
        new_decrypt = vigenere_decrypt(text, combo)
        new_fitness = analysis.quadragramfitness(new_decrypt)
        if new_fitness> maxf:
            maxf = new_fitness
            maxkey = combo
            maxdecrypt = new_decrypt
    
    return maxkey, maxdecrypt, maxf
    
def hill_climb_vigenere(text):
    alphabet = string.ascii_uppercase
    period = vigenere_block_size(text,30)
    best_key = ['A'] * period
    done = False
    
    while not done:
        oldkey = best_key
        for i in range(period):
            current_fitness = analysis.quadragramfitness(vigenere_decrypt(text, best_key))
            for l in range(26):
                candidate_keyword = best_key.copy()
                candidate_keyword[i] = alphabet[l]
                candidate_fitness = analysis.quadragramfitness(vigenere_decrypt(text, candidate_keyword))
                
                if candidate_fitness > current_fitness:
                    best_key = candidate_keyword
                    current_fitness = candidate_fitness

        if oldkey == best_key:
            done = True
            
    return best_key, vigenere_decrypt(text, best_key), analysis.quadragramfitness(vigenere_decrypt(text, best_key))

    
def vigenere_keyword_to_key(keyword):
    key = []
    letters = string.ascii_uppercase
    for letter in keyword:
        key.append(letters.index(letter))
    return key
# make key to keyword asw

def vigenere_decrypt(text,keyword):
    letters = string.ascii_uppercase
    key = vigenere_keyword_to_key(keyword)
    text = formatcorpus(text)
    text = text.replace(' ','')
    period = len(keyword)
    new_text = ''
    
    for position,letter in enumerate(text):
        new_letter_index = (letters.index(letter) - key[position%period])%26
        new_text += letters[new_letter_index]
    
    return new_text

def hill_climb_beaufort(text):
    alphabet = string.ascii_uppercase
    period = vigenere_block_size(text,30)
    best_key = ['A'] * period
    done = False
    
    while not done:
        oldkey = best_key
        for i in range(period):
            current_fitness = analysis.quadragramfitness(beaufort_decrypt(text, best_key))
            for l in range(26):
                candidate_keyword = best_key.copy()
                candidate_keyword[i] = alphabet[l]
                candidate_fitness = analysis.quadragramfitness(beaufort_decrypt(text, candidate_keyword))
                
                if candidate_fitness > current_fitness:
                    best_key = candidate_keyword
                    current_fitness = candidate_fitness

        if oldkey == best_key:
            done = True
            
    return best_key, beaufort_decrypt(text, best_key), analysis.quadragramfitness(beaufort_decrypt(text, best_key))

def beaufort_decrypt(text,keyword):
    letters = list(string.ascii_uppercase)
    key = vigenere_keyword_to_key(keyword)
    text = formatcorpus(text)
    text = text.replace(' ','')
    period = len(keyword)
    new_text = ''
    
    for position,letter in enumerate(text):
        new_letter_index = (letters[::-1].index(letter) + key[position%period]+1)%26
        new_text += letters[new_letter_index]

    return new_text


def railfence_encrypt(text,n_rails,offset = 0):
    rails = [''] * n_rails
    seq = [a for a in range(n_rails)] + [b for b in range(n_rails-2,0,-1)]

    for i,r in enumerate(cycle(seq)):
        if i == len(text) + offset:
            break
        if i < offset:
            continue
        rails[r] += text[i - offset]
        
    return ''.join(rails), rails

def railfence_decrypt(text,n_rails,offset = 0):
    text = list(text)
    template = 'X' * len(text)
    trash, template = railfence_encrypt(template,n_rails,offset)
    text_tranches = []
    seq = [a for a in range(n_rails)] + [b for b in range(n_rails-2,0,-1)]
    new_text = ''

    for tranche in template:
        text_tranches.append(text[:len(tranche)])
        text = text[len(tranche):]
        
    for i,r in enumerate(cycle(seq)):
        if i < offset:
            continue
        if len(text_tranches[r]) == 0:
            break
        new_text += text_tranches[r].pop(0)
    
    return new_text
 
def maximum_offset(text,rails):
    maximum = len(text)
    return min(maximum,(rails*2)-2)    
 
def brute_railfence_decrypt(text):
    range_of_rails = [r for r in range(2,len(text))]    
    maxf = -20
    maxkey = [0,0]
    maxdecrypt = 'not found'
    railsfound = False
    for r in range_of_rails:
        for o in range(maximum_offset(text,r)):
            plaintext = railfence_decrypt(text, r, o)
            fitness = analysis.quadragramfitness(plaintext)
            if fitness > -11 and fitness > maxf:
                maxf = fitness
                maxkey = [r,o]
                maxdecrypt = plaintext
                railsfound = True
        if railsfound:
            return maxkey, maxdecrypt, maxf

            
def brute_permutation_decrypt(text, try_up_to = 8):
    for period in range(1,try_up_to):
        print('Trying period length:',period)
        k, p, f = autopermutationdecrypt(text, period)
        if f > -11:
            print('Plaintext: ',p)
            print('\nFitness: ',f)
            print('\nKey: ',k)
            print('\nBlock size: ',period,'\n')

        

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
    raw_text = formatcorpus(text)
    raw_text = raw_text.replace(' ','')
    key = 'not found'
    decrypt = 'not found'
    for k in range(26):
        fitness = analysis.monogramfitness(raw_text,0)
        if fitness > 0.55:
            decrypt = caesardecrypt(text, k).replace(' ','')
            key = k
        raw_text = caesardecrypt(raw_text,1)
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
    
def bruteaffinedecrypt(raw_text):
    text = formatcorpus(raw_text)
    key = 'not found'
    decrypt = 'not found'
    A = [1,3,5,7,9,11,15,17,19,21,23,25]
    B = [x for x in range(26)]
    maxf = 0
    
    for a in A:
        for b in B:
            canddecrypt = affinedecrypt(text, a, b)
            candfitness = analysis.monogramfitness(canddecrypt, False)
            if candfitness > maxf:
                maxf = candfitness
                maxa = a
                maxb = b
                
    decrypt = affinedecrypt(raw_text, maxa, maxb)
    key = [maxa,maxb]
    
    return key, decrypt, maxf

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
        
def dictionarise_key(key):
    k = {}
    for a in range(25):
        k[string.ascii_uppercase[a]] = key[a]
    return k
    
def sortdict(mydict,mode=1,reverse = True):
    # mode = 0 sorts by key, mode = 1 by value
    
    sorteddict = sorted(mydict.items(),key= lambda item: item[mode])
    if reverse:
        sorteddict = dict(sorteddict[::-1])
    else:
        sorteddict = dict(sorteddict)
    
    return sorteddict

# English letter frequencies (from most common to least)
#ENGLISH_FREQS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def create_initial_key(ciphertext):
    english_freqs = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    # Create initial key based on letter frequencies in ciphertext
    freq_order = ''.join(sorted(set(english_freqs), key=ciphertext.count, reverse=True))
    freq_order = freq_order.replace(' ','')
    return {c: english_freqs[i] for i, c in enumerate(freq_order)}

def score_text(text):
    return analysis.quadragramfitness(text)

def monoalphabetic_decrypt(text, key):
    return ''.join(key.get(c, c) for c in text)

def hill_climb(ciphertext, max_iterations=10000):
    key = create_initial_key(ciphertext)
    best_score = score_text(monoalphabetic_decrypt(ciphertext, key))
    tenpercent = max_iterations//10
    
    for _ in range(max_iterations):
        if _ % tenpercent == 0:
            print(str(_//(tenpercent//10))+'% complete')
        # Randomly swap two letters in the key
        new_key = key.copy()
        a, b = random.sample(list(new_key.keys()), 2)
        new_key[a], new_key[b] = new_key[b], new_key[a]
        
        # Score the new key
        new_score = score_text(monoalphabetic_decrypt(ciphertext, new_key))
        
        # If the new key is better, keep it
        if new_score > best_score:
            key = new_key
            best_score = new_score
    print('100% complete')
    return key

def auto_monoalphabetic_decrypt(text):

    fciphertext = analysis.formatcorpus(text)    
    
    best_key = hill_climb(fciphertext)
    best_key = sortdict(best_key,1,False)
    plaintext = monoalphabetic_decrypt(text, best_key)
    best_fitness = analysis.quadragramfitness(analysis.formatcorpus(plaintext))

    
    return plaintext, best_key, best_fitness
#GUIs


def GUI():
    option = input('''
Welcome to your cipher toolbox.
Select an option:
    (1) Decryption
    (2) Encryption
    (3) Text analysis
    (4) Insert spaces (for plaintexts)
    ''')
              
    if option == '1':
        GUI_decrypt()
    elif option == '2':
        GUI_encrypt()
    elif option == '3':
        GUI_analysis()
    elif option == '4':
        print(insert_spaces(ciphertext()))
    elif option == 't':
        # INSERT TEST FUNCTION
        print(simple_columnar_transposition_decrypt(ciphertext(), 8))
    else:
        GUI()
    
def GUI_decrypt():
    option = input('''
Select an option:
    (1) Caesar decrypt
    (2) Affine decrypt
    (3) Monoalphabetic substitution decryption
    (4) Polyalphabetic cipher decryption
    (5) Permutation decryption
    (6) Railfence decryption
    (7) Polybius square
    (0) Back to main menu
    ''')
                   
    if option == '1':
        solved = brutecaesardecrypt(ciphertext())
        print('Plaintext:',solved[1])
        print('\nKey:',solved[0])
    elif option == '2':
        solved = bruteaffinedecrypt(ciphertext())
        print('Plaintext:',solved[1])
        print('\nKey:',solved[0])
        print('\nFitness:',solved[2])
    elif option == '3':
        GUI_monoalphabetic_decryption()
    elif option == '5':
        GUI_permutation_decryption()
    elif option == '4':
        GUI_polyalphabetic_decryption()
    elif option == '6':
        GUI_railfence_decryption()
    elif option == '7':
        GUI_polibius_square_decryption()
    elif option == '0':
        GUI()
    else:
        GUI_decrypt()
        
def GUI_encrypt():
    option = input('''
Select an option:
    (1) Permutation encryption
    (0) Back to main menu
    ''')
                   
    if option == '1':
        keyinput = input('''
Enter key each item separated by a comma:
    ''')
        print(permutationencrypt(ciphertext(), keyinput.split(',')))
    elif option == '0':
        GUI()
    else:
        GUI_decrypt()

def GUI_monoalphabetic_decryption():
    option = input('''
Select an option:
    (1) Help for hand decryption
    (2) Automatic decryption
    (3) Decryption (known key)
    (0) Back to main menu
    ''')
                   
    if option == '1':
        monoalphabetickeyword_help()

    elif option == '2':
        plaintext, best_key, best_fitness = auto_monoalphabetic_decrypt(ciphertext())
        print(f"\nDecrypted text: {plaintext}")
        print(f"\nFitness: {best_fitness}")
        print(f"\nKey: {''.join(best_key.keys())}")
        
    elif option == '3':
        print('''Input key:
ABCDEFGHIJKLMNOPQRSTUVWXYZ''')
        print(monoalphabetic_decrypt(ciphertext(),dictionarise_key(input())))
        
    elif option == '0':
        GUI()
    else:
        GUI_monoalphabetic_decryption()
        
def GUI_permutation_decryption():
    option = input('''
Select an option:
    (1) Automatic decryption
    (2) Decryption (known period)
    (3) Decryption (known key)
    (0) Back to main menu
    ''')
                   
    if option == '1':
        brute_permutation_decrypt(ciphertext(),11)

    elif option == '2':
        p = input('''
Enter the period:
    ''')    
        solved = autopermutationdecrypt(ciphertext(), int(p))
        print(solved[1])
        print('key:',solved[0])
        
    elif option == '3':
        keyinput = input('''
Enter key each item separated by a comma:
    ''')
        print(permutationdecrypt(ciphertext(), keyinput.split(',')))
        
    elif option == '0':
        GUI()
    else:
        GUI_permutation_decryption()
    
def GUI_polyalphabetic_decryption():
    option = input('''
Select an option:
    (1) Automatic Vigenère decryption
    (2) Automatic Beaufort decryption
    (3) Coming soon (quagmire)
    (0) Back to main menu
    ''')
                   
    if option == '1':
        best_key, plaintext, best_fitness = hill_climb_vigenere(ciphertext_clean())
        print(f"\nDecrypted text: {plaintext}")
        print(f"\nFitness: {best_fitness}")
        print(f"\nKey: {''.join(best_key)}")

    elif option == '2':
        best_key, plaintext, best_fitness = hill_climb_beaufort(ciphertext_clean())
        print(f"\nDecrypted text: {plaintext}")
        print(f"\nFitness: {best_fitness}")
        print(f"\nKey: {''.join(best_key)}")
        
    elif option == '3':
        print('''Input key:
ABCDEFGHIJKLMNOPQRSTUVWXYZ''')
        print(monoalphabetic_decrypt(ciphertext(),input()))
        
    elif option == '0':
        GUI()
    else:
        GUI_monoalphabetic_decryption()        
        
def GUI_railfence_decryption():
    option = input('''
Select an option:
    (1) Automatic decryption
    (2) Decryption (known key)
    (0) Back to main menu
    ''')
                   
    if option == '1':
        best_key, plaintext, best_fitness = brute_railfence_decrypt(ciphertext_clean())
        print(f"\nDecrypted text: {plaintext}")
        print(f"\nFitness: {best_fitness}")
        print(f"\nRails: {best_key[0]}  Offset: {best_key[1]}")

    elif option == '2':
        rails = input('''
Enter the number of rails:
    ''')    
        off = input('''\nEnter the offset:
    ''')
        solved = railfence_decrypt(ciphertext_clean(), int(rails),int(off))
        print(solved)
        
    elif option == '3':
        keyinput = input('''
Enter key each item separated by a comma:
    ''')
        print(permutationdecrypt(ciphertext(), keyinput.split(',')))
        
        
    elif option == '0':
        GUI()
    else:
        GUI_railfence_decryption()   


def GUI_polibius_square_decryption():
    option = input('''
Select an option:
    (1) Automatic polibius squre decryption
    (0) Back to main menu
    ''')               

    if option == '1':
        plaintext, best_key, best_fitness = auto_monoalphabetic_decrypt(double_char_to_one(ciphertext().replace(' ','')))
        print(f"\nDecrypted text: {plaintext}")
        print(f"\nFitness: {best_fitness}")
        
    elif option == '0':
        GUI()
    else:
        GUI_monoalphabetic_decryption()

         
def GUI_analysis():
    # variable s is 1/True to include spaces, 0/False to exclude them
    s = input('''Include spaces?
    (0) No
    (1) Yes''')
    if s == '1':
        s = True
    if s == '0':
        s = False 
    mf = analysis.monogramfitness(ciphertext_clean(),s)
    qf = analysis.quadragramfitness(ciphertext_clean(), analysis.englishquadragrams(s,1), spacesincluded = s)
    ioc = analysis.ioc(ciphertext_clean(),s)
    mf = round(mf,3)
    qf = round(qf,2)
    ioc = round(ioc,3)
    print('''Performing analysis...
    Monogram fitness:''',str(mf),'Eng: 0.996, Rand: 0.76' + '''
    Quadragram fitness:''',str(qf),'Eng: -9.6, Rand: -18.3'+'''
    Index of coincidence:''',str(ioc),'''Eng: 1.7, Rand: 1.0
    (Reference values assume spaces are excluded)''')
    

def monoalphabetickeyword_help():
    key = list(input('''Enter key. Use - for unknowns. 
ABCDEFGHIJKLMNOPQRSTUVWXYZ
'''))
    englishkey = []
    cipherkey = []
    eletters = list(string.ascii_uppercase)
    if len(key) != 26:
        key = THEclue(ciphertext())
        print(key)
    for l in key:
        if l in eletters:
            cipherkey.append(l)
            englishkey.append(eletters[key.index(l)])
    charreplace(ciphertext(),[cipherkey,englishkey])
    monoalphabetickeyword_help()

# CODE

#cProfile.run('print(hill_climb_monoalphabetic(ciphertext()))')
GUI()
#cProfile.run('print(hill_climb_vigenere(ciphertext()))')

