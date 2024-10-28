from math import sqrt
import string
import numpy as np


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

# Dictionary maniupulation

def sortdict(mydict,mode=1):
    # mode = 0 sorts by key, mode = 1 by value
    
    sorteddict = sorted(mydict.items(),key= lambda item: item[mode])
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

#Frequency counters


def wordfreq(text):
    words = {}
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


def monogramfreq(text,spacesincluded=False):

    if spacesincluded:
        eletters = list(string.ascii_uppercase+' ')
    else:
        eletters = list(string.ascii_uppercase)
        text = text.replace(' ','')
        
    letters = [0] * len(eletters)
        
    for letter in text:
        letters[eletters.index(letter)] += 1
            
    # Makes a list of letters' frequencies
    return letters


def trigramfreq(text,lettersonly=False):
    text = text.upper()
    
    if lettersonly:
        text = formatcorpus(text)
        text = text.replace(' ','')
        text = text.replace('\n','')
    
    trigrams = {}
    
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
        return 'error'
    
    length = len(alpha)
    total = 0
    
    for item in range(length):
        product = alpha[item]*beta[item]
        total += product
    return total

def cosineangle_vectors(a,b):
    # This calcualtes the angle between two vectors
    binner = innerproduct_vectors(b, b)
    abinner = innerproduct_vectors(a, b)
    ainner = innerproduct_vectors(a, a)
    
    denominator = sqrt(ainner*binner)
    
    return abinner/denominator


def monogramfitness(text,s):
    # fb is the frequency of the brown corpus, s with spaces, else without
    if s:
        fb = [381728, 72822, 147237, 188251, 592982, 110706, 92531, 258019, 345777, 7640, 31188, 196168, 120667, 336729, 360310, 95951, 5103, 290953, 310710, 438979, 128805, 47272, 89151, 9439, 81735, 4516, 1002175]
    else:
        fb = [381728, 72822, 147237, 188251, 592982, 110706, 92531, 258019, 345777, 7640, 31188, 196168, 120667, 336729, 360310, 95951, 5103, 290953, 310710, 438979, 128805, 47272, 89151, 9439, 81735, 4516]
    ft = monogramfreq(text,s)
    return (cosineangle_vectors(ft,fb))


# Quadragram fitness

def englishquadragrams(spacesincluded = False, log = False):
    if spacesincluded:
        if log:
            doc = open('english_quadragram_frequencies_spaces_logvalues.txt','r')
        else:
            doc = open('english_quadragram_frequencies_spaces.txt','r')
    else:
        if log:
            doc = open('english_quadragram_frequencies_logvalues.txt','r')
        else:  
            doc = open('english_quadragram_frequencies.txt','r')
    
    f = doc.read()
    f = f.split('\n')
    for a in range(len(f)-1):
        n = f[a]
        n = float(n)
        f[a] = n
    return f

def quadragramfitness(text,equadragrams= englishquadragrams(0,1),spacesincluded = False, scale = True):
    eletters = list(string.ascii_uppercase)
           
    if not spacesincluded:
        # If you don't want spaces
        text = text.replace(' ','')
    else:
        eletters += ' '

    loglist = equadragrams
    sigma = 0.0
        
    for i in range(len(text)-3):
        index = (eletters.index(text[i])*26*26*26) + (eletters.index(text[i+1])*26*26) + (eletters.index(text[i+2])*26) + (eletters.index(text[i+3]))
        sigma += (loglist[index])
    if scale:
        return (sigma)/(len(text)-2)
    return (sigma)

# Index of coincidence

def ioc(text, spacesincluded = False):
    fac = 27
    if not spacesincluded:
        text.replace(' ','')
        fac = 26
        
    df = monogramfreq(text,spacesincluded)
    l = 0
    sigma = 0
    
    for v in df:
        l += v
        sigma += v*(v-1)
    sigma /= (l*(l-1))
    
    return fac * sigma

#g = open('english_quadragram_frequencies_logvalues.txt','w')
#f = open('english_quadragram_frequencies_logvalues.txt','r').read()
#for a in string.ascii_uppercase:
#    f.replace(a,'')
#f.replace(';','')
#g.write(f)
