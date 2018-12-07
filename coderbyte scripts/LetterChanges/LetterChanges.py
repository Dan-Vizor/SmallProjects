def LetterChanges(str):
    out = ""
    for each in str:
        if ord(each) in range(ord("a"), ord("z")):
            if chr(ord(each) + 1) in ["a", "e", "i", "o", "u"]:
                out += chr(ord(each) + 1).upper()
            else:
                out += chr(ord(each) + 1)
        else:
            out += each
    return out
    
# keep this function call here  
print(LetterChanges(input()))  
