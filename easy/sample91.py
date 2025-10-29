import math

def calculateGoalMoney(capital,year):

    def calculateInterestRate(capital):
        if capital % 2 == 0:
            return 0.02
        else:
            return 0.03

    rate = calculateInterestRate(capital)
    amount = capital * math.pow(1+rate,year)
    return math.floor(amount)