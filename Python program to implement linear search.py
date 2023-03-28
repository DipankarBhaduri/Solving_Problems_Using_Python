def findOutTarget ( target , numbers ) :
    index = 0 
    for index in range (len(numbers)) :
        temp = numbers[index]
        if temp == target :
            return index
    
    return -1 


numbers = []
num = int(input("Enter a number :"))

start = 0 
while start < num :
    temp = int(input())
    numbers.append(temp)
    start += 1 

target = int(input("Enter a target :"))

ans = findOutTarget ( target , numbers )
print("Numbers :" , numbers)
print(target ,"found at :" , ans )
    

