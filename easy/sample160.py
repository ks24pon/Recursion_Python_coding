import math


def calculateGoalMoney(capital, year):
    # 年利の初期値
    rate = 0
    if capital % 2 == 0:
        rate += 0.02
    else:
        rate += 0.03

    # 複利の式
    num = capital*(1+rate)**year

    # 出力
    return math.floor(num)
