# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 10:58:41 2018

@author: Brandon

Set 1 Challenge 2
Set 1 challenges available on https://cryptopals.com/sets/1

The goal of this challenge is to convert a string of hexadecimals into a string of base 64.
"""
from cryptohacks import *

hexS = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
#When decoded from hex, hexS should produce "I'm killing your brain like a poisonous mushroom"
b64 = hex2b64(hexS)
print(b64)
#Should produce "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
assert b64.strip('\n') == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t", "Something went wrong!"

#LIkewise, going backwards should return hexS
def b642hex(b64):
    '''Converts a base 64 string to hex string. First the base 64 string is decoded to binary. Then the binary is encoded to hex.
    Last the hex is decoded to utf8 for readability.'''
    return codecs.encode(codecs.decode(str.encode(b64), 'base64'), 'hex').decode('utf8')
print(b642hex(b64))
