class charGenerator:
    def __init__(self,char,shiftSize):
        self.char = char
        self.shiftSize = shiftSize

    def createNewChar(self):
        # get ASCII value of new char
        newCharInt = ord(self.char) + self.shiftSize

        # check if new char an upper or lowercase char
        if self.char.isupper():
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