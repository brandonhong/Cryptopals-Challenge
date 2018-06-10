# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 11:01:58 2018

@author: Brandon

Set 1 Challenge 2
Set 1 challenges available on https://cryptopals.com/sets/1

The goal of this challenge is to get familiar with exclusive or'ing or xor'ing. Plaintext in hexadecimal will be xor'd with a key 
of the same character length to produce the ciphertext.
"""
from cryptohacks import *

plaintext = "1c0111001f010100061a024b53535009181c"
key = "686974207468652062756c6c277320657965"
#The key when decoded from hex should be "hit the bull's eye"
#And the ciphertext should be "the kid don't play" when decoded from hex
#The message should be "746865206b696420646f6e277420706c6179" in hex

ciphertext = xor(plaintext, key)
assert ciphertext == "746865206b696420646f6e277420706c6179", "Something went wrong!"