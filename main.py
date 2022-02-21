# @author: Orion2323/ Giancarlos Dominguez
# @file: main.py
# @date: 2/15/2022

from fileinput import close
from hashlib import new

# function that reads input from a txt file
def readFile():
    # Open input file stream
    input_file = open('input.txt','r')
    str_list = [line.strip('\n') for line in input_file]

    # close input file stream
    input_file.close()

    return str_list
# end method

# function that encrypts a given text with key
def ciphertext(str_list,key):
    new_str_list = []

    shiftSize = ord(key) - ord('a')

    # for-loop iterates through each element
    for x in str_list:
        char_list = list(x)
        newline = ""

        # for-loop iterates through each char of element
        for c in char_list:

            # check if char is letter or number
            if c.isalpha() or c.isnumeric():
                c = newChar(c,shiftSize)     
            newline += c

        new_str_list.append(newline)    # add encypted line new_str_list
    
    return new_str_list
# end method

# method that deciphers a given text with key
def decipher(str_list,key):
    new_str_list = []

    shiftSize = ord('a') - ord(key)
    # for-loop iterates through all lines
    for x in str_list:
        newline = ""
        char_list = list(x)

        # for-loop iterates through all chars in line
        for c in char_list:
            # check if char is a letter or number
            if c.isalpha() or c.isnumeric():
                c = newChar(c,shiftSize)

            newline += c
        
        new_str_list.append(newline)    # add deciphered line to new_str_list
    
    return new_str_list
# end method

# function that calculates ASCII code of new 
def newChar(char,jumps):
    newCharInt = ord(char) + jumps

    if char.isupper():
        if newCharInt > 90:
            newCharInt -= 26;
        elif newCharInt < 65:
            newCharInt = 90 - (64 % newCharInt)
    else:
        if newCharInt > 122:
            newCharInt -= 26
        elif newCharInt < 97:
            newCharInt = 122 - (96 % newCharInt)

    return chr(newCharInt)
# end method

# start program
fileChoice = input("Do you want to read file? (y/n)\n")
str_list = []

if fileChoice.lower() == 'y':
    str_list = readFile()
    key = input("Enter a key: ")
elif fileChoice.lower() == 'n':
    text = input("Enter text to encrypt: ")
    str_list.append(text)
    key = input("Enter single letter key: ")
else:
    print("Invalid input!")

cipher_list = ciphertext(str_list,key)
print("Encrypted text:")
print(*cipher_list, sep = '\n')

print()

plain_text = decipher(cipher_list,key)
print("Decrypted text:")
print(*plain_text,sep = '\n')
# end program