def hideACreditCardNumber (card) :
    length = len(card)
    result = ''

    for index in range(length) :
        char = card[index]
        if index != 0 and index != 1 and index != length - 1 and index != length -2 :
            result = result + 'X' 
        else :
            result = result + char 
        index = index + 1 

    return result


card = "1234553647892678"
ans = hideACreditCardNumber(card) 
print(ans)
