def recursiveAddition(m,n):
    if n <= 0:
        return m

    return recursiveAddition(m + 1, n - 1)
