def SimpleSymbols(str): 
    if str == "": return "false"
        
    inpList = []
    for each in str:
        inpList += [each]
    
    for i in range(0, len(str)):
        if ord(inpList[i]) in range(ord("a"), ord("z")):
            if i == 0: return "false"
            
            #print(inpList[i -1] + inpList[i] + inpList[i +1])
            try:
                if inpList[i -1] == "+" and inpList[i +1] == "+": pass
                else: return "false"
            except: return "false"
    return "true"
    
# keep this function call here  
print(SimpleSymbols(input()))
