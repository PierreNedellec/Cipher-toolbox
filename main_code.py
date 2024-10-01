# IMPORTS
# -*- coding: utf-8 -*-

import string

# VARIABLES
global letters
letters = list(string.ascii_uppercase)

global alphabet
alphabet = {}

keys = [a for a in list(string.printable)]

for key in keys:
    alphabet[key] = 0
# Creates dictionary with (all printable characters) : 0
# The 0 represents the frequency

# FUNCTIONS

def char_freq(text):

    for character in text:
        alphabet[character] += 1

    for freq in range(max(alphabet.values()),0,-1):
        for place in list(string.printable):
            if alphabet[place] == freq:
                print(place, freq)
    # This for loop prints the items in order of frequency, rather than in alphabetical order.

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
    
def formatcorpus(corpus):
    punctuation = list(string.punctuation).remove('-',"'")
    for item in punctuation:
        corpus = corpus.replace(item,'')
    corpus = corpus.replace("""'s""",'')
    corpus = corpus.replace('\n',' ')
    while '  ' in corpus:
        corpus = corpus.replace('  ',' ')
    corpus = corpus.upper()
    return corpus

# CODE

cipher = """AREIR JKZVJ JJKPY RJVZL JKEAZ VKKUE KVNEJ LBGCB MVBGR ADPPC LIGYE VZKUE KNRNC LYASV BAEBP KUVBT CSBCK RVBKU RMCYL ZRKUE KPCLJ RBKZR PCLEI RIVTU KKUEK VKUEJ JCZRM EYLRE JEJFR GVEYR AVKVC BCSFC RJNCI XDLKV GCLYA BCKJR REBPK UVBTI RZEIX EDYRE DCLKV KKUEK ZVTUK ROFYE VBKUR FIRJR BGRCI KURAR EKUCS KURPC LBTZE BPCLS CLBAV BKURY VDIEI PVKVJ ESVBR JFRGV ZRBEB AVKNE JNVKU JCZRI RYLGK EBGRK UEKVE KKEGX RAKUR DVBAV BTEJV AVABC KROFR GKKCS VBAEB PKUVB TIRZE IXEDY RKURI RVBPC LGEBV ZETVB RZPJL IFIVJ RKURB KCAVJ GCMRI KUREK KEGUR ABCKR GYREI YPNIV KKRBV BEGVF URIEB AGEIR SLYYP GCBGR EYRAD RKNRR BKURY REKUR IEBAK URRBA DCEIA JRMRB KURBV EJJLZ RAKUV JKCDR EFLDY VJURI JKIVG XKCFI CZCKR KURRA VKVCB TVMRB KURFI CZVBR BGRCS RBGIP FKVCB VBKUR KEYRD LKGCB JLYKV BTNVK UZPSI VRBAJ VBKUR DCCXK IEARB CBRCS KURZU EAURE IACSJ LGUEG CBGRV KEBAV GCLYA BCKSV BAEBP IRGCI ACSEB EAMRI KVJVB TGEZF EVTBI RSRII VBTKC JLGUE GLIVC JVKPE KKUVJ FCVBK VSRYK VJUCL YAEKY REJKE KKRZF KKCAR GVFUR IKURZ RJJET REBAH LVGXY PAVJG CMRIR AKUEK KUREL KUCIU EALJR AKURM RIPZV YAGCB MRBKV CBCSE JUVSK GVFUR IGYRE IYPVB KRBAR AKCDR DICXR BKURS VIJKY VBRIR EAIRG RBKRM RBKJU EMRZE ARVKG YREIR IKUEB RMRIK CZRKU EKVEZ VBZCI KEYAE BTRIE BAKUR IRJKG CBKEV BRAZL GUKCE YEIZZ RRJFR GVEYY PKURI EKURI GYLZJ PIRMR IJREG ICJKV GNUVG UIREA ZLIAR IKUCL TUSCI KURYC BTRJK KVZRV EJJLZ RAVKK CIREA IRAIL ZNUVG UGELJ RAZRZ LGUGC BSLJV CBNUR KURIC IBCKK UVJGC BGREY RAZRJ JETRF CVBKJ KCKUR LBSCI KLBEK RAREK UCSPC LIVBK RIYCF RIVJB CKEFF EIRBK KCZRD LKVKU VBXPC LEIRI VTUKK UEKVK JFIRJ RBGRJ UCLYA DRJLS SVGVR BKKCR BGCLI ETRKU RFCYV GRKCI RCFRB KURGE JRVNV YYSCI NEIAE GCFPC SKUVJ YRKKR IKCTR KURIN VKUZP SVBAV BTJKC ZPSIV RBAKC ZUEIF RIEJG UVRSC SFCYV GRURJ UCLYA UEMRK URFCN RIEBA VBSYL RBGRK CACJC NVKUZ PDRJK NVJUR JZELI VGRAI ZELIV GRNUV KRZA"""


f = open('brown.txt','w')
f.write(formatcorpus(open('brown.txt','r').read()))

