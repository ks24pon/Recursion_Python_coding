import math

def calculateGoalMoney(capital,year):
    # 整数を受け取って偶数なら0.02%,奇数なら0.03%を返す関数
    def calculateInterestRate(capital):
        if capital % 2 == 0:
            return 0.02
        else:
            return 0.03
    return math.floor(capital * pow(1 + calculateInterestRate(capital),year))



