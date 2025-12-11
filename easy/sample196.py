import math

def isPalindromeInteger(n):
    # 数字を文字列に
    s = str(n)
    # 長さを求める
    length = len(s)
    # 真ん中の位置を求める
    mid = math.floor(length/2)

    # 左右から1文字ずつループ
    for i in range(mid +1):
        # 左右の対応する文字比較
        if s[i] != s[length -1 -i]: return False
    
    return True
