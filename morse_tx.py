# R. Sheehan 23 - 3 - 2020
# Module that implements methods for Morse code transmission
# useful resources
# en.wikipedia.org/wiki/Morse_Code
# www.wikihow.com/Learn-Morse-Code

MOD_NAME_STR = "morse_tx"

# need a dictionary to convert from alpha-numeric character to morse character



# methods to enable the conversion
def convert_to_morse(str_input):
    # method that converts a string to morse code
    
    FUNC_NAME = ".convert_to_morse()"
    ERR_STATEMENT = "Error: " + MOD_NAME_STR + FUNC_NAME
    
    try:

        if str_input is not None:
            str_input = str_input.upper()
            print("Input string to be converted: %(v1)s"%{"v1":str_input})
        else:
            raise Exception
    except Exception as e:
        print(ERR_STATEMENT)
        print(e)
