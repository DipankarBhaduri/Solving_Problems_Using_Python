#   Calcious = ((( Fahrenheit - 32 ) * 5 ) / 9 ) 

def convertFahrenheitToCelsius ( F ) :
    C = ((( F - 32 ) * 5 ) / 9 )
    return C 


F = input ( "Enter the temparature in Fahrenheit : ") 
C = convertFahrenheitToCelsius ( int(F) ) 
print ( C // 1 ) 