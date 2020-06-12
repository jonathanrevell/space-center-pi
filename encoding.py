class EncodedMessage:
    def __init__(self):
        self.data = []

    def encodeLED(self, val):
        if val:
            self.data.append(True)
        else:
            self.data.append(False)
    
    def encodeBarGraph(self, val, bar_len=10):
        """
        Provided an integer between 0 and bar_len
        Light up val number of LEDs on the bar from left to right
        """
        if(val > bar_len or val < 0):
            raise Exception("Must be an int between 0 and " + str(bar_len))
        print("Encoding bar graph " + str(val))
        counter = 1
        while counter < bar_len:
            if counter <= val:
                self.data.append(True)
            else:
                self.data.append(False)
            counter += 1

    def encodeReverseBarGraph(self, val, bar_len=10):
        """
        Provided an integer between 0 and bar_len
        Light up val number of LEDs on the bar from right to left
        """        
        if(val > bar_len or val < 0):
            raise Exception("Must be an int between 0 and " + str(bar_len))
        
        rem = bar_len - val # Ensure the number lit up = val
        print("Encoding reverse bar graph " + str(val))

        counter = 1
        while counter < bar_len:
            if counter <= rem:
                self.data.append(False)
            else:
                self.data.append(True)
            counter += 1  
    
    def encodeMazeValues(self, inputNum, endNum):
        """
        Provided an integer between 0 and 5
        Light up val number of LEDs on the bar from right to left
        """        
        if(inputNum > 5 or inputNum < 0):
            raise Exception("Must be an int between 0 and 10")

        print("Encoding maze graph " + str(inputNum))

        counter = 1
        while counter < 5:
            if counter == inputNum:
                self.data.append(True)
            else:
                self.data.append(False)
            counter += 1         
        
        counter = 1
        while counter < 5:
            if counter == endNum:
                self.data.append(True)
            else:
                self.data.append(False)
            counter += 1
    
    def encodeAlphaNumericNumber(self, val):
        """
        Provided a number, coerce it to a string and encode it
        """
        return self.encodeAlphaNumeric(str(val))
    
    def encodeAlphaNumeric(self, string):
        """
        Encodes a string into a message supported by the Adafruit LED backpack
        """
        print("Encoding " + str(len(string)) + " character string for alpha numeric display")
        for ch in string:
            binstr = numdict[ch]
            binstr = self.mapAlphaBinaryToPinOrder(binstr)
            self.encodeBinaryString(binstr)

    def mapAlphaBinaryToPinOrder(self, s):
        '''
        To help make wiring easier
        '''
        return [s[4],s[3],s[2],s[1],s[0],s[5],s[6]]

    def encodeBinaryString(self, binstr):
        for bit in binstr:
            if bit == "0":
                self.data.append(False)
            if bit == "1":
                self.data.append(True)

'''
A  B  C  D  E  F  G
0  1  2  3  4  5  6
12 10 9  7  1  18 13|6
'''

[0,1,2,3,4,5,6]
[4,3,2,1,0,5,6]

numdict = {
    "0": "1111110"
    "1": "0110000"
    "2": "1101101"
    "3": "1111001"
    "4": "0110011"
    "5": "1011011"
    "6": "1011111"
    "7": "1110000"
    "8": "1111111"
    "9": "1111011"
}

# Based on the LED Backpack
# https://github.com/adafruit/Adafruit_LED_Backpack/blob/master/Adafruit_LEDBackpack.cpp
'''
We probably can't use this:
numdict = {
    " ": "0000000000000000", 
    "!": "0000000000000110", 
    "\"": "0000001000100000", 
    "#": "0001001011001110", 
    "$": "0001001011101101", 
    "%": "0000110000100100", 
    "&": "0010001101011101", 
    "'": "0000010000000000", 
    "(": "0010010000000000", 
    ")": "0000100100000000", 
    "*": "0011111111000000", 
    "+": "0001001011000000", 
    ",": "0000100000000000", 
    "-": "0000000011000000", 
    ".": "0000000000000000", 
    "/": "0000110000000000", 
    "0": "0000110000111111", 
    "1": "0000000000000110", 
    "2": "0000000011011011", 
    "3": "0000000010001111", 
    "4": "0000000011100110", 
    "5": "0010000001101001", 
    "6": "0000000011111101", 
    "7": "0000000000000111", 
    "8": "0000000011111111", 
    "9": "0000000011101111", 
    ":": "0001001000000000", 
    ";": "0000101000000000", 
    "<": "0010010000000000", 
    "=": "0000000011001000", 
    ">": "0000100100000000", 
    "?": "0001000010000011", 
    "@": "0000001010111011", 
    "A": "0000000011110111", 
    "B": "0001001010001111", 
    "C": "0000000000111001", 
    "D": "0001001000001111", 
    "E": "0000000011111001", 
    "F": "0000000001110001", 
    "G": "0000000010111101", 
    "H": "0000000011110110", 
    "I": "0001001000000000", 
    "J": "0000000000011110", 
    "K": "0010010001110000", 
    "L": "0000000000111000", 
    "M": "0000010100110110", 
    "N": "0010000100110110", 
    "O": "0000000000111111", 
    "P": "0000000011110011", 
    "Q": "0010000000111111", 
    "R": "0010000011110011", 
    "S": "0000000011101101", 
    "T": "0001001000000001", 
    "U": "0000000000111110", 
    "V": "0000110000110000", 
    "W": "0010100000110110", 
    "X": "0010110100000000", 
    "Y": "0001010100000000", 
    "Z": "0000110000001001", 
    "[": "0000000000111001", 
    "]": "0000000000001111", 
    "^": "0000110000000011", 
    "_": "0000000000001000", 
    "`": "0000000100000000", 
    "a": "0001000001011000", 
    "b": "0010000001111000", 
    "c": "0000000011011000", 
    "d": "0000100010001110", 
    "e": "0000100001011000", 
    "f": "0000000001110001", 
    "g": "0000010010001110", 
    "h": "0001000001110000", 
    "i": "0001000000000000", 
    "j": "0000000000001110", 
    "k": "0011011000000000", 
    "l": "0000000000110000", 
    "m": "0001000011010100", 
    "n": "0001000001010000", 
    "o": "0000000011011100", 
    "p": "0000000101110000", 
    "q": "0000010010000110", 
    "r": "0000000001010000", 
    "s": "0010000010001000", 
    "t": "0000000001111000", 
    "u": "0000000000011100", 
    "v": "0010000000000100", 
    "w": "0010100000010100", 
    "x": "0010100011000000", 
    "y": "0010000000001100", 
    "z": "0000100001001000", 
    "{": "0000100101001001", 
    "|": "0001001000000000", 
    "}": "0010010010001001", 
    "~": "0000010100100000"
}

