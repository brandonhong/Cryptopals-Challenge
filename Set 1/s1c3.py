# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 11:11:13 2018

@author: Brandon

Set 1 Challenge 3
Set 1 challenges available on https://cryptopals.com/sets/1

The goal of this challenge is to decrypt a message in hexadecimal by using a single-byte xor cipher. Since the key can be any single-byte,
a scoring mechanism must also be used to determine the most probable plaintext.
"""
from cryptohacks import *

ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
#ciphertext has to be xor'd by a single-byte xor cipher
#I will brute force every xor combination using the chr(x) where x is an int from 0-255
keys = range(256)
msgLen = len(ciphertext)

msgs = {}
for letter in keys:
    key = ""
    while len(key) != msgLen:
        key += hex(letter)[2:]
    hexMsg = xor(ciphertext, key)
    msg = codecs.decode(hexMsg, 'hex').decode('utf8')
    
    #I add the letter used to decode at the end of msg so I can reference it if needed
    msg += chr(letter)
    #I now score the msg based on letter frequnecy and add it to the msgs dictionary
    msgs[msg] = score(msg[:-1], scoresDict)
    
decoded = max(msgs, key = msgs.get)
print(decoded[:-1])
print("Key: %s" % decoded[-1])
