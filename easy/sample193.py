def notDivisibleNumbers(x, y):
    # x == 1 かつ y == 1は除外
    if x == 1 and y == 1:
        return ""
    
    # カウントを初期化
    count = []

    # 1からxまでループ
    for i in range(1, x+1):
        # yで割り切れない場合
        if i % y != 0:
            # 追加
            count.append(str(i))

    # リストを"-"で連結して1つの文字列にして返す
    return "-".join(count)