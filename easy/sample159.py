import math


def isPerfectSquare(x, y):
    xNum = x*x
    yNum = y*y

    if math.sqrt(xNum + yNum).is_integer():
        return True
        return False
