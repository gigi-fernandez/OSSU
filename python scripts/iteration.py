def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    carry = 1
    if (exp == 0):
        base = 1
    while exp > 0:
        carry = carry * base
        exp-=1
    return carry

print(iterPower(2,4))
print(iterPower(3,3))