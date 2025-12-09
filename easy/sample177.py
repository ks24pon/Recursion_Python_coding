def totalSquareArea(x):
    if x <= 1:
        return 1

    return totalSquareArea(x-1) + (x**3)
