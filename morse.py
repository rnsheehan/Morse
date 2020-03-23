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

def main():
    pass

if __name__ == '__main__':
    main()

    pwd = os.getcwd()

    print(pwd)
    print("\n")

    str_input = input('Enter a string to transmit:')

    morse_tx.convert_to_morse(str_input)
