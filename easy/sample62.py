def insertionSort(arr):
    # 2番目の要素から順に処理
    for i in range(1, len(arr)):
        # 挿入したい値を一時的に保存
        key = arr[i]
        # keyの直前の要素を指すインデックス
        j = i -1

        # keyより大きい要素を右に1つずつシフトして空きを作る
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # 空いた位置にkeyを挿入
        arr[j + 1] = key

    # ソート済みの配列を返す
    return arr