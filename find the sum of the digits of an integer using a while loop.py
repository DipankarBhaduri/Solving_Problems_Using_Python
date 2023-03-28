def findTheSum(num) :
    sum = 0 
    while num > 0 :
        temp = num % 10 
        sum += temp 
        num = num // 10 

    return sum 


num = int(input("Enter a number : "))
sum = findTheSum(num)
print("Sum of the digit of an integer : ",         sum)
