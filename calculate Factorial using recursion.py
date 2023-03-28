
def findFactorialUsingRecursion ( num ) :
    if num == 1 :
        return num 
    else :
        return num * findFactorialUsingRecursion( num - 1 )


num = input ("Enter a number : ") 
ans = findFactorialUsingRecursion ( int(num) ) 
print("The Factorial is : ", ans) 