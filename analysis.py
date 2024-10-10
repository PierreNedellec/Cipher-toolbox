from math import sqrt
import string

global english_monogram_frequencies_inner_product
english_monogram_frequencies_inner_product = 1477094937415

global brown_corpus
brown_corpus = open('brown_corpus_words.txt','r').read()


def formatcorpus(text):
    text = text.upper()
    eletters = string.ascii_uppercase + ' '
    
    for a in range(3):
        for j in range(len(text)):
            s = 0
            try:
                if not text[j-s] in eletters:
                    try:
                        text = text.replace(text[j],'')
                        s += 2
                    except:
                        continue
            except:
                continue
        # This checks if a character is in the alphabet, if it isnt, it deletes it. The try statements is because replacement results in an IndexError at the end (because the text is shorter that what it started as.)
    while '  ' in text:
        text = text.replace('  ',' ')
               
    return text

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
    text = text.upper()
    eletters = string.ascii_uppercase + ' '

    if not spacesincluded:
        eletters = string.ascii_uppercase
        
    letters = {}
    for i in eletters:
        letters[i] = 0
        
    for letter in text:
        if letter in eletters:
            letters[letter] += 1
            
    # Makes a dictionary with all the letters with their frequencies
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

global english_monogram_frequencies
english_monogram_frequencies = monogramfreq(brown_corpus,0)

def monogramfitness(text,s):
    ft = dict2valuelist(monogramfreq(text,s))
    fb = dict2valuelist(english_monogram_frequencies)
    if s:
        fb = dict2valuelist(monogramfreq(brown_corpus,s))
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
    quaddict = {}
    
    for item in doc.readlines():
        item = item.replace('\n','')
        item = item.split(';')
        quaddict[item[0]] = item[1]
    return quaddict


def quadragramfitness(text, spacesincluded = False):
    text = formatcorpus(text)
    
    eletters = string.ascii_uppercase
           
    if not spacesincluded:
        # If you don't want spaces
        text = text.replace(' ','')
    else:
        eletters += ' '

    
    logtable = englishquadragrams(spacesincluded,1)
    loglist = dict2valuelist(logtable)
    sigma = 0.0
        
    for i in range(len(text)-3):
        index = (eletters.index(text[i])*26*26*26) + (eletters.index(text[i+1])*26*26) + (eletters.index(text[i+2])*26) + (eletters.index(text[i+3]))
        sigma += (float(loglist[index])/(len(text)-2))
        
    return (sigma)

# Index of coincidence

def ioc(text, spacesincluded = False):
    text = formatcorpus(text)
    fac = 27
    if not spacesincluded:
        text.replace(' ','')
        fac = 26
        
    df = monogramfreq(text,spacesincluded)
    l = 0
    sigma = 0
    
    for k,v in df.items():
        l += v
        sigma += v*(v-1)
    sigma /= (l*(l-1))
    
    return fac * sigma

