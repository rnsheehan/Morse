# R. Sheehan 20 - 3 - 2020
# Python script for converting input text into Morse code
# Idea being to display Morse version of text using blinking LED
# Down the line this could become a lab in which messages are transmitted
# using Morse and received and decoded using a Pre-Amp Receiver
# Will need to define a dictionary using the ITU Morse alphabet and
# write a function for converting the text into Morse
# Message will be transmitted using GPIO controlled blinking LED
# Aim is to demonsrtate that something useful can be done with the RPi
# Use as much of Python's built-in string handling capabilities as possible

import sys
import os
import glob
import re
import math
import numpy

#import scipy # apparently cannot install scipy on raspberry pi
#import matplotlib # apparently cannot install matplotlib on raspberry p

# import required modules
import morse_tx

def sandbox():
    # space for testing random bits of code
    
    str_input = "What God Hath Wrought"
    
    # need to convert string to an array of words
    # split string using spaces
    print(str_input.split(' '))
    # need to convert word to an array of letters
    # split words using list
    print("\n")
    print(list(str_input.upper()))

    string = "nlwnw*;akncakdkk?kdkjd*lwlw>27.3912"

    string = re.sub(r'[^\w]', '', string)

    print(string)

    print(re.search("[A-Z]",string))
    print(re.search("[0-9]",string))
    print("\n")


    #test_str = "dit-dit-dah-dah-dah-dit-dit"
    test_str = ""
    print(test_str.split('-'))

def main():
    pass

if __name__ == '__main__':
    main()

    pwd = os.getcwd()

    print(pwd)
    print("\n")

    str_input = input('Enter a string to transmit:')

    morse_output = morse_tx.convert_to_morse(str_input, True)

    morse_tx.morse_transmit(morse_output, False, False, True)

    #sandbox()
