# Python program to find the factorial of a number using recursion

def factOFANumber ( num ) :
    if num == 0 :
        return 1
    else :
        return num * factOFANumber ( num - 1 ) 
    
    

num = int(input("Enter a number : "))
ans = factOFANumber ( num )
print(ans) 
