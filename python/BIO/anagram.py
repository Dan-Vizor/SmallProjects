#!/usr/bin/python

def isAnagram(inp, no):
    tarList = []
    tar = inp * no
    print(inp)
    for char in chr(inp): tarList += [int(char)]
    if len(inpList) != len(inpList): return False
    else:
        for char in inp:
            if tarList == []: return False
            if char in tarList: tarList.remove(char)
            else: return False
        return True
    
while True:
    try:
        inp = int(input("enter input number: "))
        break
    except:
            print("error: bad input\n")
            continue

print("\n")
switch = False
for i in range(1,9):
    if isAnagram(inp,i) == True:
        print(i)
        switch = True
if switch == False:
    print("no")