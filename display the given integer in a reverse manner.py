def reverseTheNumber ( num ) : 
    rem = 0 
    rev = 0 

    while num > 0 :
        rem = num % 10 
        rev = rev * 10 + rem 
        num = num // 10 
    
    return rev 

num = int(input("Enter the number : "))
ans = reverseTheNumber ( num )
print (ans )