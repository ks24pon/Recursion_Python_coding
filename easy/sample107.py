def reverseString(s):
    # ベースケース
    if s == "":
        return ""
    # 再帰
    return s[len(s)-1] + reverseString(s[:len(s)-1])