# IMPORTS

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
        
def alphabeticcipherdecrypt(text,key):
    key = list(key)
    
    new_text = ''
    for character in text:
        if character not in letters:
            new_text += character
            continue
        new_character = letters[key.index(character)]
        new_text += new_character
    print(new_text)

# CODE

cipher = """

EATI WCEVA,
UCN EVE KUA KITVBAAJ SAK CB? V TJJLZA KUAP RITRXAE KUA RVFUAIJ, HLK FAIUTFJ KUAP JKILSSYAE NVKU NUTK KUA YAKKAI KCYE KUAZ. PCL BAAE KC XBCN GLVKA T HVK THCLK KUA LJ KC LBEAIJKTBE NUTK NTJ SCVBS CB.
ZP CNB IATEVBS VJ KUTK KUA CNBAI CD KUA YVHITIP NUAIA KUA HCEP NTJ DCLBE NTJ FYTBBVBS CB ZCLBKVBS T RTZFTVSB KC SAK AYARKAE TJ SCMAIBCI CD KUA JKTKA HLK NTJ NCIIVAE KUTK TBP JRTBETY ZVSUK LBEAIZVBA UVJ RUTBRAJ. UA JAAZJ KC UTMA HAAB CB SCCE KAIZJ NVKU KUA YCRTY RUVAD CD FCYVRA, TBE JVBRA KUTK VJ TYJC TB AYARKAE FCJVKVCB, KUAP NVYY UTMA HCKU LBEAIJKCCE NUTK NTJ TK JKTXA.
V ELS TICLBE TBE DCLBE KUTK KUA RUVAD, KCZ UTIFAI, UTE T IAFLKTKVCB TJ TB UCBAJK ZTB, HLK UVJ WLESAZABK ZVSUK UTMA HAAB VBDYLABRAE HP UVJ DIVABEJUVF NVKU ICSAIJ, TBE KUA DTRK KUTK KUA FCYVRA NAIA IAYLRKTBK KC VBMAJKVSTKA ZVSUK UTMA UTE ZCIA KC EC NVKU ZTBFCNAI JUCIKTSAJ KUTB TBP LBELA VBDYLABRA. V RUARXAE KUAVI TIRUVMAJ TBE KUAIA VJ JCZA AMVEABRA KUTK UTIFAI RTIIVAE CLK GLVAK ABGLVIVAJ CD UVJ CNB, FAIUTFJ TDKAI UA IARAVMAE KUA YAKKAI DICZ ICSAIJ. V NCBEAIAE VD KUTK NTJ ELA EVYVSABRA, HLK VK ZVSUK TYJC HA HARTLJA UA IARAVMAE T JKITBSA YAKKAI DICZ T YCRTY ECRKCI NUC JAAZAE KC UTMA HAAB TJJVJKVBS KUA YVHITIVTB, ZTVJVA JKPYAJ, NVKU UAI CNB VBMAJKVSTKVCB VBKC KUA RTJA. V TZ JKVYY LBJLIA NUP JUA NTJ VBMCYMAE. JUA NCIXAE VB ICSAIJ' UCLJAUCYE TBE NTJ KUA CBA NUC DCLBE KUA HCEP, HLK VK ECAJ JAAZ T YVKKYA THCMA UAI FTP SITEA KC HA YTLBRUVBS TB VBMAJKVSTKVCB VBKC KUA RVIRLZJKTBRAJ CD KUA EATKU. KUA RLIIABK CNBAI CD KUA UCLJA IAZAZHAIJ UAI SITBEDTKUAI KTYXVBS THCLK ZVJJ ZTVJVA VB DCBE KCBAJ. JUA NCIXAE UAIA LBKVY JUA NTJ BC YCBSAI THYA KC EC JC TBE NTJ T EVYVSABK YVHITIVTB NUC HLVYK KUA RCYYARKVCB DICZ SCCE KC SIATK. (VK VJ JKVYY AORAYYABK, TBE V UTMA BCK UTE KVZA KC JKTIK T RICJJNCIE CI T JLECXL JVBRA V EVJRCMAIAE VK!)
FAIUTFJ JUA NTJ LFJAK KUTK JCZACBA UTE HICXAB KUA JTBRKVKP CD UAI ECZTVB TBE WLJK NTBKAE KC LBEAIJKTBE NUP. JUA ZLJK UTMA HAAB NCIIVAE THCLK KUA JARLIVKP CD KUA RCYYARKVCB TBE VK NCLYE UTMA HAAB DILJKITKVBS KUTK KUA FCYVRA EVE BCK TFFATI MAIP VBKAIAJKAE. JUA JAAZJ KC UTMA TJXAE KUA YCRTY ECRKCI ZTLIVRA NUVKA KC VBMAJKVSTKA KUA MCYLZA DCLBE VB KUA EARATJAE'J SITJF; SVMAB UVJ DVBEVBSJ, KUTK NTJ T SCCE RTYY. V TZ BCK JLIA NUTK UVJ YAKKAI KAYYJ LJ, HLK CBRA PCL UTMA HICXAB KUA ABRIPFKVCB CB VK FAIUTFJ PCL RTB YAK ZA XBCN NUTK PCL KUVBX.
V UCFA PCL EVEB'K ZVBE ZA ABRIPFKVBS KUVJ BCKA. V KUCLSUK PCL TBE KUA KITVBAAJ ZVSUK ABWCP HIATXVBS VK. VK VJ SCCE FITRKVRA DCI KUA YAKKAI DICZ EI ZTLIVRA NUVKA ZE!
TYY KUA HAJK,
UTIIP"""


#char_freq(cipher)
#allcshifts(cipher)
#print(affinedecrypt(cipher,3,7))
#print(affineinverse(-15))
#chartobereplaced = [list('THREADSUVWXYZBCFGIJKLMNOPQ'),list(string.ascii_uppercase)]
#charreplace(cipher,chartobereplaced)

alphabeticcipherdecrypt(cipher,'THREADSUVWXYZBCFGIJKLMNOPQ')


