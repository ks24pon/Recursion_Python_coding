def interestsPaid(initialLoan,didPayOnTime):
    # 期限内に支払いなし1.15%
    entai_loan = 1.15

    # 支払えた場合1.02%
    default = 1.02

    # 手数料、2.5
    num = 2.5

    # 合計値
    total = initialLoan

    if didPayOnTime: total = total * default
    else:
        total = total * entai_loan
    return total + num