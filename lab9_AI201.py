# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:41:38 2021

@author: Dell
"""
"""

Now, create a program to implement the decryption of a given caeser cipher with known shift 
using the formula:

(Decryption formula with shift 26)

"""
# ENCRYPTION METHOD
def ENCRYPTION(text,shift):
    RES = " "
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 # 
print("hi")
        # Encrypt uppercase characters
        if (char.isupper()):
            RES += chr((ord(char) + shift-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            RES += chr((ord(char) + shift - 97) % 26 + 97)
 
    return RES
text="abcdefghij"
shift = 4
print ("Text:" + text)
print ("Shift:" + str(shift))
print ("Cipher:" + ENCRYPTION(text,shift))

# DECRYPTION
def DECRYPTION(text,shift):
 
    RES = " "
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            RES += chr((ord(char) - shift-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            RES += chr((ord(char) - shift - 97) % 26 + 97)
 
    return RES
text="abcdefghij"
shift = 4
print ("Text:" + text)
print ("Shift:" + str(shift))
print ("Cipher:" + DECRYPTION(text,shift))

            
