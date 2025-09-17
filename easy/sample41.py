def swapPosition(s):
    if len(s) <= 1: return s
    return s[1:2] + s[:1] + swapPosition(s[2:])