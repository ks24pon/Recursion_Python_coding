# 2つの数を足してtargetになる組み合わせを探す関数
def canMakeTargetVal(arr, target):
    # 配列の要素を1つずつ取り出し、インデックスも利用
    for i, a in enumerate(arr):
        # 自分より後ろの要素だけをループ(i+1から最後まで)
        for j in range(i + 1, len(arr)):
            b = arr[j] # j番目の要素をbに格納

            # a + b がtargetに一致するかチェック
            if a + b == target:
                return True # 条件を満たすペアが見つかればTrueを返す

    # 最後まで調べても見つからなければFalse
    return False