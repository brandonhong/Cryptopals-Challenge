# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 11:16:44 2018

@author: Brandon

Set 1 Challenge 4
Set 1 challenges available on https://cryptopals.com/sets/1

Given a file that contains several 60-character strings, the task is to find one string that has been xor'd by single-character xor.
Similarly to challenge 3, it will be relatively easy to brute force the cipher using all possible combinations of a byte. A scoring
mechanism is used again to determine the most probable plaintext.
"""
from cryptohacks import *

#First I read in the file associated with the challenge
with open("c4.txt") as f:
    ciphertext = f.readlines()
#Strip all newlines and generate the potential keys
ciphertext = [x.strip() for x in ciphertext]
keys = range(256)

msgs = {}
for line in ciphertext:
    for letter in keys:
        msgLen = len(line)
        try:
            key = ""
            while len(key) != msgLen:
                key += hex(letter)[2:]
            hexTxt = xor(line, key)
            msg = codecs.decode(hexTxt, 'hex').decode('utf8')
        
            #I add the letter used to decode at the end of msg so I can reference it if needed
            msg += chr(letter)
            msgs[msg] = score(msg[:-1], scoresDict)
        except:
            #This is for lines that have 58 characters instead of 60
            pass

decoded = max(msgs, key = msgs.get)
print(decoded[:-1])
print("Key: %s" % decoded[-1])
