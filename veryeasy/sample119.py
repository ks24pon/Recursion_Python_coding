def minAndMax(intArr):
    # 現在の最大値
    maxValue = intArr[0]
    # 現在の最小値
    minValue = intArr[0]
    # 配列の合計
    sumValue = 0
    # 結果リスト
    shopList = []
    # 配列チェック
    for i in intArr:
        if maxValue < i:
            maxValue = i
        if minValue > i:
            minValue = i
        sumValue += i

    shopList.append(sumValue-maxValue)
    shopList.append(sumValue-minValue)

    return shopList
