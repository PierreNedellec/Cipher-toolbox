import math
import string
from main_code import dict2valuelist, englishquadragrams



def quadragramfitness(text, spaces = False):
    text = text.upper()
    
    eletters = string.ascii_uppercase
           
    text = text.replace('-','')
    text = text.replace('\n','')
    if not spaces:
        text = text.replace(' ','')
    else:
        eletters += ' '
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

print(math.e**quadragramfitness(open('brown_corpus_words.txt','r').read()[:2000000]))