def interestsPaid(initialLoan, didPayOnTime):
    rate = 0.02 if didPayOnTime else 0.15
    return initialLoan * (1 + rate) + 2.5