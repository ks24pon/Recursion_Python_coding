def interestsPaid(initialLoan,didPayOnTime):
  percentLate = 1.15
  percentDefault = 1.02
  serviceFee = 2.5
  total = initialLoan

  # 間に合った場合、デフォルトの利子
  if didPayOnTime: total = total * percentDefault
  # 遅れた場合、割高の利子
  else: total = total * percentLate
  # トータルに$2.5をプラスで請求します
  return total + serviceFee

# 関数の呼び出し
print(interestsPaid(100,True))
print(interestsPaid(100,False))
