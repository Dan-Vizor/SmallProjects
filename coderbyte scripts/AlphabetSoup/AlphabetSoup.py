def AlphabetSoup(str): 
    Llist = []
    for each in str:
        Llist += [each]
    Llist.sort()

    letters = ""
    for each in Llist:
        letters += each
    return letters
    
# keep this function call here  
print(AlphabetSoup(input()))
