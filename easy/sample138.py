def interestsPaid(initialLoan,didPayOnTime):
    # 期限内に支払いない
    percentLate = 1.15
    # 支払われた場合
    percentDefault = 1.02
    # 手数料
    serviceFee = 2.5
    # 合計
    total = initialLoan

    # 間に合った場合、デフォルト利子
    if didPayOnTime:
        total = total * percentDefault
    else:
        total = total * percentLate
    return total + serviceFee