def interestsPaid(initialLoan, didPayOnTime):
    # 手数料
    handlingFee = 2.5

    # 期限内にお金が支払われた場合
    if didPayOnTime == True:
        interestRate = 0.02
    else:
        interestRate = 0.15

    # 利子
    interestAmount = initialLoan * interestRate
    # 合計支払額
    TOTAL = initialLoan + interestAmount + handlingFee

    return TOTAL
