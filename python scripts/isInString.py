def isIn(char, aStr):
    if (aStr) == '':
        return False

    if (len(aStr) == 1):
        return aStr == char

    midIndex = len(aStr)//2
    midChar = aStr[midIndex]
    if (midChar == char):
        return True
        
    elif (midChar > char):
        return isIn(char, aStr[:midIndex])
    else:
        return isIn(char, aStr[midIndex+1:])

isIn('j', 'eux')