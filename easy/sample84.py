import math

def howMuchIsYourDebt(year):
    interest = 1.2
    initialDebt = 10000

    return math.floor(initialDebt * math.pow(interest,year))