def LongestWord(sen): 
    words = sen.split(" ")
    wordsLen = []
    for each in words:
        word = ""
        for letter in each:
            if ord(letter.lower()) in range(ord("a"),ord("z")):
                word += letter
        wordsLen += [len(word)]

    current_loc = 0
    large_loc = 0
    large_value = 0
    for each in wordsLen:
        if each > large_value:
            large_value = each
            large_loc =  current_loc
        current_loc += 1
    return words[large_loc]
    
# keep this function call here  
print(LongestWord(input()))
