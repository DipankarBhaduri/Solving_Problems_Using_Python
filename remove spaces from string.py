def removeSpaces ( sentence ) :
    length = len(sentence) 
    result = "" 

    for index in range(length) :
        char = sentence[index] 
        if char == ' ' :
            continue 
        else :
            result = result + char 
            
    return result 


sentence =input ("Enter a sentence : ")
result = removeSpaces ( sentence ) 
print ( result )