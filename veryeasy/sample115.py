def getMaxIndex(arr):
    # 最大値
    maxIndex = 0

    # 1つずつ比較して大きければ更新
    for i in range(len(arr)):
        if arr[i] > arr[maxIndex]:
            maxIndex = i
    return maxIndex