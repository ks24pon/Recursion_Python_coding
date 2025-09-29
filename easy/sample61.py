def selectionSort(arr):
    # 配列の長さを取得
    n = len(arr)
    for i in range(n):
        # i番目の位置に入るべき最小値を探す
        minIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # 見つけた最小値をi番目と交換
        if minIndex != i:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr