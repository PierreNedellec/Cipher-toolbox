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


# CODE

cipher = """MCT RFJJFXU KGFTW.
NFGNPOHMFXU: KXJJ HZTUM MGHFUTT NXCXGM
NN: CHGGB
FU TFZCMTTU UFUTMB-JFY, HM H RHUJFXU FU AGXSFQTUNT, GCXQT FJOHUQ, MCT OFKGHGFHU RHFJFT JMBOTJ WXPUQ H KXQB HM MCT WXXM XW MCT OFKGHGB OHQQTG. MCT QTNTHJTQ VHJ NOPMNCFUZ H JRHOO KPM SHOPHKOT KXXL MCHM CHQ KTTU MHLTU WGXR MCT MXA JCTOW, AGTJPRHKOB KTWXGT MCT HNNFQTUM.
MCT KXXL VHJ OTHMCTG-KXPUQ, XUT XW MCT TFZCM SXOPRTJ FU MCT JX-NHOOTQ HRXUMFOOHQX TQFMFXU, JFZUTQ KB MCT APKOFJCTG. MCT AXOFNT VTGT NHOOTQ HUQ, WXOOXVFUZ MCTFG FUSTJMFZHMFXUJ, QTMTGRFUTQ MCHM MCT JMGHUZTG CHQ WHOOTU MX CFJ QTHMC VCFOT MGBFUZ MX JMTHO MCT KXXL. MCT TUDPFGB JTTRJ MX CHST KTTU NOXJTQ VFMCFU H WTV QHBJ. UX XMCTG XWWFNFHO QXNPRTUMJ CHST KTTU WXPUQ FU MCT AXOFNT WFOTJ NXUNTGUFUZ MCT NHJT TYNTAM H NCHFU XW OTMMTGJ WGXR MCT OFKGHGFHU, PGZFUZ MCT AXOFNT MX GT-XATU MCT NHJT.
XPG FUMTGTJM FU MCFJ XMCTGVFJT GXPMFUT FUSTJMFZHMFXU VHJ MGFZZTGTQ KB MCT QFJNXSTGB XW H CFJMXGFN GTDPTJM WXG FUWXGRHMFXU HKXPM MCT QTNTHJTQ, JTUM KB AFULTGMXU'J QTMTNMFST HZTUNB MX MCT RTMGXAXOFMHU AXOFNT. XPG WFTOQ HZTUM QFSFJFXU, MCT OHRAOFZCMTGJ, HGT VXGLFUZ MX WFUQ HUQ GTMGFTST HUB WPGMCTG NXGGTJAXUQTUNT HJJXNFHMTQ VFMC MCT NHJT, KPM JX WHG CHST XUOB GTNXSTGTQ MCT HMMHNCTQ OTMMTG. FM HAATHGJ MX KT VGFMMTU KB MCT XVUTG XW MCT OFKGHGB, GXZTGJ, HUQ JTUM MX MCT AGXSFQTUNT, GCXQT FJOHUQ NCFTW XW AXOFNT. FM FJ OFZCMOB TUNGBAMTQ PJFUZ H JPKJMFMPMFXU NFACTG VFMC H LTBVXGQ QTGFSTQ WGXR MCT MFMOT XW XUT XW MCT JCXGM JMXGFTJ FU MCT UXSTOOH WXPUQ HM MCT JNTUT.
BXPG WFGJM RFJJFXU FJ MX QTNFACTG MCHM OTMMTG. BXP NHU RHLT PJT XW MCT KXJJ JPKJMFMPMFXU NFACTG HAA HUQ MCT OTMMTG WGTDPTUNB NXPUMTG XU XPG NFACTG MXXOJ AHZT FW MCHM FJ CTOAWPO.
ZXXQ OPNL,
IXQFT"""


#char_freq(cipher)
#allcshifts(cipher)
print(affinedecrypt(cipher,3,7))
#print(affineinverse(-15))



