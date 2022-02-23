from src.charGenerator import charGenerator

class Decryptor:
    # default constructor
    def __init__(self,str_list,key):
        self.str_list = str_list
        self.key = key
    

    # method for turning ciphertext to plaintext
    def decrypt(self):
        new_str_list = []
        keyCounter = 0

        # for-loop iterates through each element
        for x in self.str_list:
            char_list = list(x)
            newline = ""

            # for-loop iterates through each char of element
            for c in char_list:
                # check if key char is a letter
                while not (self.key[keyCounter].isalpha()):
                    keyCounter += 1

                    # check if reached the last char of key
                    if (keyCounter >= len(self.key) - 1):
                        keyCounter = 0;

                # calculate jumps according to whether function encrypts or decrypts
                shiftSize = ord('a') - ord(self.key[keyCounter])    # get difference from key letter and 'a' decimal values

                # check if char is letter or number
                if c.isalpha() or c.isnumeric():
                    newChar = charGenerator(c,shiftSize)  
                    c = newChar.createNewChar()

                newline += c
                keyCounter += 1

                # check if reached the last char of key
                if (keyCounter >= len(self.key) - 1):
                    keyCounter = 0;

            new_str_list.append(newline)    # add encypted line new_str_list
        
        return new_str_list