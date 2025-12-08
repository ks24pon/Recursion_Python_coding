def processPayment(creditCardType, cost):
    if not checkCardType(creditCardType):
        return -1.0
    # 消費税
    tax = cost * 0.10
    # チップ
    tip = askForTip(cost)
    # 合計値
    totalPayment = cost + tax + tip
    # 合計300ドル超えると残高不足になり-1.0返す
    if totalPayment > 300:
        return -1.0

    return totalPayment

# VisaかMasterCardチェック関数
def checkCardType(creditCardType):
    return creditCardType in ["Visa", "MasterCard"]

# 食事代を受け取りチップ計算関数
def askForTip(cost):
    if cost % 3 == 0:
        return cost * 0.03
    if cost % 5 == 0:
        return cost * 0.05
    if cost % 7 == 0:
        return cost * 0.07
    else:
        return cost * 0.10
