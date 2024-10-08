def textToMorseCodeAndBack(inputValue):
    morse_code_list = ["._","_...","_._.","_..", ".",".._.","__.","....","..",".___","_._","_..","__","_.","___",
                       ".__.","__._","._.","...","_",".._","..._",".__","_.._","_.__","__..",".____","..___","...__",
                       "...._",".....","_....","__...","___..","____.","_____","..__..","_._.__"]
    letters_list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
                  "S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0",
                  "?","!"]

    morse = None
    flag = 0

    for i in inputValue:
        if i == "." or i == "_":
            flag += 1
        elif i.isalpha():
            flag-=1

    if flag>1:
        morse=True
    elif flag<-1:
        morse=False
    elif flag==0:
        morse=False

    inputValue=inputValue.upper()
    converted=""

    # convert text to morse
    if not morse:
        for j in inputValue:
            for a in range(len(letters_list)):
                if j==letters_list[a]:
                    converted=converted+morse_code_list[a]+" "

    elif morse:
        inputValue=inputValue.split()
        for k in inputValue:
            for b in range(len(morse_code_list)):
                if k==morse_code_list[b]:
                    converted=converted+letters_list[b]



    return converted

print(textToMorseCodeAndBack(".. .__ ._ _. _ _ ___ __ . . _ .___ . ... ... .. . ._ __. ._ .. _. ._ ... ... .... . .. ... . _.._ ._ _._. _ _.. _.__ _ .... . _._ .. _. _.. ___ .._. .__. . ._. ... ___ _. .. ._ __ _.. ___ ___ _._ .. _. __. .._. ___ ._. "))