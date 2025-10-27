def interestsPaid(initialLoan,didPayOnTime):
    # 期限内
    DEFAULTPERCENT = 1.02
    # 期限外
    DEADPERCENT = 1.15
    # 手数料
    FEE = 2.5

    # 合計
    total = initialLoan

    if didPayOnTime:
        total *= DEFAULTPERCENT
    else:
        total *= DEADPERCENT
    return total + FEE

