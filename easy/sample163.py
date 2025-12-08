import math

def calculateCorporationTax(state, year, profit):
    # 連邦税
    federalTaxRate = profit * isLeapYear(year)
    # 州税
    stateTaxRate = profit * stateTax(state)

    # 合計
    return math.ceil(federalTaxRate + stateTaxRate)

# 州税を計算する関数
def stateTax(state):
    # 州によって税率変更
    if state == "AZ":
        return 0.049
    if state == "CA":
        return 0.0884
    if state == "TX":
        return 0.0
    if state == "NC":
        return 0.025
    else:
        return 0.05

# 閏年かどうかチェック関数
def isLeapYear(year):
    if year % 400 == 0:
        return 0.0
    if year % 100 == 0:
        return 0.21
    if year % 4 == 0:
        return 0.0
    return 0.21
