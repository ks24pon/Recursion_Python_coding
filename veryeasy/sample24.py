def getMaxIndex(arr):
    # 最初の要素を仮の最大値として設定
    maxValueIndex = 0
    # 配列の要素を順番にチェック
    for i in range(len(arr)):
        # もし現在の値が最大値以上なら
        if arr[i] >= arr[maxValueIndex]:
            # 最大値のインデックスを更新
            maxValueIndex = i
    # 最終的なインデックスを返す
    return maxValueIndex