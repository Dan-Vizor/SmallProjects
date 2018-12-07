def VowelSquare(strArr):
    Vowels = ["a", "e", "i", "o", "u"]
    topLoc = []
    elementNo = 0
    for element in strArr:
        elementNo += 1
        elementList = []
        for each in element: elementList += [each]
        
        if topLoc != []:
            if elementList[topLoc[0]] in Vowels and elementList[topLoc[1]] in Vowels:
                return "{}-{}".format(elementNo -2, topLoc[0])
        
        for i in range(0, len(elementList)):
            if elementList[i] in Vowels:
                try:
                    if elementList[i +1] in Vowels:
                        topLoc = [i, i +1]
                        break
                except: pass
    return "not found"

# keep this function call here
print(VowelSquare(["aqrst", "ukaei", "ffooo"]))
#["aqrst", "ukaei", "ffooo"]

#  To Do
# - change to python2
# - add user input
