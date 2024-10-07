def textToMorseCodeAndBack(inputValue):
    morse_code = {"A": "._", "B": "_...", "C": "_._.", "D": "_..", "E": ".",
                  "F": ".._.", "G": "__.", "H": "....", "I": "..", "J": ".___",
                  "K": "_._", "L": "_..", "M": "__", "N": "_.", "O": "___",
                  "P": ".__.", "Q": "__._", "R": "._.", "S": "...", "T": "_",
                  "U": ".._", "W": ".__", "X": "_.._", "Y": "_.__", "Z": "__..",
                  "1": ".____", "2": "..___", "3": "...__", "4": "...._",
                  "5": ".....", "6": "_....", "7": "__...", "8": "___..", "0": "_____",
                  "?": "..__..", "!": "_._.__"}

    morse = None
    flag = 0

    for i in inputValue:
        if i == "." or i == "_":
            flag += 1
        elif i.isalpha():
            flag-=1

    if flag>1:
        print("this is a morse code")
        morse=True
    elif flag<-1:
        print("this is a text")
        morse=False
    elif flag==0:
        print("contains text and morse symbols")
        morse=False

    inputValue=inputValue.upper()
    print(inputValue)
    converted=""

    # convert text to morse
    if not morse:
        for j in inputValue:
            for key,value in morse_code.items():
                if j==key:
                    converted=converted+morse_code[key]+" "
    elif morse: # work on this part.
        for v in inputValue:
            for letter,morseval in morse_code.items():
                if v==morse_code[letter]:
                    converted=converted+letter


    return converted

print(textToMorseCodeAndBack(". ... .__ ._ ._."))