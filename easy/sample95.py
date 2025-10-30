def recursiveAddition(m,n):
    if n >= 0:
        return m + n

    return recursiveAddition(m,n-1) + m