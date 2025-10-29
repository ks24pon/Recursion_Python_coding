import math

def isPerfectSquare(x,y):
    def distance(x,y):
        z = math.sqrt(pow(x,2)+pow(y,2))
        return z

    def hasDecimal(z):
        return not z % 1 == 0

    return not hasDecimal(distance(x,y))