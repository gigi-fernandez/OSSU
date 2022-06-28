def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = max(a,b)
    while (a % gcd != 0) or (b % gcd != 0):
        gcd-=1
    return gcd

print(gcdIter(9, 15))
