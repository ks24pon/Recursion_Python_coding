def decimalToBinary(decNumber):
    # ベースケース０
    if decNumber == 0:
        return "0"

    # 2進数の結果を追加していく
    binary = ""

    # decNumberが0になるまで
    while decNumber > 0:
        # 余り
        remainder = decNumber % 2
        # 余りを文字列として先頭に追加
        binary = str(remainder) + binary
        # 割った結果をdecNumberとして更新
        decNumber = decNumber // 2

    return binary
