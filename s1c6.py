# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 11:34:31 2018

@author: Brandon

Set 1 Challenge 6
Set 1 challenges available on https://cryptopals.com/sets/1

The goal of this challenge is to decipher the ciphertext given in a text file format. The file is based 64'd AFTER being encrypted by
some repeating-key xor cipher. The length and value of the key is not given. Thus, the Hamming distance will be used to systematically
determine the correct length of the key. Keysize will be brute forced from lengths 2-40 and Hamming distance will be averaged and
standardized. The keysize producing the smallest Hamming distance is likely the correct length.

A Background on the Hamming Distance
The Hamming distance is the mimumum number of positions between two equal length strings in which one string differs from the other.
The bitwise Hamming distance between 11110101 and 11011011 would be 4. In English diction, two random letters are usually skewed in
their binary in a way that they do not differ as much as two uniformly randomly distributed bytes. This means on average the Hamming
distance between two random English letters is 2-3 bits but for two uniformly random bytes it is 4 bits. The difference is additive as
strings get longer.
The next point is that the Hamming distance is minimized for a cipher key of correct length. Given a random English letter X and Y from
the plaintext, the Hamming distance between X and key K is H(X, K). Likewise for Y and K it is H(Y, K). If the key is the correct length
the difference between H(X, K) and H(Y, K) is in fact just H(X, Y) - this is minimized to 2-3 bits. However, if the key is incorrect, 
K', then the distance between H(X, K) and H(Y, K') is on average 4 bits because this is basically comparing two uniformly random bytes.
"""
from cryptohacks import *

#First, load in the text file
with open("c6.txt") as f:
    ciphertext = f.readlines()
ciphertext = [line.strip() for line in ciphertext]
#Now convert this list of strings into one big string
ciphertext = "".join(ciphertext)
#Since it has been base 64'd, we can decode the base 64 to get the ciphertext that has been xor'd
ciphertext = codecs.encode(codecs.decode(str.encode(ciphertext), 'base 64'), 'hex').decode('utf8')
#Notice above the ciphertext is wrapped in a final encode in hex
#This is needed to get rid of ascii encoding such as "\x42" showing up as "B"
#Note this will double the length of ciphertext from 2876 to 5752, meaning one char is two elements long
textSize = len(ciphertext)

#From here I calculate a normalized Hamming distance for key sizes between 2-40
#And store the Hamming distance in a dict
hamDist = {}
for keySize in range(2,41):
    textChunks = [ciphertext[i:i + keySize*2] for i in range(0, textSize, keySize*2)]
    block1 = textChunks[0]
    blockSize = len(block1)
    #Now we can calculate the average Hamming distance, that is normalized by keySize
    #The additional condition if len(a) == blockSize ensures that the two strings passed to hamming are the same length
    avgHamming = sum((hamming(block1, a, "hex")) for a in (textChunks[1:]) if len(a) == blockSize)/keySize
    avgHamming /= (len(ciphertext)//(blockSize) - 1)
    hamDist[keySize] = avgHamming

keySize = min(hamDist, key=hamDist.get)
print("Probable keysize length: %d\n" % keySize)
textChunks = [ciphertext[i:i + keySize*2] for i in range(0, textSize, keySize*2)]
#Now that we have a list of the ciphertext broken up into blocks of length keySize
#It is possbile to transpose the list and break the cipher character by character
keys = range(256)
finalKey = ""
for i in range(len(textChunks[0])//2):
    tposeText = "".join(line[i*2:i*2 + 2] for line in textChunks)
    textLen = len(tposeText)
    #Now the brute force decipher beings
    msgs = {}
    for i in keys:
        key = ""
        while len(key) != textLen:
            key += hex(i)[2:]
        hexMsg = xor(tposeText, key)
        msg = codecs.decode(hexMsg, 'hex').decode('utf8')
        msg += chr(i)
        msgs[msg] = score(msg[:-1], scoresDict)
        
    decoded = max(msgs, key = msgs.get)
#    print(decoded[:-1])
#    print("Key: %s" % decoded[-1])
    finalKey += decoded[-1]

#Finally with the correct key, encode it in hex
#Now the ciphertext can be broken down into plaintext
hexKey = codecs.encode(str.encode(finalKey), 'hex').decode('utf8')

#Repeat the key to the same length as the hex encoded text
repKey = hexKey * (textSize//len(hexKey) + 1)
repKey = repKey[:textSize]

hexText = xor(ciphertext, repKey)
plaintext = codecs.decode(hexText, 'hex').decode('utf8')
print(plaintext)