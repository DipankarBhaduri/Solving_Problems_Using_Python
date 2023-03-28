# 14. Python program to display all integers within the range 100-200 whose sum of digits is an even number

def checkSumOfDigitEvenOrNOt ( num ) :
    rem = 0 
    sum = 0

    while num > 0 :
        rem = num % 10 
        sum += rem 
        num = num // 10 

    if sum % 2 == 0 :
        return True 
    else :
        return False


start = 100 
end = 200

for start in range ( start , end ) :
    temp = start 
    if checkSumOfDigitEvenOrNOt(temp) : 
        print(temp)
    start += 1 