def power(x, n):
    """ Calculate 'x' to the power of 'n'. """
    result = 1
    for i in range(n):
        result = result * x
        
    return result