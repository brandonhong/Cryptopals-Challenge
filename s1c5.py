# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 11:27:25 2018

@author: Brandon

Set 1 Challenge 5
Set 1 challenges available on https://cryptopals.com/sets/1

The goal of this challenge is to implement repeating-key xor using the key "ICE", given the plaintext. 
"""
from cryptohacks import *

plaintext = b"Burning 'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal"
key = b"ICE"
#Given the plaintext and key, the first thing to do is encode the plaintext in hex
hextext = codecs.encode(plaintext, 'hex').decode('utf8')
textLen = len(hextext)
#Repeat this for the key
hexKey = codecs.encode(key, 'hex').decode('utf8')

#The next task is to repeat the key to the same length as the hex encoded text
repKey = hexKey * (textLen//len(hexKey) + 1)
repKey = repKey[:textLen]

#Last we generate the ciphertext using the xor function in cryptohacks
ciphertext = xor(hextext, repKey)
#The ciphertext should be "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
assert ciphertext == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f", "Something went wrong!"