# R. Sheehan 23 - 3 - 2020
# Module that implements methods for Morse code transmission
# useful resources
# en.wikipedia.org/wiki/Morse_Code
# www.wikihow.com/Learn-Morse-Code

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
