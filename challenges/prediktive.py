stringRec =  "abcdfjger"
stringSent = "abcdfjgerj"

# stringRec =  "aaaaaabaa"
# stringSent = "aaaaaaaa"


if stringSent == stringRec:
    print("NA")
else:
    stringSentList = list(stringSent)
    stringRecList = list(stringRec)
    differencesList = []

    for letter in stringRecList:
        if letter in stringSentList:
            stringSentList.pop(stringSentList.index(letter))
        else:
            print(letter)
            exit()

print(stringSentList[0])
