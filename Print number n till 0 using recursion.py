def printNtoZero ( num ) :
    if num == -1 :
        return 
    else :
        print(num)
        printNtoZero(num-1)


num = int(input("Enter a number : "))
printNtoZero ( num )