import math

def howMuchIsYourDebt(year):
    # 年利
    num = 0.2
    money = 10000
    
    return math.floor(money * math.pow((1+num),year))