def primeOrNot ( num ) :
    count = 0 

    if num == 1 :
        return False 
    if num == 2 :
        return False 
    

    for idx in range (num) :
        if num % (idx+1) == 0 :
            count += 1 

    if count == 2 :
        return True 
    else :
        return False 


num = input ("Enter a number : ")

if primeOrNot (int(num)) :
    print(num + " is a prime")
else :
    print(num + " is Not a prime")