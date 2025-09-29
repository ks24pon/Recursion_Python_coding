def sumOfArray(arr):
    # ベースケース1：要素が1つならその値を返す
    if len(arr) == 1:
        return arr[0]

    # ベースケース2：空配列なら0を返す
    if len(arr) == 0:
        return 0

    # 配列を中央で分割
    mid = len(arr) // 2
    left = arr[:mid] # 左半分
    right = arr[mid:] # 右半分

    # 左右を再帰的に合計
    leftSum = sumOfArray(left)
    rightSum = sumOfArray(right)

    # 左右の結果を結合して返す
    return leftSum + rightSum
