def recursiveAddition(m,n):
    if n <= 0:
        return m
    return recursiveAddition(m, n-1) + 1

