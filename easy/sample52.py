# 各文字の ASCII 値の合計が最大になる関数
def maxAscilString(stringList):
    # 最初の文字列を初期値
    maxIndex = 0

    # stringList[0]の各文字も値を合計
    maxValue = sum(ord(c) for c in stringList[0])

    # 配列の各要素をインデックス付きでループ処理
    for i, s in enumerate(stringList):
        # 各文字のASCll合計値計算
        asciiSum = sum(ord(c) for c in s)

        # もし現在の合計がこれまでの最大より大きければ、値とインデックスを更新
        if asciiSum > maxValue:
            maxValue = asciiSum
            maxIndex = i
    # 最大のASCII合計値を持つ文字列インデックスを返す
    return maxIndex