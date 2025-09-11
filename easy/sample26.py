def insertUnderscoreAt(s,i):
    # アンダースコア前の文字列
    front = s[:i]
    # アンダースコア後の文字列
    back = s[i:]
    if i > len(s):
        return s # iが受け取った文字列サイズ以上の場合
    else:
        return front + "_" + back # それ以外の場合「_」を入れた文字列を返す