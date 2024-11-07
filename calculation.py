import string
from math import log

def sortdict(mydict,mode=1,invert=0):
    # mode = 0 sorts by key, mode = 1 by value
    
    sorteddict = sorted(mydict.items(),key= lambda item: item[mode])
    if not invert:
        sorteddict = dict(sorteddict[::-1])
    if invert:
        sorteddict = dict(sorteddict)
    # Sorts the dictionary using the key: it looks at the second variable in the dictionary entry. Thats what the lambda function does.
            
    return sorteddict


def quadragrams():
    text = open('brown_corpus_words.txt','r').read()

    text = text.upper()
    lettersonly = 1
    
    
    if lettersonly:
        #text = formatcorpus(text)
        text = text.replace('-','')
        #text = text.replace(' ','')
        text = text.replace('\n','')
    
    quadragrams = dict()
    letters = string.ascii_uppercase+' '
    keys = []
    for a in letters:
        for b in letters:
            for c in letters:
                for d in letters:
                    keys.append(a+b+c+d)
    
    for key in keys:
        quadragrams[key] = 0
    
    
    for pos in range(len(text)-3):
        item = text[pos:pos+4]
        if item in quadragrams:
            quadragrams[item] += 1
        
    for k,v in quadragrams.items():
        quadragrams[k] = v/(len(text)-3)
            
    g = open('english_quadragram_frequencies_spaces.txt','w')
    new = ''
    for k,v in quadragrams.items():
        new += (k+';'+str(v)+'\n')
    g.write(new)
    
    
def englishquadragrams(spaces = False):
    if spaces:
        doc = open('english_quadragram_frequencies_spaces.txt','r')
    else:
        doc = open('english_quadragram_frequencies.txt','r')
    quaddict = {}
    
    for item in doc.readlines():
        item = item.replace('\n','')
        item = item.split(';')
        quaddict[item[0]] = item[1]
    return quaddict


def addlogs():
    original = englishquadragrams(1)
    new = ''
    
    for k,v in original.items():
        v = float(v)
        if v ==0:
            v = -20
        else:
            v = log(v)
        new += (str(v)+'\n')  
        
    g = open('english_quadragram_frequencies_spaces_logvalues.txt','w')
    g.write(new)
    
#addlogs()

e = open('english_words.txt','w')
f = open('english_words_frequencies.txt','w')
corpus = open('brown_corpus_words.txt','r').read().split(' ')

frequencies = {}

for word in corpus:
    try:
        frequencies[word] += 1
    except KeyError:
        frequencies[word] = 1

frequencies = sortdict(frequencies)
new = ''

for k,v in frequencies.items():
    new += (k+';'+str(v)+'\n')
f.write(new)


frequencies = sortdict(frequencies,0,1)
for letter in 'BCDEFGHJKLMNOPQRSTUVWXYZ':
    del frequencies[letter]
new = []
for k,v in frequencies.items():
    if v > 0:
        new.append(k)
e.write(' '.join(new))
