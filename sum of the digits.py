def sumOfAllDigit ( num ) :
    rem = 0
    sum = 0

    while num > 0 : 
        rem = num % 10 
        sum += rem 
        num = num // 10 

    return sum 

num = int(input("Enter the number : "))
ans = sumOfAllDigit (num)
print("Sum of all digit :" , ans )