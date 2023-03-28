def checkIfDivisiableBy5and7 ( num ) : 
    if num % 5 == 0 and num % 7 == 0 :
        return "YES"
    else :
        return "NO"


num = int(input("Enter the number : "))
ans = checkIfDivisiableBy5and7( num ) 
if ans == "YES" :
    print("Yes " ,num , "is divisiable by 5 & 7")
else :
     print(num , "is Not Divisiable by 5 & 7")
