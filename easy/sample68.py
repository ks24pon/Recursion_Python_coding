def isSwapBigger(n):
    # 文字列変換
    swap = str(n)
    # 2桁入れ替え()
    swapStr = swap[1] + swap[0]
    return swap <= swapStr