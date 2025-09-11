import math

def howMuchIsYourDebt(year):
    amount = 10000
    num = 0.2
    return math.floor(amount * math.pow(1 + num, year))