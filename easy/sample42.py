def numberOfDots(x):
    # ベースケース
    if x <= 1:
        return 1
    return numberOfDots(x-1) + x