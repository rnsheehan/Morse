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

#import scipy # apparently cannot install scipy on raspberry pi
#import matplotlib # apparently cannot install matplotlib on raspberry p

import math
import numpy

def main():
    pass

if __name__ == '__main__':
    main()

    pwd = os.getcwd()

    print(pwd)
    print("\n")

    str_input = input('Enter a string to transmit:')

    str_input = str_input.upper() # conver the string to all uppercase

    print("You entered: %(v1)s"%{"v1":str_input})
