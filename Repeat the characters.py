def repeatAllCharacter ( String ) :
    length = len(String)
    result = ""

    for index in range(length) :
        char = String[index]
        result = result + char + char 

    return result


String = "123A" 
ans = repeatAllCharacter ( String )
print(ans)