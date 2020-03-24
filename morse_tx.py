# R. Sheehan 23 - 3 - 2020
# Module that implements methods for Morse code transmission
# useful resources
# en.wikipedia.org/wiki/Morse_Code
# www.wikihow.com/Learn-Morse-Code

import sys # system commands
import re # regex support
import RPi.GPIO as GPIO # GPIO controls
import time # time

#sys.path.append('~/Programming/Python/Common/')
#import Common

MOD_NAME_STR = "morse_tx"

# need a dictionary to convert from alpha-numeric character to morse character
morse_code = {"A":"dit-dah", "B":"dah-dit-dit-dit","C":"dah-dit-dah-dit","D":"dah-dit-dit",
"E":"dit","F":"dit-dit-dah-dit","G":"dah-dah-dit","H":"dit-dit-dit-dit","I":"dit-dit","J":"dit-dah-dah-dah",
"K":"dah-dit-dah","L":"dit-dah-dit-dit","M":"dah-dah","N":"dah-dit","O":"dah-dah-dah","P":"dit-dah-dah-dit",
"Q":"dah-dah-dit-dah","R":"dit-dah-dit","S":"dit-dit-dit","T":"dah","U":"dit-dit-dah","V":"dit-dit-dit-dah",
"W":"dit-dah-dah","X":"dah-dit-dit-dah","Y":"dah-dit-dah-dah","Z":"dah-dah-dit-dit","0":"dah-dah-dah-dah-dah",
"1":"dit-dah-dah-dah-dah","2":"dit-dit-dah-dah-dah","3":"dit-dit-dit-dah-dah","4":"dit-dit-dit-dit-dah",
"5":"dit-dit-dit-dit-dit","6":"dah-dit-dit-dit-dit","7":"dah-dah-dit-dit-dit","8":"dah-dah-dah-dit-dit",
"9":"dah-dah-dah-dah-dit","ACHTUNG":"dah-dit-dah-dit-dah","YES":"dah-dit-dah-dit","NO":"dah-dit",
"OVER":"dah-dit-dah","OUT":"dit-dah-dit-dah-dit","ROGER":"dit-dah-dit"}


# methods to enable the conversion
def convert_to_morse(str_input, loud = False):
    # method that converts the letters in a text string to morse code
    # output is in the form of a list of characters in Morse code
    # if the character is not in the Morse set it is ignored
    # R. Sheehan 23 - 3 - 2020
    
    FUNC_NAME = ".convert_to_morse()"
    ERR_STATEMENT = "Error: " + MOD_NAME_STR + FUNC_NAME
    
    try:

        if str_input is not None:
            print("Input string to be converted: %(v1)s"%{"v1":str_input})
            str_input = re.sub(r'[^\w]', '', str_input) # remove all non alpha-numeric characters from input
            str_list = list(str_input.upper()) # convert the input string to a list of upper case letters
            if loud: print(str_list)
            # translate the list to Morse
            morse_list = []
            for i in range(0, len(str_list), 1):
                if str_list[i] in morse_code:
                    entry = morse_code[str_list[i]]
                    morse_list.append(entry)
                    if loud: print(entry)
            return morse_list
        else:
            ERR_STATEMENT = ERR_STATEMENT + "\n" + "str_input is None"
            raise Exception
            return None
    except Exception as e:
        print(ERR_STATEMENT)
        print(e)


def morse_transmit(message, add_prosigns = False, loop_message = False, loud = False):
    # method for transmitting the Morse signal    
    # method tells the GPIO to output a signal across a circuit
    # circuit contains LED which blinks to enable Morse code transmission
    # R. Sheehan 24 - 3 - 2020

    FUNC_NAME = ".morse_transmit()"
    ERR_STATEMENT = "Error: " + MOD_NAME_STR + FUNC_NAME

    try:
        if message is not None:
            if add_prosigns:
                # Add pro-signs to beginning and end of message
                message.insert(0, morse_code["ACHTUNG"])
                message.append(morse_code["OVER"])
                message.append(morse_code["OUT"])
            
            # set GPIO up to transmit
            pin_no = 11 # assign the pin from which the signal will be transmitted
            dit_time = 0.5
            dah_time = 3.0*dit_time # dah = 3 dit

            if add_prosigns:
                # transmit the pro-signs before and after the message
                signals = morse_code["ACHTUNG"].split('-')
                signal_transmit(signals, dit_time, dah_time, pin_no, loud)

            if loop_message:
                # transmit the message multiple times by recursively calling morse_transmit without pro-signs etc
                n_loops = 3
                for k in range(0, n_loops, 1):
                    morse_transmit(message, False, False, loud)
            else:
                # loop over the letters in the message once
                for i in range(0, len(message), 1):
                    signals = message[i].split('-') # make a list of signals from the dit, dah that comprise each letter
                    signal_transmit(signals, dit_time, dah_time, pin_no, loud) # transmit the signal

            if add_prosigns:
                # transmit the pro-signs before and after the message
                signals = morse_code["OVER"].split('-')
                signal_transmit(signals, dit_time, dah_time, pin_no, loud)            
                signals = morse_code["OUT"].split('-')
                signal_transmit(signals, dit_time, dah_time, pin_no, loud)            

        else:
            ERR_STATEMENT = ERR_STATEMENT + "\n" + "message is None"
            raise Exception
    except Exception as e:
        print(ERR_STATEMENT)
        print(e)

def signal_transmit(signals, dit_time, dah_time, pin_no, loud = False):
    # method for transmitting a signal
    # R. Sheehan 24 - 3 - 2020

    FUNC_NAME = ".signal_transmit()"
    ERR_STATEMENT = "Error: " + MOD_NAME_STR + FUNC_NAME

    try:
        c1 = True if signals is not None else False
        c2 = True if dit_time > 0.0 else False
        c3 = True if dah_time > dit_time else False
        c4 = c1 and c2 and c3
        if c4:

            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(pin_no, GPIO.OUT)

            for j in range(0, len(signals), 1):
                if signals[j] == 'dit':
                    # blink once
                    if loud: print(signals[j])
                    GPIO.output(pin_no, True)
                    time.sleep(dit_time)
                elif signals[j] == 'dah':
                    # long blink == three dit
                    if loud: print(signals[j])
                    GPIO.output(pin_no, True)
                    time.sleep(dah_time)
                else:
                    # do nothing
                    pass
                # return-to-zero-between signals
                if loud: print("\tOff!")
                GPIO.output(pin_no, False)
                time.sleep(dit_time)

            GPIO.cleanup()

        else:
            if c1 == False: ERR_STATEMENT = ERR_STATEMENT + "\n" + "signal is None"
            if c2 == False: ERR_STATEMENT = ERR_STATEMENT + "\n" + "dit_time < 0.0"
            if c3 == False: ERR_STATEMENT = ERR_STATEMENT + "\n" + "dah_time < dit_time"
            raise Exception
    except Exception as e:
        print(ERR_STATEMENT)
        print(e)
