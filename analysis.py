from math import sqrt
import string

global english_monogram_frequencies_inner_product
english_monogram_frequencies_inner_product = 1477094937415

global brown_corpus
brown_corpus = open('brown_corpus_words.txt','r').read()


def formatcorpus(text):
    corpus = text
    
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
    corpus = corpus.replace('’','')
    corpus = corpus.replace('“','')
    corpus = corpus.replace('”','')
    corpus = corpus.replace('‘','')
    corpus = corpus.replace('Ï','I')
    corpus = corpus.replace('É','E')
    
    #corpus = corpus.replace('-',' ')
    for a in range(10):
        corpus = corpus.replace(str(a),'')
    # Removing all hyphens that are not in the middle of a word
    while '  ' in corpus:
        corpus = corpus.replace('  ',' ')
    corpus = corpus.upper()
    
    return corpus

# Dictionary maniupulation

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

#Frequency counters


def wordfreq(text):
    words = dict()
    if type(text) == str:
        text = formatcorpus(text)
        text = text.split(' ')
    
    for word in text:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    # Makes a dictionary with all the words with their frequencies
    return words


def monogramfreq(text,lettersonly=True):
    text = text.upper()
    eletters = string.ascii_uppercase

    if lettersonly:
        letters = {}
        for i in eletters:
            letters[i] = 0
            
        for letter in text:
            if letter in eletters:
                letters[letter] += 1
                
        return letters
    
    letters = dict()
    
    for letter in text:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    # Makes a dictionary with all the letters with their frequencies
    return letters


def trigramfreq(text,lettersonly=False):
    text = text.upper()
    
    if lettersonly:
        text = formatcorpus(text)
        text = text.replace(' ','')
        text = text.replace('\n','')
    
    trigrams = dict()
    
    for pos in range(len(text)-2):
        if text[pos:pos+3] in trigrams:
            trigrams[text[pos:pos+3]] += 1
        else:
            trigrams[text[pos:pos+3]] = 1
    # Makes a dictionary with all the trigrams with their frequencies
    return trigrams

# Monogram frequency and vector inner product

def innerproduct_vectors(alpha,beta):
    if len(alpha) != len(beta):
        print('ERROR: vector lengths do not match')
        print('Vector a:',alpha,len(alpha))
        print('Vector b:',beta,len(beta))
        return
    
    length = len(alpha)
    total = 0
    
    for item in range(length):
        product = alpha[item]*beta[item]
        total += product
    return total

def cosineangle_vectors(a,b,c = english_monogram_frequencies_inner_product):
    # This calcualtes the angle between two vectors

    binner = c
    abinner = innerproduct_vectors(a, b)
    ainner = innerproduct_vectors(a, a)
    
    denominator = sqrt(ainner*binner)
    
    return abinner/denominator

global english_monogram_frequencies
english_monogram_frequencies = monogramfreq(brown_corpus,1)

def monogramfitness(text):
    ft = dict2valuelist(monogramfreq(text,1))
    fb = dict2valuelist(english_monogram_frequencies)

    return (cosineangle_vectors(ft,fb))


# Quadragram fitness

def englishquadragrams(spaces = False, log = False):
    if spaces:
        if log:
            doc = open('english_quadragram_frequencies_spaces_logvalues.txt','r')
        else:
            doc = open('english_quadragram_frequencies_spaces.txt','r')
    else:
        if log:
            doc = open('english_quadragram_frequencies_logvalues.txt','r')
        else:  
            doc = open('english_quadragram_frequencies.txt','r')
    quaddict = {}
    
    for item in doc.readlines():
        item = item.replace('\n','')
        item = item.split(';')
        quaddict[item[0]] = item[1]
    return quaddict


def quadragramfitness(text, spaces = False):
    text = text.upper()
    text = formatcorpus(text)
    
    eletters = string.ascii_uppercase
           
    text = text.replace('-','')
    text = text.replace('\n','')
    if not spaces:
        text = text.replace(' ','')
    else:
        eletters += ' '

    
    for j in range(len(text)):
        if not text[j] in eletters:
            try:
                text = text.replace(text[j],'')
            except:
                continue
    # This checks if a character is in the alphabet, if it isnt, it deletes it. The final try statement is because replacement results in an IndexError at the end (because the text is shorter that what it started as.)
            
    qdict = englishquadragrams(spaces,1)
    qlist = dict2valuelist(qdict)
    sum = 0.0
            
    for i in range(len(text)-3):
        quad = eletters.index(text[i])*26*26*26 
        + eletters.index(text[i+1])*26*26
        + eletters.index(text[i+2])*26
        + eletters.index(text[i+3])
        
        sum+= float(qlist[quad])
        
    return (sum/(len(text)-3))

