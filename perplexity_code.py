# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:32:13 2024

@author: pierr
"""
def sortdict(mydict,mode=1,reverse = True):
    # mode = 0 sorts by key, mode = 1 by value
    
    sorteddict = sorted(mydict.items(),key= lambda item: item[mode])
    if reverse:
        sorteddict = dict(sorteddict[::-1])
    else:
        sorteddict = dict(sorteddict)
    
    return sorteddict

# PERPLEXITY GAVE ME THIS CODE

import random
from collections import Counter
import analysis

# English letter frequencies (from most common to least)
ENGLISH_FREQS = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
#ENGLISH_FREQS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def create_initial_key(ciphertext):
    # Create initial key based on letter frequencies in ciphertext
    freq_order = ''.join(sorted(set(ENGLISH_FREQS), key=ciphertext.count, reverse=True))
    freq_order = freq_order.replace(' ','')
    return {c: ENGLISH_FREQS[i] for i, c in enumerate(freq_order)}

def score_text(text):
    # Score text based on English letter frequencies
    return analysis.quadragramfitness(text)

def decrypt(ciphertext, key):
    return ''.join(key.get(c, c) for c in ciphertext)

def hill_climb(ciphertext, max_iterations=10000):
    key = create_initial_key(ciphertext)
    best_score = score_text(decrypt(ciphertext, key))
    
    for _ in range(max_iterations):
        print(_)
        # Randomly swap two letters in the key
        new_key = key.copy()
        a, b = random.sample(list(new_key.keys()), 2)
        new_key[a], new_key[b] = new_key[b], new_key[a]
        
        # Score the new key
        new_score = score_text(decrypt(ciphertext, new_key))
        
        # If the new key is better, keep it
        if new_score > best_score:
            key = new_key
            best_score = new_score
    
    return key

def auto_monoalphabetic_decrypt():
    # Sample ciphertext (encrypted "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")
    ciphertext = """MPSF ZVGG KSFBP,
HUSBX NCI QCF NCIF YPHHPF SBM HUP VBHFVRIVBR DIOOYP HUSH NCI GPBH ZP. V USJP MVGAIGGPM VH KVHU ZN AYCGP QFVPBM SBM ACYYSTCFSHCF ZF AUSFYPG TSTTSRP, SBM KP SFP TCHU CQ HUP CDVBVCB HUSH VH VG S ZNGHPFN HUSH MPZSBMG S YVHHYP ZCFP ACBHPLH VQ KP SFP HC TP CQ SBN SGGVGHSBAP HC NCI. KP UCDP HUSH KP SFP STYP HC UPYD NCI, TIH KP SFP GCZPKUSH IBAPFHSVB KUPHUPF HUVG VG GCZPHUVBR HUSH MPZSBMG CIF VZZPMVSHP SHHPBHVCB. VQ GC UCK MC NCI DFCDCGP HUSH KP GUCIYM DFCAPPM? PJPB KVHU HUP VZDFCJPZPBHG VB HFSBGSHYSBHVA HFSQQVA VH KVYY HSXP GCZP HVZP HC VBJPGHVRSHP HUVG ZSHHPF TN DCGH SBM V SZ SQFSVM KP SFP GHVYY GCZP KSN QFCZ HUP VBHFCMIAHVCB CQ HUP HFSBGSHYSBHVA HPYPRFSDU. (HUCIRU CIF QFVPBM ZF KUPSHGHCBP VG KCFXVBR SYY UCIFG HC USGHPB HUSH MPJPYCDZPBH.) KP KCIYM TP RFSHPQIY VQ NCI ACIYM FPDYN KVHU SBN QIFHUPF VBQCFZSHVCB HUSH ZSN UPYD IG.
CB HUP ZSHHPF CQ HUP TIYYPH, ZF TSTTSRP USG GIRRPGHPM HUP DCGGVTVYVHN HUSH HUP YPHHPFVBR ZVRUH TP CQ QCFPVRB CFVRVB, TIH KP SFP BCH SKSFP CQ S YSBRISRP VB KUVAU HUVG ACZTVBSHVCB CQ YSHVB ACBGCBSBHG ACIYM GVRBVQN SB PLDFPGGVTYP KCFM. UP GIRRPGHPM SYGC HUSH HUP AUSFSAHPFG ZVRUH TP HUCGP CQ SB SAFCBNZ, HUCIRU HUP YSAX CQ DIBAHISHVCB SBM HUP FPYSHVJPYN YSFRP BIZTPF CQ YPHHPFG ZSXPG HUVG, HCC, IBYVXPYN.
KP SFP HUPB TFCIRUH HC HUP DCGGVTVYVHN, KUVAU V SZ GIFP NCI USM VB ZVBM, HUSH HUP HPLH CB HUP ASGP ZVRUH FPDFPGPBH GCZP QCFZ CQ PBANDUPFPM ACZZIBVASHVCB. HUP GUCFHBPGG CQ HUP HPLH DFPGPBHG S GVRBVQVASBH DFCTYPZ. KP SFP IBSTYP HC SDDYN CIF IGISY HPAUBVEIPG CQ QFPEIPBAN SBSYNGVG HC MPHPFZVBP SBN DSHHPFB, SBM KVHUCIH ZCFP ACBHPLH KP USJP BC AFVTG CF CHUPF AYIPG HC VHG YVXPYN ZPSBVBR. VB NCIF YPHHPF NCI ZPBHVCBPM HUSH HUP TIYYPH KSG QCIBM VB S GUVDDVBR KSFPUCIGP BPSF S GHSAX CQ GPSYPM AFSHPG, SBM HUSH HUPGP KPFP TCIBM QCF PBRYSBM. KP KCIYM QVBM VH ZCGH UPYDQIY VQ NCI ACIYM HPYY IG, GUCIYM NCI XBCK, HUP ACBHPBHG CQ HUCGP AFSHPG, HUP VBMVJVMISY CF ACFDCFSHVCB HC KUVAU HUPN TPYCBR SBM HUP FPAVDVPBH QCF KUCZ HUPN SFP CF KPFP VBHPBMPM.
V SZ GCFFN VH USG HSXPB GC YCBR QCF ZP HC FPDYN HC NCI, TIH ZF TSTTSRP VG UPSJVYN VBJCYJPM VB HUP DFPDSFSHVCBG QCF HUP VBHPFBSHVCBSY QSVF HC TP UPYM YSHPF VB HUP NPSF. RVJPB HUP DFVBAP ACBGCFH’G VBJCYJPZPBH NCI ASB VZSRVBP HUSH HUPFP SFP UVRU PLDPAHSHVCBG CB SYY CQ HUCGP KUC SFP VBJCYJPM VB VHG MPYVJPFN. TP SGGIFPM UCKPJPF HUSH KP KVYY RVJP CIF QIYY SHHPBHVCB HC NCIF FPDYN SBM KP UCDP HC TP STYP HC SGGVGH NCI.
KVHU CIF JPFN TPGH KVGUPG,
SMS YCJPYSAP SBM AUSFYPG TSTTSRP"""

    fciphertext = analysis.formatcorpus(ciphertext)    

    print(f"Ciphertext: {ciphertext}")
    
    best_key = hill_climb(fciphertext,2000)
    best_key = sortdict(best_key,1,False)
    plaintext = decrypt(ciphertext, best_key)
    
    print(f"\nDecrypted text: {plaintext}")
    print(f"\nFitness: {analysis.quadragramfitness(analysis.formatcorpus(plaintext))}")
    print(f"\nKey: {''.join(best_key.keys())}")
    
if __name__ == "__main__":
    main()