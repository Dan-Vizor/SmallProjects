def LetterCapitalize(str):
    # code goes here 
    letterNo = 0
    out = ""
    oldChar = ""
    for char in str:
        if letterNo == 0 or oldChar in [" ", "_",]:
            out += char.upper()
        else:
            out += char
        oldChar = char
        letterNo += 1
    return out
    
# keep this function call here  
print(LetterCapitalize(input()))
