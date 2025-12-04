import math

def calculateInterestRate(capital):
  # 偶数or奇数チェック
  if capital % 2 == 0:
    return 0.02
  else:
    return 0.03
  
def calculateGoalMoney(capital,year):
  # 年利
  rate = calculateInterestRate(capital)

  # 複利の式
  num = capital*(1+rate)**year

  # 出力
  return math.floor(num)