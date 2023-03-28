def averageOfSet ( numbers ) :
    print( numbers)
    sum = 0 
    length = len(numbers)
    for idx in range ( length) :
        sum += numbers[idx]
        idx = idx + 1 
    return sum / length 


numbers = [] 
leng = int(input()) 
for index in range(leng) :
    temp = int(input())
    numbers.append(temp)
    index = index + 1 

avg = averageOfSet ( numbers) 
print( avg)