import string

text = open('brown_corpus_words.txt','r').read()

text = text.upper()
lettersonly = 1


if lettersonly:
    #text = formatcorpus(text)
    text = text.replace('-','')
    text = text.replace(' ','')
    text = text.replace('\n','')

quadragrams = dict()
letters = string.ascii_uppercase
keys = []
for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                keys.append(a+b+c+d)

for key in keys:
    quadragrams[key] = 0


for pos in range(len(text)-4):
    item = text[pos:pos+4]
    if text[pos:pos+4] in quadragrams:
        quadragrams[text[pos:pos+4]] += 1
    else:
        print('ERROR')
        print(item)
        print(pos)
        print(len(text))
        break
        
g = open('english_quadragrams_frequencies.txt','w')
new = ''
for k,v in quadragrams.items():
    new += (k+' '+str(v)+'\n')
g.write(new)