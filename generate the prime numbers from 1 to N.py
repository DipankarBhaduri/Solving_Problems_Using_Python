def checkPrimeOrNot ( num ) :
    count = 0 
    for index in range (num) : 
        if num % (index+1) == 0 :
            count += 1 
        index += 1 
    
    if count == 2 :
        return True 
    else :
        return False 


num = int( input ("Enter a number : "))
for idx in range (num) :  
    if checkPrimeOrNot ( idx+1 ) :
        print(idx+1) 
    idx += 1 