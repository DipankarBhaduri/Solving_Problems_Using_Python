def Check_Even_Odd ( num ) :
    if num % 2 == 0 :
        return "Even" 
    else :
        return "Odd" 


num = input("Enter a number : ")
ans = Check_Even_Odd ( int(num)) 
print( ans ) 
