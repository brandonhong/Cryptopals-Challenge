# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 10:59:47 2018

@author: Brandon
This script contains the set of functions that are used for the cryptopals challenges. It mainly relies on the codecs library.
"""
import codecs


#Below is the letter frequency in the English language
#Second column in %
with open("letterscore.txt") as f:
    scores = f.readlines()
scores = [x.strip() for x in scores]
scoresDict = {}
#Now convert scores into a dictionary
for line in scores:
    i = line.split("\t")
    scoresDict[i[0]] = float(i[1])
#Add an additional score for white space, which is a little more common than the letter "e"
scoresDict[" "] = 15.0

def decodeHex(hexString):
    '''Decodes a hex string to utf8'''
    return codecs.decode(hexString, 'hex').decode('utf8')

def decodeb64(b64):
    '''Decodes a base 64 string to utf8'''
    return codecs.decode(str.encode(b64), 'base 64').decode('utf8')

def hex2b64(hexString):
    '''Converts a hex string to base 64 string. First the hex string is decoded to binary. Then the binary is encoded to base 64.
    Last the base 64 is decoded to utf8 for readability'''
    return codecs.encode(codecs.decode(hexString, 'hex'), 'base64').decode('utf8')

def xor(hexString, key):
    '''Performs exclusive or (xor) on two hex strings of the same length. First the two hex strings are converted to base 64. 
    Then I utilize the zip function to iterate over both strings one element at a time and xor them.
    Last, I encode back to hex and decode to utf8 for readability.'''
    message = "".join(chr(a ^ b) for a, b in zip(codecs.decode(hexString, 'hex'), codecs.decode(key, 'hex')))
    return codecs.encode(str.encode(message), 'hex').decode('utf8')

def score(string, scoresDict):
    '''Scores the string based on frequency using the scoresDict. Score is rounded to 2 decimal places'''
    score = 0
    for c in string:
        if c in scoresDict:
            score += scoresDict.get(c)
    return round(score, 2)

def hamming(s1, s2, datatype):
    '''Returns the bitwise Hamming distance between two equal length strings. Both strings are converted to binary first.
    The datatype variable specifies whether the strings are in utf8 or hexadecimal format.
    For "this is a test" and "wokka wokka!!!", the function returns 37.'''
    if len(s1) != len(s2):
        return None
    scale = 16 #hexadecimal
    if datatype == "utf8":
        bS1 = bin(int(codecs.encode(str.encode(s1), 'hex'), scale))[2:]
        bS2 = bin(int(codecs.encode(str.encode(s2), 'hex'), scale))[2:]
    elif datatype == "hex":
        bS1 = bin(int(s1, scale))[2:]
        bS2 = bin(int(s2, scale))[2:]
    bits = int(8 * round(float(len(bS1))/8))
    bS1 = bS1.zfill(bits)
    bS2 = bS2.zfill(bits)
    return sum(a != b for a, b in zip(bS1, bS2))