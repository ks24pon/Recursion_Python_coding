def totalSquareArea(x):
    # ベースケース
    if x == 1: return 1
    # 再帰
    else: return totalSquareArea(x-1) + x **3