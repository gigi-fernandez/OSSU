def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    big = max(a,b)
    small= min(a,b)
    if small == 0:
        return big
    else:
        return gcdRecur(b, a%b)

print(gcdRecur(7, 16))