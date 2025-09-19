def countCharactersAfterN(arr):
    # カウント用の変数を初期化
    count = 0

    # リストに含まれる各文字列を順に取り出す
    for s in arr:
        # 文字列の中の各文字を取り出す
        for ch in s:
            # 文字コードを使って比較('n'以降の文字ならカウント)
            if ord(ch) >= ord("n"):
                count += 1
    return count

