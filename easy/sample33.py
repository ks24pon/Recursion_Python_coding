def processPayment(creditCardType ,cost):
# カードチェック：checkCardType が NG（-0.1）なら即 -0.1 を返す
    if checkCardType(creditCardType) == -1.0: return -1.0
# チップ率を決定
    tipRate = askForTip(cost)
# 税込み小計
    subTotal = totalPayment(cost)
# チップ金額
    tipAmount = cost * tipRate
# 総合計
    total = subTotal + tipAmount
    # 300以上なら-1.0,以外なら総合計出す
    if total > 300: return -1.0
    else: return total

# クレジットのチェック関数
def checkCardType(creditCardType):
    if creditCardType != "Visa" and creditCardType != "MasterCard": return -1.0

# 食事を受け取り、チップ計算する関数
def askForTip(cost):
    if cost % 3 == 0: return 0.03
    elif cost % 5 == 0: return 0.05
    elif cost % 7 == 0: return 0.07
    else: return 0.10

# 消費税とチップを使って合計金額の計算(税込の金額)
def totalPayment(cost):
    return cost * 1.10