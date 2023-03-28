# Python program to display the sum of n numbers using a list :->
  
numbers = []
num = int(input("Enter a number : "))

for index in range (num) : 
    temp  = int(input())
    numbers.append(temp)
    index += 1 

sum = 0 
for idx in range (num) :
    sum += numbers[idx] 
    idx += 1 

print("Sum of all numbers : " , sum)

