def countCharactersAfterN(arr):
    # 文字列の配列を受け取る関数
    count = 0
    # 配列の中の各文字列を1つずつ取り出す
    for i in arr:
        # また1文字ずつ取り出す
        for s in i:
            if ord("n") <= ord(s):
                count += 1
    # 全て条件を満たした文字数を返す
    return count