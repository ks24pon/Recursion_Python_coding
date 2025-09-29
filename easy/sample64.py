def doubledArray(arr):
    # ベースケース１:要素が1つなら2倍にして返す
    if len(arr) == 1:
        return [arr[0] * 2]

    # ベースケース2：空配列ならそのまま返す
    if len(arr) == 0:
        return []

    # 配列を中央で分割
    mid = len(arr) // 2
    left = arr[:mid] #左半分
    right = arr[mid:] # 右半分

    # 左右を再帰的に処理して、結果を結合
    return doubledArray(left) + doubledArray(right)

