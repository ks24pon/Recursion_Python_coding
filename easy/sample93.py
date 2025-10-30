# カードチェック関数
def checkCardType(creditCardType):
    return creditCardType in ["Visa", "MasterCard"]

# 食事代を受け取り、チップを計算する関数
def askForTip(cost):
    if cost % 3 == 0:
        return cost * 0.03
    elif cost % 5 == 0:
        return cost * 0.05
    elif cost % 7 == 0:
        return cost * 0.07
    else:
        return cost * 0.10

def processPayment(creditCardType, cost):
    # クレジットケード確認
    if not checkCardType(creditCardType):
        return -1.0
    # 消費税
    tax = cost * 0.10
    # チップ
    tip = askForTip(cost)
    # 合計数
    total = cost + tax + tip

    # 残高オーバー
    if total > 300:
        return -1.0

    return total

    # return round(totalPayment, 2)