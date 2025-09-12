import math

def calculateCorporationTax(state,year,profit):
    if isLeapYear(year):
        return math.ceil(profit * stateTax(state))
    else:
        return math.ceil(profit * stateTax(state) + profit * 0.21)

# 州名を受け取り、州税を計算する関数
def stateTax(state):
    if state == "AZ": return 0.049
    elif state == "CA": return 0
    elif state == "NC": return 0.025
    else: return 0.05

# 閏年チェック関数
def isLeapYear(year):
    if year % 400 == 0: return True
    elif year % 100 == 0: return False
    elif year % 4 == 0: return True
    else: return False