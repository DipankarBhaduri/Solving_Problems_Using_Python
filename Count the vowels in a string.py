def countVowel ( name ) :
    length = len(name)
    count = 0 

    for index in range(length) :
        char = name[index]
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' :
            count = count + 1 
        
        index = index + 1    
    return count 


name = "Dipankar Bhaduri"
result = countVowel ( name ) 
print(result)


