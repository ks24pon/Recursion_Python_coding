def insertUnderscoreAt(s,i):
    front = s[:i]
    back = s[i:]
    if i >= len(s): return s
    else: return front + "_" + back