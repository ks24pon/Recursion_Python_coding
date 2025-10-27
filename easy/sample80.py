def deleteAt(s,i):
    # 返す文字がない場合
    if i == 0 or i > len(s): return s
    else:
        front = s[:i-1]
        back = s[i:]
        return front + back
