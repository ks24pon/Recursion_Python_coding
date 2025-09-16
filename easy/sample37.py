def simpleSummation(n):
    if n <= 0:
        return 0
    return simpleSummation(n-1) + n