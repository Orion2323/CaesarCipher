# @author: Orion2323/ Giancarlos Dominguez
# @file: main.py
# @date: 2/15/2022

from fileinput import close
from genericpath import exists
from hashlib import new
from os.path import exists

# function that reads input from a txt file
def readFile():
    fileName = input("Enter file name: ")

    # while-loop iterates until user types a valid input file name
    while not (exists(fileName)):
        print("File not found!")
        fileName = input("Enter file name: ")
    
    input_file = open(fileName,'r') # open file
    str_list = [line.strip('\n') for line in input_file]

    # close input file stream
    input_file.close()

    return str_list
# end function

# function that encrypt and decrypts text
def encrypt_decrypt(str_list,key,mode):
    new_str_list = []
    keyCounter = 0

    # for-loop iterates through each element
    for x in str_list:
        char_list = list(x)
        newline = ""

        # for-loop iterates through each char of element
        for c in char_list:
            # check if key char is a letter
            while not (key[keyCounter].isalpha()):
                keyCounter += 1

                # check if reached the last char of key
                if (keyCounter >= len(key) - 1):
                    keyCounter = 0;

            # calculate jumps according to whether function encrypts or decrypts
            if (mode == 'e'):
                shiftSize = ord(key[keyCounter]) - ord('a')    # get difference from key letter and 'a' decimal values
            elif (mode == 'd'):
                shiftSize = ord('a') - ord(key[keyCounter])    # get difference from key letter and 'a' decimal values

            # check if char is letter or number
            if c.isalpha() or c.isnumeric():
                c = newChar(c,shiftSize)   

            newline += c
            keyCounter += 1

            # check if reached the last char of key
            if (keyCounter >= len(key) - 1):
                keyCounter = 0;

        new_str_list.append(newline)    # add encypted line new_str_list
    
    return new_str_list
# end function

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
# end function

# start program
correctInput = False
# check if user typed in correct options
while not (correctInput):
    fileChoice = input("Do you want to read file? (y/n): ").lower()
    
    # check if user input is a 'y' or 'n'
    if (fileChoice == 'y' or fileChoice == 'n'):
        correctInput = True
    else:
        print("Invalid input!")

str_list = []

# check if user wants to use input file or input custom plaintext
if fileChoice.lower() == 'y':
    str_list = readFile()
    key = input("Enter key: ")
elif fileChoice.lower() == 'n':
    text = input("Enter text to encrypt: ")
    str_list.append(text)
    key = input("Enter key: ")
else:
    print("Invalid input!")

# encrypt plaintext
cipher_list = encrypt_decrypt(str_list,key,'e')
print("Encrypted text:")
print(*cipher_list, sep = '\n')

print()

#decrypt ciphertext
plain_text = encrypt_decrypt(cipher_list,key,'d')
print("Decrypted text:")
print(*plain_text,sep = '\n')
# end program