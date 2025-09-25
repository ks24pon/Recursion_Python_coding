# 合計がx未満となる最大のペア和を求める
def maxOfPairSum(arr1,arr2,x):
    # 合計の最大値を入れる変数
    maxSum = None

    # arr1,arr2の要素を全て組み合わせる
    for a in arr1:
        for b in arr2:
            # 2つの要素の和を計算
            s = a + b

            # x未満かつ現在のmaxSumより大きければ更新
            if s < x and (maxSum is None or s > maxSum):
                maxSum = s

    # 結果を返す(見つかれば文字列、なあければ"no pair")
    return str(maxSum) if maxSum is not None else "no pair"