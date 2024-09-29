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

def cshift(text,shift):
    shift = shift%26
    new_text = ''
    for character in text:
        if character not in letters:
            new_text += character
            continue
        new_character = letters.index(character) + shift
        new_character = letters[new_character%26]
        new_text += new_character
    return new_text

# CODE

cipher = """ZAWN DWNNU, E YWJ'P PDWJG UKQ AJKQCD BKN WHH UKQN OQLLKNP KRAN PDA HWOP BAS UAWNO WJZ SDEHA E SEHH IEOO PDA BNAAHWJYA HEBA, EP EO CKKZ PK XA XWYG EJ PDA KBBEYA SKNGEJC SEPD PDA PAWI. E GJKS EP OQNLNEOAZ UKQ SDAJ E WOGAZ PK NAPQNJ PK PDA WNYDWAKHKCEOPO, XQP E HEGAZ PDA EJPANWYPEKJ SEPD PDA PNWEJAAO WJZ PDANA EO OKIA NAWHHU EJPANAOPEJC OPQBB HQNGEJC EJ PDA WNYDERA. WJUSWU, WBPAN PDA HWOP YKQLHA KB UAWNO E JAAZ OKIA PEIA WSWU BNKI PDA ZWU-PK-ZWU LNAOOQNAO KB HERA WYPEKJ. EB IU IKRA XWYG PK PDA DEOPKNEY BEHAO OQNLNEOAZ UKQ, IU LNKIKPEKJ PK DAWZ KB PDA ZEREOEKJ SWO W YKILHAPA ODKYG PK IA. E OLAJP WJ ARAJEJC SWJZANEJC NKQJZ PDA WNYDERA EJ WSA. E DWZJ'P XAAJ CERAJ BQHH WYYAOO XABKNA WJZ DWZ JK EZAW FQOP DKS YKILNADAJOERA PDA YKHHAYPEKJ SWO. EP SWO W HEPPHA KRANSDAHIEJC WP BENOP, XQP E PDEJG E WI CAPPEJC PDA DWJC KB EP. YDKKOEJC PDA NECDP BEHA WO W PNWEJEJC ATANYEOA EO WJ EJPANAOPEJC YDWHHAJCA, XQP E DKLA E SEHH HAWNJ BNKI PDA PNWEJAAO WO SAHH WO BNKI UKQ. E WI CHWZ UKQ PKKG IU WZREYA WJZ WNA PWGEJC W XNAWG. E DKLA UKQ HEGA PDA IWJOEKJ, E JARAN REOEPAZ, XQP E DWRA OAAJ LDKPKO WJZ NAWZ W HKP WXKQP EP. PDA HEXNWNU EO LWNPEYQHWNHU EJPANAOPEJC ... E WI HKKGEJC BKNSWNZ PK DAWNEJC XWYG BNKI UKQ. ZEZ UKQ CAP PDA WCWPDW YDNEOPEA E OAJP? DKS WNA UKQ GAALEJC XQOU? E WI CQAOOEJC OQZKGQ WJZ YNKOOSKNZO, PDKQCD PDA XKKGODAHRAO IWU XA YWHHEJC PKK OPNKJCHU. SDEYD NAIEJZO IA, I BNKI PDA LQVVHA CNKQL OAJZO DEO XAOP SEODAO. DA DKLAO PK OAA UKQ SDAJ UKQ CAP XWYG, IWUXA WP KQN XHAPYDHAU IAAPEJC. E DWZ XAPPAN CAP KJ SEPD SKNG, XQP LANDWLO UKQ YWJ DAHL IA SEPD OKIAPDEJC? E BKQJZ W OHEL KB LWLAN PQYGAZ EJ KJA KB PDA BEHAO WJZ SDEHA E YWJ AWOEHU ZAYNULP EP, E PDEJG PDANA EO OKIAPDEJC AHOA DEZZAJ EJ EP. IWUXA E SEHH CAP PDA PNWEJAAO PK PWGA W HKKG WP EP WJZ OAA EB PDAU YWJ BEJZ WJUPDEJC. WHH PDA XAOP, FKZEA"""
#char_freq(cipher)

for a in range(26):
    print('shift',a,end=' --> ')
    print(cshift(cipher,a))