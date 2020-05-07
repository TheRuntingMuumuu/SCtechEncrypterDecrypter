
"""
SCtech Encrypter
Coded by TheRuntingMuumuu
Do not distribute without my permission.
Started on March 23 2020
Made for fun. :)
[I accidentally wrote endoded and decoded instead of encrypted and decrypted in the vars, and I am too lazy to change it.]
"""


#--------------------For clearing the screen--------------------------------------#
def clear():
    os.system('cls' if os.name == 'nt' else 'clear') #Credit: stackoverflow.com/questions/2084508/clear-terminal-in-python/23075152
#----------------------------Imports the necisarry module things-----------------#
import os
from sys import exit
try:
    from needthis import *
except ImportError:
    exit("We couldn't find the file needthis.py. So we have to exit.")
#------------------------------Welcome Area--------------------------------------#
clear() #formatting (clears the window)
print('------------- SCtech Encrypter/Decrypter -------------\n') #formatting
print('\n Please do not distribute this program to anyone without my permission. Thanks, TRM.')
accept = input('Do you agree (y/n) : ') #do they agree with the terms?
encoder = 0
theyWantToEncodeAnother = True

#--------------------Functions for determining how to encrypt/decrypt-------------#
def encoderFunction(text):
    """This is the function that encodes all the text. It takes the text input from the user and will encode it and return the result"""
    verTF = False
    while verTF is False:
        ver = input('What version do you want to use to encode? (Available: 1) ')
        if ver == '1':
            encodedText = encodeVer1(text)
            verTF = True
        else:
            print('You did not enter a valid entry.')
            verTF = False
    return encodedText

def decoderFunction(text):
    """This is the function that decodes all the text. It takes the text input from the user and will decode it and return the result"""
    verTF = False
    while verTF is False:
        ver = input('What version do you want to use to decrypt : ')
        if ver == '1':
            decodedText = decryptVer1(text)
            verTF = True
        else:
            print('Please enter a valid entry.')
    return decodedText

def theyWantToEncodeAnother__Prompt():
    """This one just asks the user if they want to do it again"""
    validentry = 0
    while validentry == 0:
        prompt = input('\nDo you want to encrypt or decrypt another (y/n) : ')
        if prompt == 'y':
            return True
        elif prompt == 'n':
            exit('\tThank you for using my encryption/decryption program.')
        else:
            validentry = 0
            print('Please enter a valid entry.')

#-------------------------------Versions of encrypter and decrypter--------------#

#--------------------------------What the user wants to do------------------------#
if accept == 'y': #if they accept the program will work. Else it will skip over this and go to the else statement at the bottom of the page and will exit. :)
    while theyWantToEncodeAnother is True:
        clear()
        print('------------- SCtech Encrypter/Decrypter -------------\n')
        while encoder == 0:
            encoder = input('Do you want to use the encoder or decoder : ')
            if encoder == 'encoder' or encoder == 'Encoder' or encoder == 'encrypter' or encoder == 'encrypt' or encoder == 'e' or encoder == 'E':
                encoder = True
                break
            elif encoder =='decoder' or encoder == 'Decoder' or encoder == 'decrypter' or encoder == 'decrypt' or encoder == 'd' or encoder == 'D':
                encoder = False
                break
            else:
                encoder = 0
                print('Please enter a valid entry.')
        if encoder is True:
            textToEncode = input('What do you want to encode : ')
            print('\t', encoderFunction(textToEncode))
            theyWantToEncodeAnother = theyWantToEncodeAnother__Prompt()
            encoder = 0
        else:
            textToDecode = input('What do you want to decode : ')
            print('\t', decoderFunction(textToDecode))
            theyWantToEncodeAnother = theyWantToEncodeAnother__Prompt()
            encoder = 0
else:
    print('Since you did not agree, you cannot use the program')
    exit()
