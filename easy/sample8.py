def isSwapBigger(n):
    # 数値を文字列に変換
    str_num = str(n)

    # 文字列を逆順にする
    str_reversed = str_num[::-1]

    # 入れ替えた文
    return str_reversed >= str_num